

```markdown
# ✋ Gesture-Based Volume Control (Linux Edition)

Control your **system volume using hand gestures** via webcam!  
Built with **Python**, **OpenCV**, **MediaPipe**, and **PulseAudio**.  
Designed for Ubuntu/Linux systems.

---

## 🎥 Features

- Real-time hand tracking using MediaPipe
- System volume control via thumb–index finger distance
- Live on-screen volume bar and lock/unlock status
- Toggle gesture control ON/OFF using the `g` key
- Quit any time using `q`
- Launchable as a Linux desktop app

---

## 📁 Project Structure

```

gesture\_volume/
├── main.py                 # Main app logic
├── hand\_tracker.py         # Hand tracking via MediaPipe
├── volume\_controller.py    # Volume control using pactl
├── launch.sh               # Script to launch app from desktop
├── requirements.txt        # Python dependencies
└── README.md               # You're reading it!

````

---

## ⚙️ Installation Instructions

### ✅ 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/gesture-volume-control.git
cd gesture-volume-control
````

---

### ✅ 2. Create and activate a Conda environment

```bash
conda create -n gesture_volume python=3.10 -y
conda activate gesture_volume
```

---

### ✅ 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

### ✅ 4. Install system dependency

```bash
sudo apt update
sudo apt install pulseaudio-utils
```

---

### ✅ 5. Run the application

```bash
python main.py
```

You should see:

* Your webcam feed
* Real-time hand tracking
* A live volume bar
* Gesture-based volume control
* `g` key to lock/unlock
* `q` to quit

---

## 🖥️ Optional: Add to Applications Menu (Linux App)

### ➤ Step 1: Create a launcher script

```bash
nano launch.sh
```

Paste:

```bash
#!/bin/bash
source ~/anaconda3/bin/activate gesture_volume
python /home/YOUR_USERNAME/path/to/gesture_volume/main.py
```

> Replace `YOUR_USERNAME` and path as needed.

Save and make it executable:

```bash
chmod +x launch.sh
```

---

### ➤ Step 2: Create a `.desktop` file

```bash
nano ~/.local/share/applications/gesture-volume.desktop
```

Paste the following:

```ini
[Desktop Entry]
Name=Gesture Volume Control
Comment=Control system volume using hand gestures
Exec=/home/YOUR_USERNAME/path/to/gesture_volume/launch.sh
Icon=/home/YOUR_USERNAME/path/to/gesture_volume/icon.png
Terminal=false
Type=Application
Categories=Utility;
```

Make it executable:

```bash
chmod +x ~/.local/share/applications/gesture-volume.desktop
```

> Now you can launch your app from the **Applications menu** 🎉

---

## 🎮 Keyboard Controls

| Key | Action                        |
| --- | ----------------------------- |
| `g` | Toggle gesture control ON/OFF |
| `q` | Quit application              |

---

## 🧩 `requirements.txt`

```
opencv-python>=4.7
mediapipe==0.10.3
numpy>=1.21
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🧰 Customization Tips

* Adjust volume range by modifying `map_range(...)` in `main.py`
* Change gesture smoothing sensitivity with `change_threshold`
* Customize lock/unlock text or visual feedback

---

## 📌 Notes

* Use **Python 3.10** (MediaPipe is not stable on Python 3.12+)
* Ensure your webcam is connected and available
* Works best on Ubuntu 20.04 / 22.04 with PulseAudio

---

## 🧑‍💻 Contributing

Pull requests and suggestions are welcome!
Fork the repo, make changes, and submit a PR.

---

## 📜 License

MIT License. See `LICENSE` file for details.

---

## 🙌 Credits

* [MediaPipe](https://github.com/google/mediapipe) by Google
* [OpenCV](https://opencv.org/)
* [PulseAudio](https://www.freedesktop.org/wiki/Software/PulseAudio/)

---

> Made with 🖐️ and 🐍 on Ubuntu


```
