Salary Prediction Web Application

This project is a simple machine learning web application that predicts an individual's salary based on their years of experience. It uses a linear regression model built with scikit-learn and a web interface powered by Flask.

Features
- Input form to submit years of experience
- Predicts salary based on trained ML model
- Real-time result displayed on the same page

Tech Stack
- Backend: Flask (Python)
- Frontend: HTML5, CSS3
- ML Model: Scikit-learn (Linear Regression)

File Structure
Salary-Prediction-Web-App/
├── app.py                  - Main Flask application
├── model.pkl               - Trained ML model (pickled)
├── templates/
│   └── index.html          - Main HTML UI
├── static/
│   └── css/
│       └── style.css       - Custom styles (if any)
├── README.md               - Project documentation

Setup Instructions
1. Clone the repository
   git clone https://github.com/yourusername/Salary-Prediction-Web-App.git
   cd Salary-Prediction-Web-App

2. Create a virtual environment and activate it
   python -m venv venv
   venv\Scripts\activate  (On Windows)
   source venv/bin/activate  (On Mac/Linux)

3. Install required dependencies
   pip install -r requirements.txt

4. Run the application
   python app.py

5. Open in browser
   Visit: http://127.0.0.1:5000

Screenshots
(Place an image in static folder named screenshot.png)

Model Info
- Trained using a dataset containing YearsExperience and Salary
- Simple Linear Regression was used for prediction

Note
Make sure the model.pkl file is generated and placed in the root directory. If not, re-run the training script to generate it.

