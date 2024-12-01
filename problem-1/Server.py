import asyncio
import websockets
from Message import Message, MessageManager

# Instantiate the MessageManager to handle messages
message_manager = MessageManager()

# Define an asynchronous function to handle the WebSocket connection
async def handle_websocket(websocket, path):
    print("Client Connected!")
    
    try:
        # This loop listens for incoming messages from the WebSocket
        async for message in websocket:
            print(f"Received: {message}")
            
            # Simulate message creation for conversation handling
            message_manager.add_message(sender="Client", phone_number="000-000-0000", content=message)

            # Respond back to the client
            await websocket.send(f"Message Received: {message}")

    except websockets.ConnectionClosed:
        print("Client Disconnected")

# Define the main asynchronous function to start the WebSocket server
async def main():
    # Start the WebSocket server on localhost at port 6789
    async with websockets.serve(handle_websocket, "localhost", 6789):
        print("WebSocket server started on ws://localhost:6789")
        await asyncio.Future()  # Keep the server running

if __name__ == "__main__":
    asyncio.run(main())  # Run the WebSocket server asynchronously
