import cv2
import functions


def draw_landmarks(image, landmarks):
    image_rows, image_cols, _ = image.shape
    for landmark in landmarks.landmark:
        # if ((landmark.HasField('visibility') and
        #     landmark.visibility < _VISIBILITY_THRESHOLD) or
        #     (landmark.HasField('presence') and
        #     landmark.presence < _PRESENCE_THRESHOLD)):
        # continue
        landmark_px = functions.proportional_to_pixel(
            [image_cols, image_rows], [landmark.x, landmark.y]
        )

        landmark_color = (0, 0, 255)
        draw_one_landmark(image, landmark_px, color=landmark_color)


def draw_one_landmark(image, pos, radius=10, color=(0, 255, 0)):
    cv2.circle(image, pos, radius, color=color, thickness=5)


def draw_connections(landmarks):
    pass


def draw_one_connection(pos):
    pass
