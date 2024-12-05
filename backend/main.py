import os
from dotenv import load_dotenv
import logging
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.logger import logger as fastapi_logger
import openai

DEBUG = False

# -----------------------------------------------------------------------------------
#
# Initialization
#
# -----------------------------------------------------------------------------------

load_dotenv()

client = openai.AsyncOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1"
)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
if "gunicorn" in os.environ.get("SERVER_SOFTWARE", ""):
    """
    When running with gunicorn the log handlers get suppressed instead of
    passed along to the container manager. This forces the gunicorn handlers
    to be used throughout the project.
    """

    gunicorn_logger = logging.getLogger("gunicorn")

    root_logger = logging.getLogger()
    gunicorn_error_logger = logging.getLogger("gunicorn.error")
    uvicorn_access_logger = logging.getLogger("uvicorn.access")

    # Use gunicorn error handlers for root, uvicorn, and fastapi loggers
    root_logger.handlers = gunicorn_error_logger.handlers
    uvicorn_access_logger.handlers = gunicorn_error_logger.handlers
    fastapi_logger.handlers = gunicorn_error_logger.handlers

    # Pass on logging levels for root, uvicorn, and fastapi loggers
    root_logger.setLevel(logging.INFO)
    uvicorn_access_logger.setLevel(logging.INFO)
    fastapi_logger.setLevel(logging.INFO)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
async def read_root(request: Request):
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/hello")
async def get_hello():
    """
    Returns a simple hello from the LLM.
    """
    try:
        response = await client.chat.completions.create(
            # Gemini because it's really cheap and fast.
            model="google/gemini-flash-1.5-8b",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI that's part of a fun and experimental web app prototype. You're interacting with the developer of the app. Be friendly and feel free to use emojis in your responses!",
                },
                {"role": "user", "content": "Hi, how are you?"},
            ],
        )
        return {"message": response.choices[0].message.content}
    except Exception as e:
        return {"message": f"Error: {e}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
    )
