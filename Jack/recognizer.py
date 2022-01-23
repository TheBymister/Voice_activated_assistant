import face_recognition
import pickle
import numpy as np
import time
import os


print("Loading dataset_faces")
# Load face encodings
with open('dataset_faces.dat', 'rb') as f:
	all_face_encodings = pickle.load(f)

# Grab the list of names and the list of encodings
face_names = list(all_face_encodings.keys())
face_encodings = np.array(list(all_face_encodings.values()))

# Try comparing an unknown image
while True:
    print()
    print("Available test images")
    for filename in os.listdir():
        if filename.endswith(".jpg") or filename.endswith(".png"):
            print(filename)

    print()
    print("Please add the file extension e.g. (filename).jpg or (filename).png")
    FaceTest = input("Enter the name of the file to be scanned: ")
    print("Finding face...")
    tic = time.perf_counter()
    try:
        unknown_image = face_recognition.load_image_file(FaceTest)
        unknown_face = face_recognition.face_encodings(unknown_image)
        result = face_recognition.compare_faces(face_encodings, unknown_face)
    except:
        print("No file found")

    names_with_result = list(zip(face_names, result))
    length = len(names_with_result)
    for i in range(length):
        if True in names_with_result[i]:
            print(names_with_result[i])
            break
        else:
            pass
    toc = time.perf_counter()
    stop1 = toc - tic
    print(stop1)
    Quit = input("Do you wish to exit?  Y or N: ")
    if Quit == "Y" or "y":
        break
    else:
        continue
    
input("Press any button to exit: ")
