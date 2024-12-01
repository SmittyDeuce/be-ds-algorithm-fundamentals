from datetime import datetime

class MessageManager:
    def __init__(self):
        self.messages = []  # List to store all messages
        self.message_dict = {}  # Dictionary to store messages by their message_id
        self.conversations = {}  # Dictionary to store messages grouped by conversation_id

    def add_message(self, sender, phone_number, content, conversation_id=None):
        message = Message(sender, phone_number, content)
        self.messages.append(message)
        self.message_dict[message.message_id] = message

        # If a conversation_id is provided, associate the message with the conversation
        if conversation_id:
            if conversation_id not in self.conversations:
                self.conversations[conversation_id] = []
            self.conversations[conversation_id].append(message)

        return message

    def search_by(self, search_str, search_type="sender"):
        # Search messages by sender or phone_number
        if search_type == "sender":
            return [msg for msg in self.messages if search_str.lower() in msg.sender.lower()]
        elif search_type == "phone_number":
            return [msg for msg in self.messages if search_str == msg.phone_number]
        else:
            raise ValueError("Invalid search_type. Use 'sender' or 'phone_number'.")

    def search_message_content(self, search_str):
        # Search for messages by content
        return [msg for msg in self.messages if search_str.lower() in msg.content.lower()]

    def filter_conversations(self, conversation_id):
        # Retrieve all messages for a specific conversation
        if conversation_id in self.conversations:
            return sorted(self.conversations[conversation_id], key=lambda msg: msg.timestamp, reverse=True)
        return []

    def print_messages(self):
        # Print all messages in the message manager
        for message in self.messages:
            print(message)

class Message:
    # Class attribute to track next message_id
    message_counter = 0

    def __init__(self, sender, phone_number, content):
        if not sender or not content:
            raise ValueError("Sender and content cannot be empty.")

        # Increment the counter and assign it as the message ID
        Message.message_counter += 1
        self.message_id = Message.message_counter
        self.sender = sender
        self.phone_number = phone_number
        self.content = content

        # Timestamp formatted without seconds and microseconds
        self.timestamp = datetime.now().strftime("%m-%d-%Y %H:%M")

    def __str__(self):
        return (
            f"Message ID: {self.message_id}, Sender: {self.sender}, "
            f"Phone Number: {self.phone_number}, Message: {self.content}, Timestamp: {self.timestamp}"
        )

# Example of managing messages and conversations
if __name__ == "__main__":
    message_manager = MessageManager()

    # Add messages and associate with conversation IDs
    message_manager.add_message("Mom", "123-456-7890", "Don't forget to do your chores", conversation_id="1")
    message_manager.add_message("Sister", "123-555-7890", "Mom said, no games before chores", conversation_id="1")
    message_manager.add_message("Brad", "123-999-7890", "Can you play Minecraft?", conversation_id="2")

    # Print all messages
    print("Inbox Messages:")
    message_manager.print_messages()

    # Search by sender
    print("\nSearch Results by Sender (Mom):")
    for result in message_manager.search_by("Mom", search_type="sender"):
        print(result)

    # Search by phone number
    print("\nSearch Results by Phone Number (123-456-7890):")
    for result in message_manager.search_by("123-456-7890", search_type="phone_number"):
        print(result)

    # Search by content
    print("\nSearch Results for Content (chores):")
    for result in message_manager.search_message_content("chores"):
        print(result)

    # Print messages for a specific conversation sorted by timestamp
    print("\nMessages for Conversation 1 (Sorted by Timestamp):")
    for msg in message_manager.filter_conversations("1"):
        print(msg)
