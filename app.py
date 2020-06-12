import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image
titleimage=Image.open('type.jpg')
green=Image.open('green.png')
amber=Image.open('amber.png')
red=Image.open('red.png')

st.image(image=titleimage)
st.title("Helping physicians find the best treatment for patients with type 2 diabetes")
patient1=pd.read_csv('patient1.csv',index_col=[0])
patient2=pd.read_csv('patient2.csv',index_col=[0])
patient3=pd.read_csv('patient3.csv',index_col=[0])
patient4=pd.read_csv('patient4.csv',index_col=[0])
patient5=pd.read_csv('patient5.csv',index_col=[0])

patient=st.selectbox('Select patient EMR data',('Patient 1','Patient 2','Patient 3'))
dataframe=pd.read_csv('dataframe_jun11_2.csv',index_col=0)
bins=[0,5.7,6.5,np.inf]
names=['green','amber','red']
dataframe['last_A1C_stoplight']=pd.cut(dataframe['last_A1C'],bins,labels=names)

X_rf = dataframe.drop(['SEQN','last_A1C','year','last_A1C_stoplight'],1)  
y_rf = dataframe['last_A1C_stoplight']
from sklearn.model_selection import train_test_split
X_rf_train, X_rf_test, y_rf_train, y_rf_test = train_test_split(X_rf, y_rf, test_size=.25,random_state = 0)

from sklearn.ensemble import RandomForestClassifier
clf_rf = RandomForestClassifier(n_estimators=20,class_weight='balanced',random_state = 0)
clf_rf.fit(X_rf_train, y_rf_train)

if patient=='Patient 1':
	st.write(patient1)
	st.write("This patient's A1C is currently in the red zone")
	st.image(image=red)
if patient=='Patient 2':
	st.write(patient2)
	st.write("This patient's A1C is currently in the red zone")
	st.image(image=red)
if patient=='Patient 3':
	st.write(patient3)
	st.write("This patient's A1C is currently in the red zone")
	st.image(image=red)

if st.button("Find out how certain interventions are predicted to affect this patient's A1C"):
	if patient=='Patient 1':
		st.subheader('Antidiabetic medications')
		st.text('predicted score with insulin: 6.5+') 
		st.text('predicted score with alpha-glucosidase inhibitor: 6.5+')
		st.text('predicted score with biguanide: 6.5+')
		st.text('predicted score with dopamine agonist: 6.5+')
		st.text('predicted score with DPP-4 inhibitor: 6.5+')
		st.text('predicted score with DPP-4 inhibitor; biguanide: 6.5+')
		st.text('predicted score with GLP-1R agonist: 6.5+')
		st.text('predicted score with SGLT2 inhibitor: 6.5+')
		st.text('predicted score with SGLT2 inhibitor; biguanide: 6.5+')
		st.text('predicted score with sulfonylurea: 6.5+')
		st.text('predicted score with thiazolidinedione: 6.5+')
               
		st.subheader('Blood pressure')
		st.text('predicted score with BP of 120/80: 6.5+')
		
		st.subheader('Body mass index')
		st.text('predicted score with BMI of 24: 6.5+')
		
		st.subheader('Diet')
		st.text('predicted score with a diet rated "excellent": 6.5+')
	if patient=='Patient 2':
		st.subheader('Antidiabetic medications')
		st.text('predicted score with insulin: 6.5+')
		st.text('predicted score with alpha-glucosidase inhibitor: 6.5+')
		st.text('predicted score with biguanide: 6.5+')
		st.text('predicted score with dopamine agonist: 6.5+')
		st.text('predicted score with DPP-4 inhibitor: 6.5+')
		st.text('predicted score with DPP-4 inhibitor; biguanide: 6.5+')
		st.text('predicted score with GLP-1R agonist: 6.5+')
		st.text('predicted score with SGLT2 inhibitor: 6.5+')
		st.text('predicted score with SGLT2 inhibitor; biguanide: 6.5+')
		st.text('predicted score with sulfonylurea: 6.5+')
		st.text('predicted score with thiazolidinedione: 6.5+')

		st.subheader('Blood pressure')
		st.text('predicted score with BP of 120/80: 5.7-6.4')

		st.subheader('Body mass index')
		st.text('predicted score with BMI of 24: 6.5+')

		st.subheader('Diet')
		st.text('predicted score with a diet rated "excellent": 6.5+')
	if patient=='Patient 3':
		st.subheader('Antidiabetic medications')
		st.text('predicted score with insulin: 6.5+')
		st.text('predicted score with alpha-glucosidase inhibitor: 6.5+')
		st.text('predicted score with biguanide: 6.5+')
		st.text('predicted score with dopamine agonist: 6.5+')
		st.text('predicted score with DPP-4 inhibitor: 6.5+')
		st.text('predicted score with DPP-4 inhibitor; biguanide: 6.5+')
		st.text('predicted score with GLP-1R agonist: 6.5+')
		st.text('predicted score with SGLT2 inhibitor: 6.5+')
		st.text('predicted score with SGLT2 inhibitor; biguanide: 6.5+')
		st.text('predicted score with sulfonylurea: 6.5+')
		st.text('predicted score with thiazolidinedione: 6.5+')

		st.subheader('Blood pressure')
		st.text('predicted score with BP of 120/80: 6.5+')

		st.subheader('Body mass index')
		st.text('predicted score with BMI of 24: 6.5+')

		st.subheader('Diet')
		st.text('predicted score with a diet rated "excellent": 6.5+')
