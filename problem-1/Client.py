import asyncio
import websockets

# Define async func to connect to websocket server
async def connect():
    uri = 'ws://localhost:6789'  # WebSocket URI to connect to the server

    # Connect to websocket URI
    async with websockets.connect(uri) as websocket:
        print("Connected to server!")  # Client connection confirmation

        await websocket.send("Hello Server!")  # Send message to server

        response = await websocket.recv()  # Wait for a response from the server

        print(f"Server Response: {response}")  # Print server response

# Run the connect function, which starts the event loop and handles WebSocket communication
asyncio.run(connect())  # This manages the asynchronous event loop
