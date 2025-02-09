from django.shortcuts import render
import pickle
import numpy as np
import pandas as pd

# Load the trained model
model_path = 'Model/Heart_Attack_70.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

def Heart_Attack(request):
    global Report
    result = None  # Default value for prediction result

    if request.method == 'POST':
        try:
            # Get input data
            Name = request.POST['Name']
            Age = int(request.POST['Age'])
            Gender = 1 if request.POST['Gender'].lower() == 'male' else 0  # Encode Gender
            BMI = float(request.POST['BMI'])
            Diabetes = 1 if request.POST['Diabetes'].lower() == 'yes' else 0  # Encode Diabetes
            Urban_rural = 1 if request.POST['Urban_rural'].lower() == 'urban' else 0  # Encode Urban/Rural
            Lifestyle = int(request.POST['Lifestyle'])  # Assuming Lifestyle is numeric

            # Prepare input for model
            test_input = np.array([[Age, Gender, BMI, Diabetes, Urban_rural, Lifestyle]])
            test_input = pd.DataFrame(test_input,
                                      columns=['Age', 'Gender', 'BMI', 'Diabetes', 'UrbanOrRural', 'Lifestyle'])

            # Make prediction
            result = model.predict(test_input)[0]  # Extract prediction


        except Exception as e:
            result = f"Error: {str(e)}"  # Handle errors

    return render(request, 'Heart_Attack_model/Heart_Attack.html', {'result': result})
