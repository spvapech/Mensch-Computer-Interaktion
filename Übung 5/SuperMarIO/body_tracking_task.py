import cv2
import mediapipe as mp
from custom_input_task import custom_input_loop
from game_files.Anonymization import displayAnonymization

showBodyMarkers = True
showAnonymization = False

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = None
playerFrame = None


def custom_input_thread(stop_event):
    global pose
    pose = mp_pose.Pose(model_complexity=1,
                        enable_segmentation=False,
                        smooth_landmarks=True)

    cap = cv2.VideoCapture(0)  # Für Windows ggf. cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("❌ Keine Webcam gefunden")
        return

    try:
        while not stop_event.is_set():
            ok, frame = cap.read()
            if not ok:
                continue

            frame, markerList = getMarkerListAndShowMarkers(frame, showBodyMarkers)

            custom_input_loop(markerList)

            displayWebcam(frame, markerList)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


def getMarkerListAndShowMarkers(frame, showBodyMarkers):
    global pose

    if pose is None:
        return frame, None

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = pose.process(img_rgb)
    markerList = res.pose_landmarks  # kann None sein

    if showBodyMarkers and markerList is not None:
        mp_drawing.draw_landmarks(
            frame,
            markerList,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing.DrawingSpec(thickness=2, circle_radius=2),
            connection_drawing_spec=mp_drawing.DrawingSpec(thickness=2),
        )

    return frame, markerList


def displayWebcam(frame, markerList):
    global playerFrame

    if showAnonymization:
        frame = displayAnonymization(frame, markerList)

    mirrored_frame = cv2.flip(frame, 1)
    mirrored_frame = cv2.resize(mirrored_frame, (280, 213))
    mirrored_frame = cv2.cvtColor(mirrored_frame, cv2.COLOR_BGR2RGB)
    playerFrame = mirrored_frame


def getPlayerFrame():
    return playerFrame
