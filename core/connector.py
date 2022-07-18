"""
This gonna be the connector manager.
"""
import uuid
import json

import websockets
from websockets.exceptions import ConnectionClosedError
from pynput import keyboard

from models.entity import ContextType
from core.utils import Computation, DataManagement


KEEP_A_LIVE = json.dumps({'message': 'Keep a live'})


class Connector:
    
    def __init__(self, type: ContextType = None):
        # based on the type, create a connection to the client | server
        self.type = type
        self.connections = dict()
    
    async def server_handler(self, websocket):
        while True:
            try:
                message = await websocket.recv()
                # print(message)  # Remove the comment and get exposed the "keep a live" messages

                if message:
                    message = json.loads(message)

                    if 'id' in message and not message['id'] in self.connections:
                        print(f'New connection received: {message["id"]}')
                        self.connections[message['id']] = websocket

                    if 'l' in message and 'r' in message:
                        print('<<< Fibonacci Received')
                        l, r = DataManagement.sanitize_data(data=message)
                        fib = Computation.fibonacci_in_range(l=l, r=r)
                        memo = 'Remember to press "Space" to proceed with a new Fibonacci computation.'
                        out = f'>>> Fibonacci: {fib}\n\n{memo}'
                        await websocket.send(out)
                    else:
                        await websocket.send(KEEP_A_LIVE)

            except websockets.ConnectionClosedOK:
                # There is no active connections, after a while the server will go to sleep
                pass

            except ConnectionClosedError:
                if self.connections:
                    self.connections = {}
   
    async def client_handler(self, websocket, old_id: str = None):
        conn_id = old_id if old_id else str(uuid.uuid4())
        try:
            print('Press "Space" to proceed into Fibonacci computation: ')
            while True:
                # Client Keep a live scenario
                # print('Press "Space" to proceed into Fibonacci computation: ')
                while True:
                    await websocket.send(KEEP_A_LIVE)
                    message = await websocket.recv()
                    # print(message)  # Remove the comment and get exposed the "keep a live" messages

                    with keyboard.Events() as events:
                        event = events.get(1.0)
                        if event:
                            if event.key == keyboard.Key.space:
                                events = None
                                break
                
                print('')
                left = input('Insert start sequence: ')
                right = input('Insert end sequence: ')
                message = {'id': conn_id, 'l': left, 'r': right}
                await websocket.send(json.dumps(message))

                if not conn_id in self.connections:
                    self.connections[conn_id] = websocket

                message = await websocket.recv()
                print(message)

        except websockets.ConnectionClosedOK:
            print('Client - Closing the connection')
