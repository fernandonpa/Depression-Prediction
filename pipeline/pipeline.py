import pandas as pd
import sys
from catboost import CatBoostClassifier, Pool

# Paths to saved models
MODEL_PATH_STUDENT = "../models/catboost_model_s.cbm"
MODEL_PATH_WP = "../models/catboost_model_wf.cbm"

# Load the models
model_student = CatBoostClassifier()
model_student.load_model(MODEL_PATH_STUDENT)

model_wp = CatBoostClassifier()
model_wp.load_model(MODEL_PATH_WP)


# Function to make predictions
def predict(input_data):
    df = pd.DataFrame([input_data]).astype(str)

    # Determine category (Student or Working Professional)
    category = df["Working Professional or Student"].iloc[0]

    if category == "Student":
        model = model_student
    elif category == "Working Professional":
        model = model_wp
    else:
        raise ValueError("Invalid category. Must be 'Student' or 'Working Professional'.")

    
    # Make predictions
    prediction = model.predict(df)
    probability = model.predict_proba(df)[:, 1]

    return {
        "prediction": int(prediction[0]),  # 0 = No Depression, 1 = Depression
        "probability": float(probability[0])
    }

# Run from command line
if __name__ == "__main__":
    sample_input = [{
        #"id": 0,
        "Name": "John Doe",
        "Gender": "Male",
        "Age": 26,
        "City": "New York",
        "Working Professional or Student": "Student",
        "Profession": "Engineer",
        "Academic Pressure": 4.0,
        "Work Pressure": None,
        "CGPA": 3.8,
        "Study Satisfaction": 3.0,
        "Job Satisfaction": None,
        "Sleep Duration": "Less than 5 hours",
        "Dietary Habits": "Unhealthy",
        "Degree": "BTech",
        "Have you ever had suicidal thoughts ?": "No",
        "Work/Study Hours": 6,
        "Financial Stress": 3.0,
        "Family History of Mental Illness": "No"
    },
    {'Name': 'praneeth', 
     'Gender': 'Male', 
     'Age': 23.0, 
     'City': 'kuliyapitiya', 
     'Working Professional or Student': 'Working Professional', 
     'Profession': 'Engineer', 
     'Sleep Duration': '7-8 hours', 
     'Dietary Habits': 'Moderate Diet', 
     'Degree': 'Engineering', 
     'Have you ever had suicidal thoughts ?': 'Yes', 
     'Work/Study Hours': 6.0, 
     'Financial Stress': 4.0, 
     'Family History of Mental Illness': 'Yes', 
     'Academic Pressure': None, 
     'Work Pressure': 4.0, 
     'CGPA': None, 
     'Study Satisfaction': None, 
     'Job Satisfaction': 2.0}
    ]

    

    result = predict(sample_input[1])
    print(result)

