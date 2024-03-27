from dotenv import load_dotenv
import os
import pandas as pd
import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI


load_dotenv()
api_key=os.getenv('OPENAI_API_KEY')





model=ChatOpenAI(model='gpt-4',)


st.title('Ask questions about uploaded csv files')
if "file_uploader_key" not in st.session_state:
    st.session_state["file_uploader_key"] = 0

if "uploaded_files" not in st.session_state:
    st.session_state["uploaded_files"] = []

files = st.file_uploader(
    "Upload csv files",
    accept_multiple_files=True,
    key=st.session_state["file_uploader_key"],
)

if files:
    st.session_state["uploaded_files"] = files
    lst=[]

    for file in files:
        df=pd.read_csv(file)
        lst.append(df)
        
    agent=create_pandas_dataframe_agent(model,lst,verbose=False)

if st.button("Clear uploaded files"):
    st.session_state["file_uploader_key"] += 1
    st.experimental_rerun()



if 'last_question' not in st.session_state:
    st.session_state.last_question=''
    
if 'show_response' not in st.session_state:
    st.session_state.show_response=False

user_input=st.text_input('Ask your question',value='',key='user-query')
submit_button=st.button('Ask')

if submit_button:
    st.session_state.last_question=user_input
    st.session_state.show_response=True
    if user_input.lower()!='quit':
        response=agent.run(user_input)
        st.session_state.response=response
        
    else:
        st.stop()
        
st.header('Respose',divider='rainbow')

if st.session_state.show_response:
    st.markdown(f'<p style="background-color:lightblue; padding: 8px 8px; border-radius: 5px;">Question: {st.session_state.last_question}</p>', unsafe_allow_html=True)
    st.write(f"Answer: {st.session_state.response}")
    st.session_state.show_response = False  




'''
This is a web based AI chatbot that is built using streamlit and langchain that answer any questions relevant to the data that we provided
Here we are using OpenAI as LLM and gpt-4 model
The data to be provided needs to be in csv format only and we can pass any no. of csv files whether relevant to each other or not and model learns it
We can also Clear all the files that we have passed in which case model completely learns the new files that we will pass
With streamlit i have made a web interface that allows one to upload multiple files, to clear all the files uploaded, to ask the question and display the responce 
With langchain I have made a agent using create_pandas_dataframe_agent which takes in our dataframe and the openai model and generate responce based on the asked question
'''