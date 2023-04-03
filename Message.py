class Message:
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.SYSTEM = "system"

    def __str__(self):
        return f"{self.sender} : {self.content}"

    def dict_to_message(self, dictionary):
        self.sender = dictionary["sender"]
        self.content = dictionary["content"]
        return self

    def to_dict(self):
        return {
            "role": self.sender,
            "content": self.content
        }
