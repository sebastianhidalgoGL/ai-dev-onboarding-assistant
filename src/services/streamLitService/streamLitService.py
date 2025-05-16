from src.services.streamLitService.chat import Chat
from src.services.streamLitService.message import Message
import streamlit as st
from constants import Avatars, LOGO

class StreamLitService:
    def __init__(self, llama_index_service):
        self.llama_index_service = llama_index_service
        self.initialize_session_state()
    
    def initialize_session_state(self):

        if "chat_engine" not in st.session_state:  # Initialize the chat engine
            st.session_state.chat_engine = self.llama_index_service.get_chat_engine()

        # Initialize the chat history
        if "chats" not in st.session_state:
            chat = Chat([
                Message("assistant", "Hi there!")
            ], "Chat 1")
            st.session_state["current_chat"] = chat.get_id()
            st.session_state["chats"] = [chat]
        current_chat = self.get_current_chat()
        st.title(current_chat.get_title())


    def run(self):
        self.display_sidebar()
        self.display_chat_history()
        self.handle_user_input()

    def display_sidebar(self):
        with st.sidebar:
            with st.container():
                 st.image(LOGO, width=150)
                 left, right = st.columns(2)
                 left.markdown("# Chat History")
                 right.markdown("")
                 right.button("New Chat +", type="tertiary", key="new_chat", use_container_width=True, on_click=self.generate_new_chat)
                 for chat in st.session_state["chats"]:
                     st.button(chat.get_title(), type="tertiary", key=f"chat_{chat.get_title()}", on_click=lambda chat_id=chat.get_id(): self.change_current_chat(chat_id))

    def change_current_chat(self, chat_id):
        print(f"Changing current chat to {chat_id}")
        st.session_state["current_chat"] = chat_id

    def generate_new_chat(self):
        new_chat = Chat([
            Message("assistant", "Hi there!")
        ], "Chat " + str(len(st.session_state["chats"]) + 1))
        st.session_state["chats"].append(new_chat)
        st.session_state["current_chat"] = new_chat.get_id()
    
    def get_current_chat(self):
        current_chat_id = st.session_state["current_chat"]
        for chat in st.session_state["chats"]:
            if chat.get_id() == current_chat_id:
                return chat
        return None

    def display_chat_history(self):
        current_chat = self.get_current_chat()
        for message in current_chat.get_messages():
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
        current_chat = self.get_current_chat()
        current_chat.add_message(Message("user", chat_prompt))
    
    def generate_assistant_response(self, chat_prompt):
        current_chat = self.get_current_chat()
        with st.chat_message("assistant", avatar=Avatars["assistant"]):
            response_stream = st.session_state.chat_engine.stream_chat(chat_prompt)
            st.write_stream(response_stream.response_gen)
            current_chat.add_message(Message("assistant", response_stream.response))


