import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

# cargar imágenes y etiquetas


def load_images_and_labels(data_path, size=(100, 100)):
    images = []
    labels = []
    labels_dic = {}
    cur_label = 0

    for subdir, dirs, files in os.walk(data_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                path = os.path.join(subdir, file)
                label = os.path.basename(subdir)
                if label not in labels_dic:
                    labels_dic[label] = cur_label
                    cur_label += 1
                image = cv2.imread(path)
                image = cv2.resize(image, size, interpolation=cv2.INTER_CUBIC)
                images.append(image)
                labels.append(labels_dic[label])

    return np.array(images), np.array(labels), labels_dic


data_path = "path/to/your/dataset"
images, labels, labels_dic = load_images_and_labels(data_path)

# entrenar modelo
face_cascade = cv2.CascadeClassifier(
    "path/to/haarcascade_frontalface_default.xml")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(images, labels)

# probar el modelo


def predict(face_recognizer, image, cascade, size=(100, 100)):
    faces = cascade.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    if (len(faces) == 0):
        return None, None
    (x, y, w, h) = faces[0]
    face = image[y:y+h, x:x+w]
    face = cv2.resize(face, size, interpolation=cv2.INTER_CUBIC)
    label, confidence = face_recognizer.predict(face)
    return label, confidence


# test the model on a few images
test_path = "path/to/your/test_images"
for subdir, dirs, files in os.walk(test_path):
    for file in files:
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            path = os.path.join(subdir, file)
            image = cv2.imread(path)
            label, confidence = predict(face_recognizer, image, face_cascade)
            if label is not None:
