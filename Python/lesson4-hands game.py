from tracemalloc import start
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # print(image.shape)
    image_height, image_width, _ = image.shape
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        print(hand_landmarks)
        
# ================================== Указательный палец

        center_coordinates = (
            int(hand_landmarks.landmark[8].x * image_width), 
            int(hand_landmarks.landmark[8].y * image_height)
        )
        radius = 20
        color = (255, 0, 0)
        thickness = 2
        image = cv2.circle(image, center_coordinates, radius, color, thickness)

# ================================== Прямоугольник справа

        center_coordinates = (
            int(hand_landmarks.landmark[8].x * image_width),
            int(hand_landmarks.landmark[8].y * image_height)
        )
        start_point = (1, 200)
        end_point = (10, 300)
        color = (255, 0, 0)
        thickness = 2
        #image = cv2.rectangle(image, center_coordinates, radius, color, thickness)
        #image = cv2.rectangle(image, start_point, end_point, color, thickness)
        image2 = cv2.rectangle(image, center_coordinates, end_point, color, thickness)

# ==================================

        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())


    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()