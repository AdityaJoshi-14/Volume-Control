import cv2
import numpy as np
from hand_tracker import HandTracker
from volume_controller import set_volume

# Global settings
last_volume = None
change_threshold = 5  # Minimum volume change to trigger update
gesture_enabled = True  # Toggle gesture control

def calculate_distance(p1, p2):
    x1, y1 = p1[1], p1[2]
    x2, y2 = p2[1], p2[2]
    distance = np.hypot(x2 - x1, y2 - y1)
    return distance, (x1, y1), (x2, y2)

def map_range(value, input_min, input_max, output_min, output_max):
    return int(np.interp(value, [input_min, input_max], [output_min, output_max]))

def main():
    global last_volume, gesture_enabled

    cap = cv2.VideoCapture(0)
    tracker = HandTracker()

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        frame = tracker.find_hands(frame)
        landmarks = tracker.get_landmark_positions(frame)

        if landmarks:
            thumb_tip = landmarks[4]
            index_tip = landmarks[8]
            distance, p1, p2 = calculate_distance(thumb_tip, index_tip)

            # Visual feedback
            cv2.line(frame, p1, p2, (0, 255, 0), 2)
            cv2.circle(frame, p1, 8, (0, 0, 255), -1)
            cv2.circle(frame, p2, 8, (0, 0, 255), -1)

            # Map gesture distance to volume percentage
            volume = map_range(distance, 30, 200, 0, 100)

            if gesture_enabled:
                if last_volume is None or abs(volume - last_volume) > change_threshold:
                    set_volume(volume)
                    last_volume = volume

            # Volume bar
            cv2.rectangle(frame, (50, 150), (85, 400), (255, 255, 255), 2)
            bar_height = int(np.interp(volume, [0, 100], [400, 150]))
            cv2.rectangle(frame, (50, bar_height), (85, 400), (0, 255, 0), -1)
            cv2.putText(frame, f'{volume} %', (40, 430), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Gesture lock status display
        if not gesture_enabled:
            cv2.putText(frame, "🔒 Volume Locked", (180, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        else:
            cv2.putText(frame, "🔓 Volume Unlocked", (180, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Gesture Volume Control", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('g'):
            gesture_enabled = not gesture_enabled
            print(f"[INFO] Gesture Control {'Enabled' if gesture_enabled else 'Disabled'}")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

