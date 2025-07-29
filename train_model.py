# train_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# 1. Load the dataset
data = pd.read_csv('salary_data.csv')  # Make sure the file is in same folder

# 2. Split into input and output
X = data[['YearsExperience']]  # must be 2D
y = data['Salary']

# 3. Train the model
model = LinearRegression()
model.fit(X, y)

# 4. Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
