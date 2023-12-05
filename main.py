import mediapipe as mp
import cv2
import my_cv2_drawer
from matplotlib_3d_visualizer import RealTimeScatter
import threading

# import test_3D_visualizer


def main_video_processing_function():
    cap = cv2.VideoCapture("test2.mp4")
    while cap.isOpened():
        _, frame = cap.read()

        # frame = cv2.resize(frame, (350, 600))

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        pose_results = pose.process(frame_rgb)
        # print(pose_results.pose_landmarks)

        plot.load_new_landmarks(pose_results.pose_landmarks.landmark)

        if pose_results.pose_landmarks:
            my_cv2_drawer.draw_landmarks(frame, pose_results.pose_landmarks)
        # draw skeleton on the frame
        # mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # if pose_results.pose_landmarks is not None:
        # print(pose_results.pose_landmarks.landmark[9].x)
        # print(frame.shape)
        # print("\r", functions.get_angle_from_3_points(
        #     functions.proportional_to_pixel(frame.shape,[pose_results.pose_landmarks.landmark[11].x,pose_results.pose_landmarks.landmark[11].y]),
        #     functions.proportional_to_pixel(frame.shape,[pose_results.pose_landmarks.landmark[13].x,pose_results.pose_landmarks.landmark[13].y]),
        #     functions.proportional_to_pixel(frame.shape,[pose_results.pose_landmarks.landmark[15].x,pose_results.pose_landmarks.landmark[15].y]),
        # ),end="")
        # print("-"*20)

        # display the frame
        cv2.imshow("Output", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

threading.Thread(target=main_video_processing_function).start()

plot = RealTimeScatter()
plot.show()
