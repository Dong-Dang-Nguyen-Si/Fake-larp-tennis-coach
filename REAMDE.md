========================================================================



&#x20;      DIGITAL TWIN: 3D TENNIS TRACKING \& 6-DOF ROBOTIC SYSTEM



========================================================================







1\. INSTALL DEPENDENCIES (Run once initially)



\------------------------------------------------------------------------



Open Terminal or Command Prompt (CMD) and run the following command:







&#x20;   pip install opencv-python numpy websockets flask flask-cors











2\. HOW TO LAUNCH THE SYSTEM (2 Steps)



\------------------------------------------------------------------------



STEP 1: Start the Camera Tracker (Python Backend)



&#x20; - Open the project folder in VS Code or Terminal/CMD.



&#x20; - Run the python script:



&#x20;       python main.py



&#x20; - Keep this terminal window running in the background (do not close it).







STEP 2: Launch the 3D Interface (Web Frontend)



&#x20; - In VS Code: Right-click "index.html" -> Select "Open with Live Server".



&#x20; - Or open Chrome/Brave and navigate to: http://127.0.0.1:5500/index.html



&#x20; - Note: If using Brave Browser and the 3D scene appears black, disable



&#x20;   "Brave Shields" (the lion icon in the address bar).











3\. OPERATIONAL MODES \& PRESENTATION GUIDE



\------------------------------------------------------------------------



\[1] Mode 1: Simulation (Test)



&#x20; - Click and drag the tennis ball directly in 3D space to inspect



&#x20;   real-time velocity vectors and PTV camera coordinates.



&#x20; - Click "Toggle Auto-Fly Mode" to observe automated parabolic flight.



&#x20; - Ball ground impacts will leave red impact marks on the court.







\[2] Mode 2: Real Match (YOLO)



&#x20; - Click any point on the court surface to lock the target landing zone.



&#x20; - Swing your hand (or a bottle cap) across your webcam to launch the ball.



&#x20; - The system projects the predicted trajectory (dashed line), Magnus



&#x20;   spin dynamics (Topspin / Slice), and calculated impact coordinates.







\[3] Mode 3: Robot Match (6-DOF Robotic Defense)



&#x20; - Click 1: Select the landing point on the Robot's side (far court).



&#x20; - Click 2: Select the return target point on your side (near court).



&#x20; - The Robot will slide along its horizontal rail to align with the ball.



&#x20; - Swing across the webcam: The ball flies over -> Robot swings its racket



&#x20;   and returns the ball directly to Click 2.







\[4] Useful Shortcuts:



&#x20; - SPACEBAR: Resets ball position and clears active target markers.



&#x20; - "Clear Impact Marks" button: Clears all red impact marks on the court.



========================================================================

