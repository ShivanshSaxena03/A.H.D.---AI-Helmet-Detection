# A.H.D.---AI-Helmet-Detection
AHD (Advanced Helmet Detection) is a Python-based image classification tool that sorts images into 'HELMET' and 'NO_HELMET' folders using brightness analysis. Includes personalized greetings, logs, and summary image output for each run.


🛡️ AHD – Advanced Helmet Detection System
AHD is a Python-based image classification utility designed to simulate helmet detection using basic image brightness. It reads a dataset of images, classifies them into HELMET and NO_HELMET folders, and generates visual logs for user-friendly feedback.

🚀 Features:
✨ Personalized greeting image with timestamp

📁 Batch image loading from a dataset folder

💡 Dummy classification based on image brightness

🗂️ Auto-sorting into HELMET and NO_HELMET folders

📸 Summary image generation at the end of the run

🧾 Clean console logs for each image processed


HOW TO RUN: 
1. Install Dependencies:

  pip install opencv-python numpy

2. Directory Structure:
   YOUR_BASE_PATH/
├── DATASET/           # Folder with input images
├── HELMET/            # Will be auto-created for classified helmet images
├── NO_HELMET/         # Will be auto-created for classified no-helmet images
└── main.py

3. Run the Script:
   python main.py

4. User Input: You'll be prompted to enter the aspirant’s name via keyboard.

5. Output:
  output_greeting.png → shows the start of the process

  output_summary.png → summarises the result

  Sorted images go into HELMET/ and NO_HELMET/ folders
