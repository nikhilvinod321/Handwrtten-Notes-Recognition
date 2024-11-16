# Handwritten Digit and Text Recognition

This project allows for recognizing handwritten digits and text from images using a pre-trained MNIST model for digit recognition and EasyOCR for text recognition.

## Requirements

To run this project, you need the following dependencies:

1. **Python** (version 3.6 or later)
2. **TensorFlow** (for digit recognition using the MNIST model)
3. **OpenCV** (for image preprocessing)
4. **EasyOCR** (for text recognition)

### Install Required Libraries

You can install all the required libraries using the following command:

```bash
pip install tensorflow opencv-python easyocr
```

## Steps for Running the Project

1. **Train the MNIST Model** (only if you haven't done this already):
   - Ensure you have the script `train_mnist_model.py` that trains the MNIST model and saves it as `mnist_model.h5`.
   - If you haven't already trained the model, you can run the following command to do so:

     ```bash
     python train_mnist_model.py
     ```

   - This will save the trained model as `mnist_model.h5` in the same directory.

2. **Run the Main Script**:
   - To run the project, execute the `main.py` script by running:

     ```bash
     python main.py
     ```

   - You will be prompted to choose between **Digit Recognition** or **Text Recognition**:
     - **1** for Digit Recognition: You will be asked to provide the path to an image containing a handwritten digit.
     - **2** for Text Recognition: You will be asked to provide the path to an image containing handwritten or printed text.

3. **Input Image**:
   - When prompted, provide the path to an image (e.g., `handwritten_digit.jpg`) containing the handwritten digits or text you want to recognize.
   - The program will process the image and display the recognized result:
     - If you chose **1**, it will display the predicted digit.
     - If you chose **2**, it will display the recognized text.


## Example

```bash
Choose an option:
1. Digit Recognition
2. Text Recognition
Enter your choice (1/2): 1
Enter the path of the image: handwritten_digit.jpg
Predicted Digit: 1

