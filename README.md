
# GPT-3 Chatbot

This project is a FastAPI application that interacts with the OpenAI GPT-3 model to create a chatbot.

## Code Explanation

The `main.py` file contains the main logic of the application. It defines a function `gpt_call` that makes a call to the GPT-3 model with a list of messages and returns the model's response. It also defines two FastAPI routes: `/new_chat` and `/gpt_response`. The `/new_chat` route accepts a POST request with a message from the user, adds it to the list of messages, and returns an HTML response with the user's message. The `/gpt_response` route makes a call to the GPT-3 model with the list of messages, adds the model's response to the list of messages, and returns an HTML response with the model's response.

The application also serves static files from the `static` directory.

## Project File Structure

- `main.py`: This is the main Python file. It contains the logic of the application.
- `static`: This is a directory that contains static files.
  - `index.html`: This is an HTML file that contains the structure of a web page.
