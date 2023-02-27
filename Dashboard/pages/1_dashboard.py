import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
import os

#webpage title
st.set_page_config(page_title='student',page_icon=":bar:", layout="wide")
st.header(":red[_World Class Student_] :blue[Data]")

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")



#load gif
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_d5hrx4au.json")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_coding,height=200,key ="Coding")
    with right_column:
        st.write("This data collected from a sample of students enrolled in online sections of Eberly College of Science Statistics department.This data set gives information about campus,work status of students and their Learning status and course completed status.")


##widgets

a1, a2, a3, a4 = st.columns(4)

a1.metric("Learner Status Types"," 2 ")
a2.metric("Work Status Type"," 3 ")
a3.metric("No.of Primary Campus"," 3 ")
a4.metric("Total Online Course completed"," 1846 ")

#Load Data frame
DATA_PATH = os.path.join(dir_of_interest, "data", "WCStudentData.csv")
df = pd.read_csv(DATA_PATH)



#campus selectbox
campus_filter = st.selectbox("Select the Campus",pd.unique(df['Primary Campus']))
placeholder = st.empty()


#Top 10 companys Layoff count


col1,col2, = st.columns(spec=2,gap="medium")
fig_1 = px.histogram(df[df["Primary Campus"]== campus_filter],x="Online Courses Completed",color="Primary Campus")
col1.plotly_chart(fig_1, use_container_width=True)


fig_2 = px.pie(data_frame = df,names="Primary Campus",color = "Primary Campus")
col2.plotly_chart(fig_2, use_container_width=True)

b1,b2 = st.columns(2)

fig_3 = px.bar(df[df["Primary Campus"]== campus_filter],y="Work Status",color="Work Status")
b1.plotly_chart(fig_3, use_container_width=True)


fig_4 = px.bar(df[df["Primary Campus"]== campus_filter],x="Learner Status",color="Learner Status")
b2.plotly_chart(fig_4, use_container_width=True) 

c1,c2 = st.columns(spec=2,gap="medium") 
fig_5 = px.box(df[df["Primary Campus"]== campus_filter],x="Learner Status",y="Online Courses Completed",color="Learner Status")
c1.plotly_chart(fig_5,use_container_width=True)

fig_6 = px.scatter(df[df["Primary Campus"]== campus_filter],x="Work Status",y="Online Courses Completed",color="Work Status")
c2.plotly_chart(fig_6,use_container_width=True)

st.subheader("Dataset")
st.write(df)