from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from router.auth_router import router as auth_router
from router.user_router import router as user_router

# uvicorn main:app --reload --port 8080
app = FastAPI()


app.mount("/assets", StaticFiles(directory="public/assets"), name="assets")

app.include_router(auth_router)
app.include_router(user_router)
