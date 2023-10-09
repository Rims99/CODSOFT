import streamlit as st
import cv2
import numpy as np

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Streamlit app title and description
st.title("Face Detection App")
st.write("This app detects faces in images.")

# Function to detect faces in an image
def detect_faces(image):
    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    return faces

# Streamlit main function
def main():
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_image is not None:
        # Read the uploaded image
        image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)
        
        # Detect faces in the image
        faces = detect_faces(image)
        
        # Display the image with detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
        st.image(image, channels="BGR", caption="Faces Detected", use_column_width=True)
        st.write(f"Number of faces detected: {len(faces)}")

if __name__ == "__main__":
    main()
