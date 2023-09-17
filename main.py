from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

def gpt_call(messages):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=messages
)

    return response['choices'][0]['message']['content']

messages = [{"role": "system", "content": "you are a helpful assistant"}]

@app.post("/new_chat")
async def new_chat(request: Request):
    data = await request.form()
    message = data["message"]
    print(message)
    messages.append({"role": "user", "content": message})
    return HTMLResponse(f'<div class="bg-gray-700 px-4 py-2 mx-1 text-white" hx-get="gpt_response" hx-target=".messages" hx-trigger="load" hx-swap="beforeend">{message}</div>')

@app.get("/gpt_response")
async def gpt_resp():
    assistant_message = gpt_call(messages)
    messages.append({"role": "assistant", "content": assistant_message})
    return HTMLResponse(f'<div class="bg-gray-600 px-4 py-2 mx-1 text-white">{assistant_message}</div>')


app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
