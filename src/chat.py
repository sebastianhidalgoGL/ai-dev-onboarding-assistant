import uuid

class Chat:
    def __init__(self, messages, title):
        self.messages = messages
        self.title = title
        self.id = str(uuid.uuid4())

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_id(self):
        return self.id
