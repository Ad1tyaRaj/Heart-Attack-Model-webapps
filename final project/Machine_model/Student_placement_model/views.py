from sklearn.tree import DecisionTreeClassifier
DecisionTreeClassifier.monotonic_cst = None

from django.shortcuts import render
import pickle
import numpy as np

# Load the trained model
model_path = 'Model/Student_placement.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)


def Student_placement(request):
    prediction_text = ""
    if request.method == 'POST':
        try:
            # Extract features from the form
            Name = (request.POST['Name'])
            CGPA = float(request.POST['CGPA'])
            Resume_Score = float(request.POST['Resume Score'])

            # Prepare the data for prediction
            final_features = [np.array([CGPA, Resume_Score])]

            # Make prediction
            prediction = model.predict(final_features)
            prediction_text = 'Placed' if prediction[0] == 1 else 'Not Placed'

        except KeyError as e:
            prediction_text = f"Error: Missing field {str(e)}"
        except Exception as e:
            prediction_text = f"An error occurred: {str(e)}"

    return render(request, 'Student_placement_model/Student_prediction.html', {'result': prediction_text})
