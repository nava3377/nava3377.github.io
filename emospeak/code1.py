import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog

# Constants
TRAIN_IMAGE_DIRS = ["train_images\\500", "train_images\\2000"]
TRAIN_OUTPUT_DIR = "train"
TEST_OUTPUT_DIR1 = "test\\ids1"
TEST_OUTPUT_DIR2 = "test\\ids2"
IMAGE_SIZE = (1200, 512)

# Function to process images
def process_image(img, output_dir, k):
    # Resizing
    img = cv2.resize(img, IMAGE_SIZE, interpolation=cv2.INTER_LINEAR)

    # Denoising image
    img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

    # Converting to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Compute the median of the single channel pixel intensities
    v = np.median(img_gray)
    sigma = 0.33

    # Apply automatic Canny edge detection using the computed median
    lower = int(max([0, (1.0 - sigma) * v]))
    upper = int(min([255, (1.0 + sigma) * v]))
    img_canny = cv2.Canny(img_gray, lower, upper)

    # Extracting features
    id1 = img_canny[195:195 + 170, 190:190 + 85]
    id2 = img_canny[330:330 + 105, 720:720 + 105]
    id3 = img_canny[320:320 + 90, 865:865 + 205]
    id4 = img_canny[250:250 + 40, 1120:1120 + 40]
    id5 = img_canny[5:5 + 405, 660:660 + 40]
    id6 = img_canny[284:284 + 132, 1090:1090 + 90]

    ids = [id1, id2, id3, id4, id5, id6]

    for d, i in enumerate(ids, 1):
        output_path = os.path.join(output_dir, f"id{d}_{k}.jpg")
        cv2.imwrite(output_path, i)

# Extracting features from training images
def trainproc():
    k = 0
    for train_dir in TRAIN_IMAGE_DIRS:
        train_imgs = [os.path.join(train_dir, filename) for filename in os.listdir(train_dir) if filename.endswith('.jpg')]

        out = os.path.join(TRAIN_OUTPUT_DIR, os.path.basename(train_dir))

        for tr in train_imgs:
            img = cv2.imread(tr)
            process_image(img, out, k)
            k += 1

ids1 = []
ids2 = []
def testproc():
    root = tk.Tk()
    pth = tk.filedialog.askopenfilename()
    root.destroy()

    img = cv2.imread(pth)
    process_image(img, TEST_OUTPUT_DIR1, 1)
    process_image(img, TEST_OUTPUT_DIR2, 2)

    # Displaying the features
    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(ids1[i])  # Make sure to define ids1
        plt.xticks([])
        plt.yticks([])
    plt.show()

    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(ids2[i])  # Make sure to define ids2
        plt.xticks([])
        plt.yticks([])
    plt.show()

# Main procedure
while True:
    x = input("Enter 0 to start extracting features from training images or 1 for testing the image\n")
    if x == '0':
        trainproc()
        print("Features extracted!")
        os.system("perform-training.py")
        break
    elif x == '1':
        testproc()
        print("Features extracted!")
        os.system("perform-testing.py")
        break
    elif x == 'exit':
        print("Exited!")
        break
    else:
        print("Enter correct key")
        continue
