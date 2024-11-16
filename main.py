import cv2
import numpy as np
from tensorflow.keras.models import load_model
import easyocr

model = load_model('mnist_model.h5')

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28))
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)
    return img

def predict_digit(image_path):
    processed_img = preprocess_image(image_path)
    prediction = model.predict(processed_img)
    return np.argmax(prediction)

def recognize_text(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    text = [item[1] for item in result]
    return text

def main():
    print("Choose an option:")
    print("1. Digit Recognition")
    print("2. Text Recognition")
    choice = input("Enter your choice (1/2): ")

    image_path = input("Enter the path of the image: ")

    if choice == '1':
        digit = predict_digit(image_path)
        print(f"Predicted Digit: {digit}")
    elif choice == '2':
        text = recognize_text(image_path)
        print("Recognized Text:", text)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
