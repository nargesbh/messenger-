# Messenger App

This repository contains a simple messenger application consisting of two Python files: `server.py` and `telegram.py`. This messenger app allows users to sign up, sign in, send messages to other users, block/unblock users, and view message history. Below, you'll find a brief overview of each file's functionality and how to use the messenger app.

## `server.py`

`server.py` is responsible for managing the backend database operations. It connects to a MySQL database and handles various client requests. Here's an overview of its functions:

- **main(client_sent)**: This is the main function that processes client requests and routes them to the appropriate functions based on the user's input.
- **get_user_names()**: Retrieves a list of all user names from the database.
- **insert_delete(query)**: Executes INSERT and DELETE queries on the database.
- **send_password(client_sent)**: Retrieves a user's password based on their username.
- **get_all_messages(query)**: Retrieves messages from the database based on a query.
- **block_check(query)**: Checks if a user is blocked based on a query.

## `telegram.py`

`telegram.py` is the main application file that users interact with. It provides a command-line interface for users to sign up, sign in, and communicate with other users. Here's a brief overview of its functionality:

- **sign_up()**: Allows a user to sign up by providing personal information and choosing a username and password.
- **sign_in()**: Allows an existing user to sign in by entering their username and password.
- **after_enter(user)**: Handles interactions after signing in, including choosing a user to communicate with and viewing messages.
- **send_message(sender, receiver)**: Allows a user to send messages to another user.
- **show_all_messages(sender, receiver)**: Displays the message history between two users.
- **block_func(blocker, blocked_id)**: Blocks a user from sending messages.
- **block_check(sender, receiver)**: Checks if a user is blocked by another user and provides options for blocking/unblocking.

## Getting Started

1. Ensure you have Python installed on your system.

2. Set up a MySQL database and configure the connection settings in `server.py` (host, user, password, and database).

3. Run `server.py` to start the server.

4. Run `telegram.py` to use the messenger app.

## Usage

1. When you run `telegram.py`, you can choose to sign up or sign in.

2. If you sign up, you'll be prompted to provide personal information and choose a username and password.

3. If you sign in, you can interact with other users by choosing their usernames and sending messages.

4. You can block/unblock users and view your message history.

5. Follow the command-line prompts for each action.

This is a basic overview of how the messenger app works. You can further customize and expand its features as needed. Enjoy communicating with your friends using this simple messenger app!
