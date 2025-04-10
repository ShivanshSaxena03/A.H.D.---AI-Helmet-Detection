import os
import cv2
import numpy as np
from datetime import datetime

# --- Ask for Aspirant's Name ---
name = input("Enter the name of aspirant from keyboard: ")

# --- Initial Greeting Image ---
greeting_img = np.zeros((200, 1500, 3), dtype="uint8")
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(greeting_img, f"Hi {name}  Helmet_Detection_Project", (50, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(greeting_img, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), (50, 150), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imwrite("output_greeting.png", greeting_img)
print("Greeting image saved as 'output_greeting.png'")

# --- Paths ---
base_path = 'D:\\Personal Projects\\HELMET DETECTION SYSTEM\\DRAFT 1_ FINAL'
dataset_path = os.path.join(base_path, 'DATASET')
helmet_path = os.path.join(base_path, 'HELMET')
no_helmet_path = os.path.join(base_path, 'NO_HELMET')

# Create output folders if not exist
os.makedirs(helmet_path, exist_ok=True)
os.makedirs(no_helmet_path, exist_ok=True)

# --- Load Images ---
def load_images_from_folder(folder_path):
    image_list = []
    image_names = []
    if not os.path.exists(folder_path):
        print(f"❌ Dataset folder not found: {folder_path}")
        return image_list, image_names

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)
            if image is not None:
                image_list.append(image)
                image_names.append(filename)
    return image_list, image_names

# --- Load Dataset ---
images, image_names = load_images_from_folder(dataset_path)
print(f"\nTotal Images Found: {len(images)}\n")

# --- Dummy Classification (based on brightness) ---
for idx, (image, image_name) in enumerate(zip(images, image_names), 1):
    print(f"[{idx}/{len(images)}] Processing: {image_name}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)
    print(f"    Brightness Level: {brightness:.2f}")
    
    filename_wo_ext = os.path.splitext(image_name)[0]
    output_path = helmet_path if brightness > 100 else no_helmet_path
    status = "✅ Helmet Detected" if brightness > 100 else "❌ No Helmet Detected"
    print(f"    {status}")
    
    cv2.imwrite(os.path.join(output_path, filename_wo_ext + ".png"), image)

# --- Final Summary Image ---
summary_img = np.zeros((400, 2000, 3), dtype="uint8")
cv2.putText(summary_img, f"{name}, Helmet Detection is completed.", (50, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(summary_img, "Please visit HELMET and NO_HELMET folders", (50, 150), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(summary_img, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), (50, 200), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imwrite("output_summary.png", summary_img)
print("Result summary image saved as 'output_summary.png'")
