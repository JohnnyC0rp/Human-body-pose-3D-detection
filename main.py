import mediapipe as mp
import cv2
import functions

# initialize pose estimator
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    # read frame 11 13 15
    _ , frame = cap.read()
    
    # convert to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # process the frame for pose detection
    pose_results = pose.process(frame_rgb)
    # print(pose_results.pose_landmarks)
    
    # draw skeleton on the frame
    mp_drawing.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    if pose_results.pose_landmarks is not None:    
        # print(pose_results.pose_landmarks.landmark[9].x)
        # print(frame.shape)
        print("\r", functions.get_angle_from_3_points(
            functions.proportional_to_pixel(frame.shape,[pose_results.pose_landmarks.landmark[11].x,pose_results.pose_landmarks.landmark[11].y]),
            functions.proportional_to_pixel(frame.shape,[pose_results.pose_landmarks.landmark[13].x,pose_results.pose_landmarks.landmark[13].y]),
            functions.proportional_to_pixel(frame.shape,[pose_results.pose_landmarks.landmark[15].x,pose_results.pose_landmarks.landmark[15].y]),
        ),end="")
    print("-"*20)

    # display the frame
    cv2.imshow('Output', frame)
    
    if cv2.waitKey(1) == ord('q'):
          break
          
cap.release()
cv2.destroyAllWindows()




# def draw_landmarks(
#     image: np.ndarray,
#     landmark_list: landmark_pb2.NormalizedLandmarkList,
#     connections: Optional[List[Tuple[int, int]]] = None,
#     landmark_drawing_spec: Union[DrawingSpec,
#                                  Mapping[int, DrawingSpec]] = DrawingSpec(
#                                      color=RED_COLOR),
#     connection_drawing_spec: Union[DrawingSpec,
#                                    Mapping[Tuple[int, int],
#                                            DrawingSpec]] = DrawingSpec()):
#   """Draws the landmarks and the connections on the image.

#   Args:
#     image: A three channel BGR image represented as numpy ndarray.
#     landmark_list: A normalized landmark list proto message to be annotated on
#       the image.
#     connections: A list of landmark index tuples that specifies how landmarks to
#       be connected in the drawing.
#     landmark_drawing_spec: Either a DrawingSpec object or a mapping from hand
#       landmarks to the DrawingSpecs that specifies the landmarks' drawing
#       settings such as color, line thickness, and circle radius. If this
#       argument is explicitly set to None, no landmarks will be drawn.
#     connection_drawing_spec: Either a DrawingSpec object or a mapping from hand
#       connections to the DrawingSpecs that specifies the connections' drawing
#       settings such as color and line thickness. If this argument is explicitly
#       set to None, no landmark connections will be drawn.

#   Raises:
#     ValueError: If one of the followings:
#       a) If the input image is not three channel BGR.
#       b) If any connetions contain invalid landmark index.
#   """
#   if not landmark_list:
#     return
#   if image.shape[2] != _BGR_CHANNELS:
#     raise ValueError('Input image must contain three channel bgr data.')
#   image_rows, image_cols, _ = image.shape
#   idx_to_coordinates = {}
#   for idx, landmark in enumerate(landmark_list.landmark):
#     if ((landmark.HasField('visibility') and
#          landmark.visibility < _VISIBILITY_THRESHOLD) or
#         (landmark.HasField('presence') and
#          landmark.presence < _PRESENCE_THRESHOLD)):
#       continue
#     landmark_px = _normalized_to_pixel_coordinates(landmark.x, landmark.y,
#                                                    image_cols, image_rows)
#     if landmark_px:
#       idx_to_coordinates[idx] = landmark_px
#   if connections:
#     num_landmarks = len(landmark_list.landmark)
#     # Draws the connections if the start and end landmarks are both visible.
#     for connection in connections:
#       start_idx = connection[0]
#       end_idx = connection[1]
#       if not (0 <= start_idx < num_landmarks and 0 <= end_idx < num_landmarks):
#         raise ValueError(f'Landmark index is out of range. Invalid connection '
#                          f'from landmark #{start_idx} to landmark #{end_idx}.')
#       if start_idx in idx_to_coordinates and end_idx in idx_to_coordinates:
#         drawing_spec = connection_drawing_spec[connection] if isinstance(
#             connection_drawing_spec, Mapping) else connection_drawing_spec
#         cv2.line(image, idx_to_coordinates[start_idx],
#                  idx_to_coordinates[end_idx], drawing_spec.color,
#                  drawing_spec.thickness)
#   # Draws landmark points after finishing the connection lines, which is
#   # aesthetically better.
#   if landmark_drawing_spec:
#     for idx, landmark_px in idx_to_coordinates.items():
#       drawing_spec = landmark_drawing_spec[idx] if isinstance(
#           landmark_drawing_spec, Mapping) else landmark_drawing_spec
#       # White circle border
#       circle_border_radius = max(drawing_spec.circle_radius + 1,
#                                  int(drawing_spec.circle_radius * 1.2))
#       cv2.circle(image, landmark_px, circle_border_radius, WHITE_COLOR,
#                  drawing_spec.thickness)
#       # Fill color into the circle
#       cv2.circle(image, landmark_px, drawing_spec.circle_radius,
#                  drawing_spec.color, drawing_spec.thickness)