from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import base64
from PIL import Image
import os
import pickle
import streamlit as st

## load all the Prompt Templates of the LLM


with open('sys_message.pkl', 'rb') as f1:
    sys_message = pickle.load(f1)
    f1.close()

with open('message.pkl', 'rb') as f2:
    message = pickle.load(f2)
    f2.close()

with open('question_template.pkl', 'rb') as f3:
    question_template = pickle.load(f3)
    f3.close()


load_dotenv()
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')



# initiate LLM model

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Langchain Sequential or extended chain

llm_chain = question_template | llm | StrOutputParser()



def Ai_assistent(encoded_image,user_input):
    sys_message = SystemMessage(content="You are a programming assistant that only answers questions directly related to the code or development ideas or queries visible in the provided screenshot. If the question is about general programming concepts, features, or unrelated code, or is not a development related query, politely decline to answer.  Focus on identifying syntax errors, suggesting improvements")

    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": user_input,
            },
            {"type": "image_url", "image_url": {"url":f"data:image/png;base64,{encoded_image}"}},
        ]
    )

    otp = llm.invoke([sys_message,message])
    print(otp)
    st.write(otp.content)


def encode_uploaded_image(file_path):
    with open(file_path,'rb') as image_file:
        image_content = image_file.read()
        encoded_image = base64.b64encode(image_content).decode('utf-8')
    return encoded_image

def Image_chat_Assistant():
    st.title('Coding Assistent ( AI AGENT )')

    user_input = st.text_input("Your message:")
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:

        upload_folder = "uploaded_images"
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)


        file_path = os.path.join(upload_folder, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

    if st.button("Send"):
        encoded_image = encode_uploaded_image(file_path)
        if user_input:
            Ai_assistent(encoded_image,user_input)
        else:
            st.write("Please enter a Query")


    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")
 






# Load google api form .env file




Image_chat_Assistant()