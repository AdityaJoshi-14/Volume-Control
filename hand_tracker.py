import os
import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, max_hands=1, detection_confidence=0.7, tracking_confidence=0.7):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, frame, draw=True):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb_frame)

        if self.results.multi_hand_landmarks and draw:
            for handLms in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, handLms, self.mp_hands.HAND_CONNECTIONS)
            # Load and overlay logo
        logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
        logo = cv2.imread(logo_path, cv2.IMREAD_UNCHANGED)
        if logo is not None:
            logo_resized = cv2.resize(logo, (100, 100))
            x_offset, y_offset = 10, 10
            y1, y2 = y_offset, y_offset + logo_resized.shape[0]
            x1, x2 = x_offset, x_offset + logo_resized.shape[1]

            if logo_resized.shape[2] == 4:
                alpha_s = logo_resized[:, :, 3] / 255.0
                alpha_l = 1.0 - alpha_s

                for c in range(3):
                    frame[y1:y2, x1:x2, c] = (alpha_s * logo_resized[:, :, c] +
                                          alpha_l * frame[y1:y2, x1:x2, c])
            else:
                frame[y1:y2, x1:x2] = logo_resized
        return frame

    def get_landmark_positions(self, frame, hand_index=0):
        h, w, _ = frame.shape
        landmark_list = []

        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_index]
            for id, lm in enumerate(my_hand.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_list.append((id, cx, cy))

        return landmark_list

