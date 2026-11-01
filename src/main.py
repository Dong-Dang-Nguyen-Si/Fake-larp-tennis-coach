import cv2
import numpy as np
import time
from collections import deque
import asyncio
import websockets
import json
import threading
from flask import Flask, Response
from flask_cors import CORS

# 1. KHỞI TẠO FLASK SERVER (Cho Video Stream)
app = Flask(__name__)
CORS(app) # Cho phép Web Three.js load ảnh

telemetry_data = {"vx": 0.0, "vy": 0.0, "detected": False}

# 2. KHỞI TẠO WEBSOCKET (Cho Data Stream)
async def data_handler(websocket):
    while True:
        await websocket.send(json.dumps(telemetry_data))
        await asyncio.sleep(0.05) # 20 Hz

# Thay đổi: Bao bọc server trong một hàm async và dùng 'async with'
async def run_ws_server():
    async with websockets.serve(data_handler, "localhost", 8765):
        await asyncio.Future()  # Giữ cho server chạy vĩnh viễn

def start_ws():
    # asyncio.run() sẽ tự động tạo và quản lý event loop an toàn trong thread này
    asyncio.run(run_ws_server())

threading.Thread(target=start_ws, daemon=True).start()
# 3. VÒNG LẶP XỬ LÝ OPENCV & PHÁT VIDEO
def generate_frames():
    cap = cv2.VideoCapture(0)
    history = deque(maxlen=10)
    
    # Dải màu xanh dương (Bottle Cap)
    lower_color = np.array([95, 100, 60])
    upper_color = np.array([135, 255, 255])

    while True:
        success, frame = cap.read()
        if not success: break

        current_time = time.time()
        
        # --- LOGIC XỬ LÝ MÀU CỦA BẠN (Tóm tắt) ---
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_color, upper_color)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            ((u, v), radius) = cv2.minEnclosingCircle(c)
            if radius > 10:
                history.append((current_time, u, v))
                cv2.circle(frame, (int(u), int(v)), int(radius), (0, 255, 0), 2)
                telemetry_data["detected"] = True
                
                # Tính v_x, v_y đơn giản bằng pixel/s
                if len(history) >= 2:
                    dt = history[-1][0] - history[-2][0]
                    if dt > 0:
                        telemetry_data["vx"] = (history[-1][1] - history[-2][1]) / dt / 100.0
                        telemetry_data["vy"] = -(history[-1][2] - history[-2][2]) / dt / 100.0 # Trục Y lật ngược
        else:
            telemetry_data["detected"] = False

        # Encode frame thành JPEG để stream lên web
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    print("Khởi động API Stream Video và Data...")
    app.run(host='0.0.0.0', port=5000, threaded=True)