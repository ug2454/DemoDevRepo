from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Demo REST Service")


class UserIn(BaseModel):
    name: str
    email: str


class User(UserIn):
    id: int


_USERS: Dict[int, User] = {}
_NEXT_ID = 1


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/users", response_model=User, status_code=201)
def create_user(payload: UserIn):
    global _NEXT_ID
    user = User(id=_NEXT_ID, name=payload.name, email=payload.email)
    _USERS[_NEXT_ID] = user
    _NEXT_ID += 1
    return user


@app.get("/users", response_model=list[User])
def list_users():
    return list(_USERS.values())


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = _USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user
