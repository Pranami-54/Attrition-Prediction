import numpy as np
import pickle

#loading the saved model
loaded_model = pickle.load(open('D:/PRANAMI/Projects/Attrition data/trained_model.sav', 'rb'))

#input data
input_data = (37, 2, 1, 29, 4, 5, 0, 1, 2, 1, 78800, 3.0, 12, 1, 9.0, 2, 4, 0, 2, 3.0, 3.0, 2.0, 4, 3)

#change the inputdata to numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshape the array for one instance
input_data_reshape = input_data_as_numpy_array.reshape(1, -1)

# Make prediction
prediction = loaded_model.predict(input_data_reshape)

# Output the prediction
if prediction[0] == 0:
    print("The employee will not attrite.")
else:
    print("The employee will attrite.")