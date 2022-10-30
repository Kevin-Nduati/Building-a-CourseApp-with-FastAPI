from  fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()
users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model = List[User])
async def get_users():
    return users


@app.post("/users")
async def create_users(user: User):
    users.append(user)
    return "success"


@app.get("users/{id}")
async def get_user(id: int = Path(..., description="The Id of the user you want to retrieve", gt=2),
                                    q: str = Query(None, max_length=5)):
    return {"user": users[id], 'query': q}