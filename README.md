# Brain Tumor Detection System
The Brain Tumor Detection System is a web-based application that leverages deep learning to analyze MRI scans and detect brain tumors. The system provides users with accurate tumor classifications, confidence levels, and treatment recommendations, assisting medical professionals in diagnosis and decision-making.
## Features
* Deep Learning-Based Detection: Uses a trained model to identify tumor presence and type (e.g., Glioma, Meningioma, Pituitary Tumor, or No Tumor).

* Detailed Predictions: Displays tumor confidence level and medical insights.

* Treatment Recommendations: Provides information about possible treatment approaches, medications, and follow-up schedules.

* User Authentication: Secure login system for doctors and patients.

* Patient Management Dashboard: Allows doctors to manage patient records efficiently.

* Interactive Visualizations: Displays statistical insights through charts.

## Prerequisites
* Python 3.x
* Virtual Environment(optional)

## Technologies Used
* Front-end: HTML, CSS, JavaScript
* Back-end: Flask (Python), SQLite(Database)
* Machine Learning: TensorFlow/Keras for deep learning model
* Deployment: Flask framework with integrated model

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/abhay41/Brain-Tumor-Detection.git
   cd Brain-Tumor-Detection
      
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
This project requires configuring email functionality to work correctly. In the `apps` folder, specifically within the `operations.py` file on lines **24** and **25**, you must replace the placeholder values with your own **Google email** and **Google App Password**.

## Instructions for Email Setup
### 1. Locate the File to Edit
Open the operations.py file located in the apps folder.
Navigate to lines 24 and 25, where the placeholders for EMAIL and PASSWORD are defined.
### 2. Replace Placeholders
Replace the EMAIL placeholder with your Google email address.
Replace the PASSWORD placeholder with your Google App Password.
