from openai import OpenAI
import streamlit as st
import openai
from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex, Settings
from llama_index.vector_stores import PGVectorStore


openai.api_key = st.secrets["OPENAI_API_KEY"]
supabase_password = st.secrets["SUPABASE_PASSWORD"]
supabase_user = st.secrets["SUPABASE_USER"]
supabase_host = st.secrets["SUPABASE_HOST"]
supabase_db = st.secrets["SUPABASE_DB"]

class llamaIndexService:

    def __init__(self):
        self.index = self.load_data()

    def get_index(self):
        return self.index

    def get_chat_engine(self):
        return self.index.as_chat_engine()

    def initialize_vector_store(self):
        vector_store = PGVectorStore(
            database=supabase_db,
            host=supabase_host,
            password=supabase_password,
            user=supabase_user,
            port=5432,
            table_name='vectors'
            )
        return vector_store

    def load_data(self):
        vector_store = self.initialize_vector_store()
        Settings.llm = OpenAI(
        api_key=openai.api_key,
        model="gpt-4o-mini",
        temperature=0.2,
        system_prompt="""You are BananaBot, a helpful assistant that is going to help new developers to get started with the AIAIAI team.
        Assume that all questions are related to the team AIAIAI, ramp up process, project setup, how to start contributing to the team, etc .
        Keep your answers technical and based on facts – do not hallucinate features.""",
        )
        index = VectorStoreIndex.from_vector_store(vector_store)
        return index
