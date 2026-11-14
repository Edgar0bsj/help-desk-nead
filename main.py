from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from router.user_router import router as user_router

# uvicorn main:app --reload --port 8080
app = FastAPI()


app.mount("/assets", StaticFiles(directory="public/assets"), name="assets")

app.include_router(user_router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
