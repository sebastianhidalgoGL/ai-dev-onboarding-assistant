from openai import OpenAI
import streamlit as st
import openai
from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex, Settings
from llama_index.vector_stores.postgres import PGVectorStore

openai.api_key = st.secrets["OPENAI_API_KEY"]
SQL_PASSWORD = st.secrets["SQL_PASSWORD"]
SQL_USER = st.secrets["SQL_USER"]
SQL_HOST = st.secrets["SQL_HOST"]
SQL_DB = st.secrets["SQL_DB"]


class llamaIndexService:

    def __init__(self):
        self.index = self.load_data()

    def get_index(self):
        return self.index

    def get_chat_engine(self):
        return self.index.as_chat_engine()

    def initialize_vector_store(self):
        vector_store = PGVectorStore(
            connection_string=f"postgresql://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}/{SQL_DB}",
            table_name='documents'
        )
        return vector_store

    def load_data(self):
        vector_store = self.initialize_vector_store()
        Settings.llm = OpenAI(
            api_key=openai.api_key,
            model="gpt-4o-mini",
            temperature=0,
            system_prompt="""
        You are an intelligent documentation companion for developers working with this codebase. Your purpose is to help new developers ramp up quickly by providing accurate, contextual information about the code, architecture, and design decisions.

        When responding to queries:
        1. Provide clear, concise explanations about APIs, modules, classes, functions, and design choices.
        2. Include relevant code snippets when appropriate, properly formatted and with explanations.
        3. Always cite your sources by providing links or file paths to the relevant documentation or code.
        4. When discussing architectural decisions, reference any available decision records or design documents.
        5. If documentation is outdated or missing, clearly indicate this and provide the most accurate information available based on the current codebase.
        6. For implementation questions, explain both the "how" and the "why" behind design choices.
        7. When multiple approaches or patterns exist in the codebase, compare them and explain their respective use cases.
        8. If you're uncertain about something, acknowledge the limitations of your knowledge rather than providing potentially incorrect information.

        Your goal is to be a reliable, helpful guide that accelerates the onboarding process for new team members and serves as a valuable reference for all developers working with this codebase.
        """,
        )
        index = VectorStoreIndex.from_vector_store(vector_store)
        return index
