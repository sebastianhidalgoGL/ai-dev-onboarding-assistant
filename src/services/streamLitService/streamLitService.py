from src.services.streamLitService.message import Message
import streamlit as st
from constants import Avatars

class StreamLitService:
    def __init__(self, llama_index_service):
        self.llama_index_service = llama_index_service
        self.initialize_session_state()
    
    def initialize_session_state(self):
        if "chat_engine" not in st.session_state: 
            st.session_state.chat_engine = self.llama_index_service.get_chat_engine()
        if "messages" not in st.session_state:
            st.session_state["messages"] = [
                Message("assistant", "Hi there!")
            ]

    def run(self):
        self.display_chat_history()
        self.handle_user_input()

    def display_chat_history(self):
        for message in st.session_state["messages"]:
            with st.chat_message(message.role, avatar=Avatars[message.role]):
                st.markdown(message.content)

    def handle_user_input(self):
        chat_prompt = st.chat_input("What is up?")
        if chat_prompt:
            self.process_user_message(chat_prompt)
            self.generate_assistant_response(chat_prompt)
    
    def process_user_message(self, chat_prompt):
        with st.chat_message("user", avatar=Avatars["user"]):
            st.markdown(chat_prompt)
        st.session_state["messages"].append(Message("user", chat_prompt))
    
    def generate_assistant_response(self, chat_prompt):
        with st.chat_message("assistant", avatar=Avatars["assistant"]):
            response_stream = st.session_state.chat_engine.stream_chat(chat_prompt)
            st.write_stream(response_stream.response_gen)
            st.session_state["messages"].append(Message("assistant", response_stream.response))


