import face_recognition
import cv2

image = face_recognition.load_image_file("download.jpg")
face_locations = face_recognition.face_locations(image)
#face_landmarks_list = face_recognition.face_landmarks(image)
edit_image = image[:, :, [2, 1, 0]]
cv2.imshow("Output", edit_image)
