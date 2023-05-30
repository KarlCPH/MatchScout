from database import models
from discord_bot.bot import run_bot
from fastapi_app import app
from database import engine

# Initialize the database models and establish the connection
models.Base.metadata.create_all(bind=engine)

# Start the Discord bot
# run_bot()

# Run the FastAPI application
# routes.app.run()
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("fastapi_app:app", host="0.0.0.0", port=8000)
