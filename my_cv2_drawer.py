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
        landmark_px = functions.proportional_to_pixel([image_cols,image_rows], [landmark.x, landmark.y])

        landmark_color = (0,0,abs(landmark.z)*120) #if landmark.visibility > 0.8 else (0,0,255)
        draw_one_landmark(image, landmark_px, color=landmark_color)

def draw_one_landmark(image,pos,radius=10,color=(0,255,0)):
    cv2.circle(image, pos, radius, color=color,thickness=5)
                #  drawing_spec.thickness)
      # Fill color into the circle
    # cv2.circle(image, landmark_px, drawing_spec.circle_radius,
    #             drawing_spec.color, drawing_spec.thickness)

def draw_connections(landmarks):
    pass

def draw_one_connection(pos):
    pass

def draw_landmarks_(
    # image: np.ndarray,
    # landmark_list: landmark_pb2.NormalizedLandmarkList,
    # connections: Optional[List[Tuple[int, int]]] = None
    ):
  """Draws the landmarks and the connections on the image.

  Args:
    image: A three channel BGR image represented as numpy ndarray.
    landmark_list: A normalized landmark list proto message to be annotated on
      the image.
    connections: A list of landmark index tuples that specifies how landmarks to
      be connected in the drawing.
    landmark_drawing_spec: Either a DrawingSpec object or a mapping from hand
      landmarks to the DrawingSpecs that specifies the landmarks' drawing
      settings such as color, line thickness, and circle radius. If this
      argument is explicitly set to None, no landmarks will be drawn.
    connection_drawing_spec: Either a DrawingSpec object or a mapping from hand
      connections to the DrawingSpecs that specifies the connections' drawing
      settings such as color and line thickness. If this argument is explicitly
      set to None, no landmark connections will be drawn.

  Raises:
    ValueError: If one of the followings:
      a) If the input image is not three channel BGR.
      b) If any connetions contain invalid landmark index.
  """



  if connections:
    num_landmarks = len(landmark_list.landmark)
    # Draws the connections if the start and end landmarks are both visible.
    for connection in connections:
      start_idx = connection[0]
      end_idx = connection[1]
      if not (0 <= start_idx < num_landmarks and 0 <= end_idx < num_landmarks):
        raise ValueError(f'Landmark index is out of range. Invalid connection '
                         f'from landmark #{start_idx} to landmark #{end_idx}.')
      if start_idx in idx_to_coordinates and end_idx in idx_to_coordinates:
        drawing_spec = connection_drawing_spec[connection] if isinstance(
            connection_drawing_spec, Mapping) else connection_drawing_spec
        cv2.line(image, idx_to_coordinates[start_idx],
                 idx_to_coordinates[end_idx], drawing_spec.color,
                 drawing_spec.thickness)
  # Draws landmark points after finishing the connection lines, which is
  # aesthetically better.
  if landmark_drawing_spec:
    for idx, landmark_px in idx_to_coordinates.items():
      drawing_spec = landmark_drawing_spec[idx] if isinstance(
          landmark_drawing_spec, Mapping) else landmark_drawing_spec
      # White circle border
      circle_border_radius = max(drawing_spec.circle_radius + 1,
                                 int(drawing_spec.circle_radius * 1.2))
      