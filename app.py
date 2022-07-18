"""
Use argparse to check if the executor is a client or server
"""
import argparse
import traceback
import asyncio

import pydantic
import websockets
from decouple import config

from models.entity import Entity, Server, Client
from core.connector import Connector


async def main():
    try:
        parser = argparse.ArgumentParser(description='Ciena - Fibonacci')
        parser.add_argument('--type', dest='type', type=str,
                            help='type of entity allowed to access into the ' + \
                                'service, "client" and "server" are allowed')

        args = parser.parse_args().__dict__

        entity = Entity(**args)

        server = Server(entity)
        client = Client(entity)

        connector = Connector()

        if server.is_runnable():
            async with websockets.serve(
                connector.server_handler, config('HOST'), config('PORT')):
                print('Server-side is OK to receive connections\n\n')
                await asyncio.Future()

        if client.is_runnable():
            try:
                uri = f'ws://{config("HOST")}:{config("PORT")}'
                async with websockets.connect(uri) as websocket:
                    await connector.client_handler(websocket)

            except ConnectionRefusedError:
                print('Client - No server connected, please instance the server-side first')

    except pydantic.error_wrappers.ValidationError:
        traceback.print_exc()

if __name__ == '__main__':
    asyncio.run(main())
