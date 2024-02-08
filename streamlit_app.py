import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


st.header('IRIS FLOWER DAHSBOARD',divider='rainbow')
st.sidebar.title('Description')
st.sidebar.write('''The Iris dataset is a popular dataset in m
                 achine learning and statistics. It is often used for educational purposes and
                  serves as a standard reference dataset for testing classification algorithms. 
                 The dataset consists of 150 samples of iris flowers, each belonging to one of three species:
                  Setosa, Versicolor, and Virginica. Each sample contains four features:
                 -Sepal length (in cm)
                 -Sepal length (in cm)
                 -Petal length (in cm)
                 -Petal width (in cm)''')
df = pd.read_csv('C:/Users/User11/Desktop/Deployment/myenv/Data/iris.csv')
col1,col2=st.columns(2)
with col1:
    class_data= df['class'].values_counts()
    fig,ax = plt.subplots()
    ax.pie(class_data,labels=['setosa','versicolor','virginica'])
    st.pyplot(fig)