from openai import OpenAI
import streamlit as st
import openai
from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings

openai.api_key = st.secrets["OPENAI_API_KEY"]

class llamaIndexService:

    def __init__(self):
        self.index = self.load_data()

    def get_index(self):
        return self.index
    
    def get_chat_engine(self):
        return self.index.as_chat_engine()
        
    def load_data(self):
     reader = SimpleDirectoryReader(input_dir="src/data", recursive=True)
     docs = reader.load_data()
     Settings.llm = OpenAI(
        api_key=openai.api_key,
        model="gpt-4o-mini",
        temperature=0.2,
        system_prompt="""You are BananaBot, a helpful assistant that is going to help new developers to get started with the AIAIAI team.
        Assume that all questions are related to the team AIAIAI, ramp up process, project setup, how to start contributing to the team, etc . 
        Keep your answers technical and based on facts – do not hallucinate features.""",
      )
     index = VectorStoreIndex.from_documents(docs)
     return index
    
    



