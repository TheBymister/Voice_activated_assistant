import face_recognition
import pickle
import os
import re

i = 0
all_face_encodings = {}
for filename in os.listdir(".\\Dataset\\"):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        i = face_recognition.load_image_file(".\\Dataset\\"+filename)
        query = filename
        stopwords = {'.jpg,.png'}
        resultwords  = [word for word in re.split("\W+",query) if word.lower() not in stopwords]
        comm = ' '.join(resultwords)
        all_face_encodings[comm] = face_recognition.face_encodings(i)[0]
        i = i+1

with open('dataset_faces.dat', 'wb') as f:
    pickle.dump(all_face_encodings, f)

print("Finished...")
input("Press any key to quit")
