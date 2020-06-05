import streamlit as st

from PIL import Image
titleimage=Image.open('type.jpg')
st.image(image=titleimage)
st.title("Tell us about your patient")
st.header("(These features are correlated with A1C score)")

st.header("Blood work")
st.subheader("Triglycerides (mg/dl)")
a=st.number_input('40-500',key='a')
st.subheader("HDL cholesterol (mg/dl)")
b=st.number_input('20-125',key='b')
st.subheader("Total cholesterol (mg/dl)")
c=st.number_input('75-370',key='c')
st.subheader("Platelet count (1000 cells/ul)")
d=st.number_input('50-600',key='d')
st.subheader("White blood cell count (1000 cells/ul)")
e=st.number_input('3.0-18.0',key='e')
st.subheader("Red blood cell count (million cells/ul)")
f2=st.number_input('2.9-6.8',key='f2')

st.header("Appointment measurements")
st.subheader("60 second pulse")
g=st.number_input('40-150',key='g')
st.subheader("Systolic BP (mm/hg)")
h=st.number_input('80-200',key='h')
st.subheader("Diastolic BP (mm/hg)")
i=st.number_input('35-120',key='i')

st.header("Appointment questions")
st.subheader("Current age (years)")
j=st.number_input('18-120',key='j')
st.subheader("Age of onset of diabetes (years)")
k=st.number_input('16-120',key='k')

import pandas as pd
import numpy as np


X_diabetes=pd.read_csv('X_diabetes.csv',index_col=[0])
to_add=[[a,b,c,d,e,f2,g,h,i,j,k]]
X_diabetes2=X_diabetes.append(pd.DataFrame(to_add,columns=['triglycerides_mg_dl','HDL_cholesterol_mg_dl','total_cholesterol_mg_dl','platelet_count_1000cells_ul','white_blood_cell_count_1000cells_ul','red_blood_cell_count_millioncells_ul','60secpulse','systolic_mm_hg','diastolic_mm_hg','age_yr','age_onset_diabetes']),ignore_index=True)

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
X_normalized=StandardScaler().fit_transform(X_diabetes2)
kmeans = KMeans(n_clusters = 3, random_state = 0)
kmeans.fit(X_normalized)

cluster_map=pd.DataFrame()
cluster_map['data_index']=X_diabetes2.index.values
cluster_map['cluster']=kmeans.labels_

from PIL import Image
cluster1image=Image.open('cluster1.png')
cluster2image=Image.open('cluster2.png')
cluster3image=Image.open('cluster3.png')


if st.button('Find treatments!'):
	if cluster_map.loc[cluster_map.index[-1], 'cluster'] == 0:
    		st.image(image=cluster1image)
	elif cluster_map.loc[cluster_map.index[-1], 'cluster'] == 1:
    		st.image(image=cluster2image)
	else:
    		st.image(image=cluster3image)
