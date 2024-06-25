import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('D:/PRANAMI/Projects/Attrition data/trained_model.sav', 'rb'))
loader_encoders = pickle.load(open('D:/PRANAMI/Projects/Attrition data/label_encoders.pkl', 'rb'))

# creating a function for Prediction
def attrition_prediction(input_data):
    #change the inputdata to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array for one instance
    input_data_reshape = input_data_as_numpy_array.reshape(1, -1)

    # Make prediction
    prediction = loaded_model.predict(input_data_reshape)

    # Output the prediction
    if prediction[0] == 0:
        return "The employee will not attrite."
    else:
        return "The employee will attrite."
    
def main():
    #Giving a title 
    st.title('Attrition Prediction for XYZ company')
    
    #getting the input data from the user
    Age	= st.number_input("Age of a employee : ")
    
    map1 = {
        'Non-Travel': 0,
        'Travel_Frequently': 1,
        'Travel_Rarely': 2}
    BusinessTravel	= st.selectbox("Business Travel", list(map1.keys()))
    BusinessTravel_encoded = map1[BusinessTravel]                              
    
    map2 = {
        'Human Resources':0,
        'Research & Development':1,
        'Sales':2}
    Department	= st.selectbox("Department", list(map2.keys()))
    Department_encoded = map2[Department]
	
    map3 = {
        'Belo College':1,
        'College':2,
        'Bachlor':3,
        'Master':4,
        'Doctor':5}
    Education = st.selectbox("Eduction", list(map3.keys()))
    Eduction_encoded = map3[Education]
    
    map4 = {
        'Technical Degree':0,
        'Life Sciences':1,
        'Marketing':2,
        'Medical':3,
        'Other':4,
        'Human Resources':5}
    EducationField	= st.selectbox("EducationField", list(map4.keys()))
    EducationField_encoded = map4[EducationField]
    	
    map5 = {
       'Female':0,
       'Male':1}
    Gender = st.selectbox('Gender',list(map5.keys()))
    Gender_encoded = map5[Gender]
     
    map6 = {
        'Healthcare Representative':0,
        'Human Resources':1,
        'Laboratory Technician':2,
        'Manager':3,
        'Manufacturing Director':4,
        'Research Director':5,
        'Research Scientist':6,
        'Sales Executive':7,
        'Sales Representative':8}
    JobRole = st.selectbox("Job role",list(map6.keys()))
    JobRole_encoded = map6[JobRole]
    
    map7 = {
        'Divorced':0,
        'Married':1,
        'Single':2}
    MaritalStatus = st.selectbox("MaritalStatus ", list(map7.keys()))
    MaritalStatus_encoded = map7[MaritalStatus]	
    
    MonthlyIncome	= st.text_input('Monthly income')
    
    NumCompaniesWorked = st.text_input('Number of Companies worked')
    
    PercentSalaryHike	= st.text_input('Percent Salary Hike')
    
    
    TotalWorkingYears = st.number_input('Total Working Years')
	
    TrainingTimesLastYear = st.number_input('Training Times LastYear')	
    
    YearsAtCompany	= st.number_input('Years at company')
    
    YearsSinceLastPromotion	 = st.number_input('Years Since Last Promotion')

    YearsWithCurrManager = st.number_input('Years With Current Manager')
    
    WorkLifeBalance	= st.number_input('Balance with work life', max_value=4)
    
    JobInvolvement	= st.number_input('Job Involvement', max_value=4)
    
    JobLevel = st.slider("Job Level",min_value=1, max_value=5, value=3)	
    
    DistanceFromHome = st.slider("Distance from the home : ", min_value=0, max_value=50, value=20)
    
    StockOptionLevel = st.slider('Stock Option Level',min_value=0, max_value=3, value=2)
    
    EnvironmentSatisfaction	= st.slider('Environment Satisfaction', min_value=1, max_value=4, value=2)
    
    JobSatisfaction	= st.slider('Job Satisfaction', min_value=1, max_value=4, value=2)
    
    PerformanceRating = st.slider('Performance Rating', min_value=0, max_value=5, value=2)
    
    input_data = [Age,BusinessTravel_encoded,Department_encoded,DistanceFromHome,
                  Eduction_encoded,EducationField_encoded,Gender_encoded,JobLevel,
                  JobRole_encoded,MaritalStatus_encoded,MonthlyIncome,NumCompaniesWorked,
                  PercentSalaryHike,StockOptionLevel,TotalWorkingYears,TrainingTimesLastYear,
                  YearsAtCompany,YearsSinceLastPromotion,YearsWithCurrManager,EnvironmentSatisfaction,
                  JobSatisfaction,WorkLifeBalance,JobInvolvement,PerformanceRating]
    
    result = ''
    if st.button('Predict'):
        result = attrition_prediction(input_data)
    
    st.success(result)
    

if __name__ == '__main__':
    main()
        