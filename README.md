Employee Salary Predictor
A web-based machine learning application that predicts an employee's salary based on their years of experience.
Built from scratch using Python, Flask, and scikit-learn, with a clean and responsive user interface.

Overview
This project demonstrates a practical application of simple linear regression using real-world salary data.
Users can enter the number of years of experience, and the application predicts the corresponding salary in ₹ Lakhs.

Features
Takes input: Years of Experience

Predicts salary using a trained ML model

Real-time output via a Flask web app

Minimal and professional dark-themed UI

Tech Stack
Frontend: HTML5, CSS3
Backend: Flask (Python)
ML Model: scikit-learn (Linear Regression)
Optional Deployment: Render / Vercel

Project Structure
Employee-Salary-Predictor
│
├── app.py → Main Flask application
├── model.py → Model training script
├── model.pkl → Trained Linear Regression model
├── templates/ → Contains HTML file
│ └── index.html → UI page for prediction
├── static/ → CSS styling
│ └── css/style.css
├── Salary_Data.csv → Sample dataset
├── requirements.txt → List of Python packages
└── README.md → Project documentation

How to Run Locally
Clone the Repository

git clone https://github.com/KomalHiremath/Employee-Salary-Predictor.git
cd Employee-Salary-Predictor

Create Virtual Environment

python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on Mac/Linux)

Install Required Packages

pip install -r requirements.txt

Run the Flask App

python app.py

Now open your browser and go to: http://127.0.0.1:5000

Preview Screenshot
(Optional) You can place a screenshot named screenshot.png inside the static folder.

Model Info
Input: Years of Experience

Output: Predicted Salary in ₹ Lakhs

Algorithm: Simple Linear Regression

Trained on CSV-based sample dataset
