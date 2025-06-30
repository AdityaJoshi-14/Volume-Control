# ✋ Gesture-Based Volume Control (Linux Edition)

Control your **system volume using hand gestures** via webcam!  
Built with **Python**, **OpenCV**, **MediaPipe**, and **PulseAudio**.  
Designed to work smoothly on **Ubuntu/Linux** systems.

---

## 🎥 Features

- Real-time hand tracking with MediaPipe
- Volume control via thumb–index finger distance
- On-screen volume bar and lock/unlock status
- Toggle gesture control on/off via keyboard (`g`)
- Quit app anytime with `q`
- Launchable as a Linux desktop app

---

## 📁 Project Structure

gesture_volume/
├── main.py # Main application logic
├── hand_tracker.py # MediaPipe hand tracking logic
├── volume_controller.py # Volume control using pactl
├── launch.sh # Launcher script (for .desktop)
├── requirements.txt # Python dependencies
└── README.md # You're reading it!

yaml
Copy
Edit

---

## ⚙️ Installation Instructions

### ✅ 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/gesture-volume-control.git
cd gesture-volume-control
✅ 2. Create and activate a Conda environment
bash
Copy
Edit
conda create -n gesture_volume python=3.10 -y
conda activate gesture_volume
✅ 3. Install Python dependencies
bash
Copy
pip install -r requirements.txt
✅ 4. Install system dependency
bash
Copy

sudo apt update
sudo apt install pulseaudio-utils
✅ 5. Run the application
bash
Copy
Edit
python main.py
You should see:

Webcam feed

Landmarks and hand tracking

Live volume bar

Gesture-based volume changes

g key to lock/unlock control

q key to quit

🖥️ Optional: Launch as a Linux Desktop App
➤ 1. Create a launcher script
bash
Copy
Edit
nano launch.sh
Paste this, and modify the path as needed:

bash
Copy
Edit
#!/bin/bash
source ~/anaconda3/bin/activate gesture_volume
python /home/YOUR_USERNAME/path/to/gesture_volume/main.py
Save and make it executable:

bash
Copy
Edit
chmod +x launch.sh
➤ 2. Create a desktop launcher
bash
Copy
Edit
nano ~/.local/share/applications/gesture-volume.desktop
Paste and adjust paths:

ini
Copy
Edit
[Desktop Entry]
Name=Gesture Volume Control
Comment=Control volume with hand gestures
Exec=/home/YOUR_USERNAME/path/to/gesture_volume/launch.sh
Icon=/home/YOUR_USERNAME/path/to/gesture_volume/icon.png
Terminal=false
Type=Application
Categories=Utility;
Make it executable:

bash
Copy
Edit
chmod +x ~/.local/share/applications/gesture-volume.desktop
Now you’ll find Gesture Volume Control in your Applications menu 🎉

🎮 Controls
Key	Action
g	Toggle gesture control ON/OFF
q	Quit application

🧩 requirements.txt
shell
Copy
Edit
opencv-python>=4.7
mediapipe==0.10.3
numpy>=1.21
To install:

bash
Copy
Edit
pip install -r requirements.txt
🧰 Customization
You can tweak the behavior in main.py:

Adjust map_range(...) for finer volume control

Change change_threshold to reduce volume jumpiness

Replace or disable the on-screen lock/unlock status

📌 Notes
Use Python 3.10 (MediaPipe not stable on Python 3.12+ yet)

Ensure webcam works and isn’t in use by other apps

Test on Ubuntu 20.04 or 22.04 for best results

🧑‍💻 Contributing
PRs and suggestions are welcome. Fork the repo, make your changes, and submit a pull request.

📜 License
MIT License. See LICENSE file.

🙌 Credits
MediaPipe by Google

OpenCV

PulseAudio
