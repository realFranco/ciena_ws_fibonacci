# Ciena Websocket - Fibonacci Communication

Socket implementation to handle comunications between entities,
a server side and one or many clients.

The client will send numeric data into the server and this one will
expose a Fibonacci sequence.

Also, the service will hang up waiting for the user to instance a new
computation flow.

This is a code from Ciena challenge.


## Installation Steps

As a recommendation, install a new virtual environment:

    python3 -m venv env

    source env/bin/activate

Now proceed with the installation of dependencies:

    pip3 install -r requirements.txt

Create a file to store environment variables:

    nano .env

    # And write this:
    HOST='localhost'
    PORT='8000'

    # Then save it and exit


## How to Test

To cover unit testing I selected pytest as tool:

    pytest test

    # If you wanna be verbose
    pytest test -s -v


## How to Execute

Consider that the service has only one entry point "app.py"
and two entities (server, client).

    # Remember to activate the virtual environment before run the entry point

    # Execute one server instance
    python3 app.py --type server

    # And only them, execute at least 1 client instance
    python3 app.py --type client

If you instance a client without a server, will be exposed an error.

Also, there are only two allowed entities to run the project:
 - server
 - client

If you write another string, will be raise an error.


## Importance notice

There is a problem buildind the dependency "evdev", happens on my distro:
Ubuntu 20.04

    Failed to build evdev

But the problem not affect the basic flows for the project.


## Posible Problems

- If the client (or many of them) do not perform any action, the server 
    and all the clients will be waiting forever.

- If no clients are connected and the server is running, them the server will
    be waiting forever.


## Considering another solution

- As fan of framework and python technologies I can consider FastAPI as
    another tool set to solve this assessment. Some elements are already
    covered and easy to implement, for example:
        - Logs
        - Authentication
        - Authorization
        - Deploy to production

## Improve scenarios
    
I consider some topics to improve the service:

 - Fibonacci computation: The project implement a variant of Fibonacci, 
    use a tiny persistance layer, to avoid re-computate of elements, but also
    could be use a memorization and implement the function in iterative manner,
    reducing the Big O complexity.

 - Instalations by scopes DEV | STAGE | PROD: The install of depedencies is the same
    for every context, develop, stage and production. Could be segmented to 
    expose a "context" and install depdencies in a proper way.

🇨🇦 | 🇻🇪
