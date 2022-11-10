from fastapi import FastAPI

from src.controllers.home import home

app = FastAPI()
app.include_router(home.router)

