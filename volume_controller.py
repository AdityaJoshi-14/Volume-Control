import subprocess

def set_volume(volume_percent):
    volume_percent = int(max(0, min(100, volume_percent)))  # Clamp between 0–100%
    try:
        subprocess.run(
            ["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{volume_percent}%"],
            check=True
        )
        print(f"[INFO] Volume set to {volume_percent}%")
    except subprocess.CalledProcessError as e:
        print("[ERROR] Failed to set volume:", e)

