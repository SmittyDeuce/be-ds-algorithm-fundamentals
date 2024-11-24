from datetime import datetime
import time

class Message:
    # Class attribute to track next message_id
    message_counter = 0
    def __init__(self, sender, phone_number, content):
        # Increment the counter and assign it as the message ID
        Message.message_counter += 1
        self.message_id = Message.message_counter


        self.sender = sender
        self.phone_number = phone_number
        self.content = content

        # Get the current datetime
        now = datetime.now()

        # Formatted to remove seconds and microseconds.
        self.timestamp = now.strftime("%m-%d-%Y %H:%M")

    @staticmethod
    def search_by(messages, search_str, search_type='sender'):
        results = []
        # Search by sender name
        if search_type == 'sender':
            for message in messages:
                if search_str.lower() in message.sender.lower():  # case insensitive
                    results.append(message)
        
        # Search by phone number
        elif search_type == 'phone_number':
            for message in messages:
                if search_str in message.phone_number:  # exact match on phone number
                    results.append(message)
        
        # If no results are found, print a message
        if not results:
            print("No messages found for search type")
        
        return results

    @staticmethod
    def search_message(messages, search_str):

        # Search for messages containing the given substring in their content.
        # :param messages: List of Message objects to search.
        # :param search_str: The substring to search for.
        # :return: List of Message objects matching the search criteria.

        # gather matching messages
        results = []
        for message in messages:
            if search_str.lower() in message.content.lower():
                results.append(message)
        return results

inbox = []

inbox.append(Message(sender="Mom", phone_number="123-456-7890", content="Don't forget to do your chores"))
inbox.append(Message(sender="Sister", phone_number="123-555-7890", content="Mom said, no games before chores"))
inbox.append(Message(sender="Brad", phone_number="123-999-7890", content="Can you play Minecraft rn?"))
inbox.append(Message(sender="Mom", phone_number="123-456-7890", content="and homework"))


# Create a dictionary of message_id to Message for O(1) lookup
message_dict = {message.message_id: message for message in inbox}

# print all messages inside inbox
for message in inbox:
    print(f"Message ID: {message.message_id}, Sender: {message.sender}, Message: {message.content}, {message.timestamp}")

# Example of searching by sender name
search_results = Message.search_by(inbox, "Mom", search_type="sender")
print("\nSearch Results by Sender:")
for result in search_results:
    print(f"Message ID: {result.message_id}, Sender: {result.sender}, Phone Number: {result.phone_number}, Message: {result.content}, Timestamp: {result.timestamp}")

# Example of searching by phone number
search_results = Message.search_by(inbox, "123-456-7890", search_type="phone_number")
print("\nSearch Results by Phone Number:")
for result in search_results:
    print(f"Message ID: {result.message_id}, Sender: {result.sender}, Phone Number: {result.phone_number}, Message: {result.content}, Timestamp: {result.timestamp}")


# wait 1min before adding new message to test timestamp
time.sleep(60)
inbox.append(Message(sender="Dad", content="make sure to lock the door when you get home"))

# Print the updated inbox with the new message
print("\nUpdated Inbox Messages:")
for message in inbox:
    print(f"Message ID: {message.message_id}, Sender: {message.sender}, Message: {message.content}, {message.timestamp}")



# Search for messages containing the word 'chores'
search_results = Message.search_message(inbox, "chores")

# Print search results
print("\nSearch Results:")
if search_results:
    for result in search_results:
        print(f"Sender: {result.sender}, Content: {result.content}, Timestamp: {result.timestamp}")
else:
    print("No messages found.")