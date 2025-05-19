from fastapi import FastAPI, HTTPException
from server.databases.UserDataBase import connect_user_db
from server.routes import user as user_routes
import os, uvicorn

app = FastAPI()

MONGO_DB_URL = os.getenv("MONGO_DB_URI")
USER_DATABASE_NAME = os.getenv("DATABASE_NAME")
USER_COLLECTION = os.getenv("USER_DATA_COLLECTION")

user_db_client = connect_user_db(MONGO_DB_URL, USER_DATABASE_NAME, USER_COLLECTION)

app.include_router(user_routes.router)

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

@app.get("/")
def read_root():
    return {"Hello": "World"}