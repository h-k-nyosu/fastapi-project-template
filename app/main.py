from fastapi import FastAPI

from app.api.routes import router

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(router, prefix="/v1")
