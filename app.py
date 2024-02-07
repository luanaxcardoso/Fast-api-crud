from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("2fa229c5-952e-455c-9032-ce6eaf32fbe1"),
        first_name="João",
        last_name="Silva", 
        email="joao@gmail.com",
        role=[Role.role_1]
        ),
    User(
        id=UUID("faceb8f6-561c-4010-83ef-6cad2324ca8f"),
        first_name="Luana",
        last_name="Cardoso", 
        email="luana@gmail.com",
        role=[Role.role_2]
        ),
    User(
        id=UUID("3895b1a4-9c67-48a4-9b9f-050f5b154e4a"),
        first_name="Maria",
        last_name="Santos", 
        email="maria@gmail.com",
        role=[Role.role_3]
        )
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "User not found"}

@app.post("/api/users")
async def add_user(user: User):
    db.append(user) # adiciona o usuário no banco de dados
    return {"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return 
        raise HTTPException(
            status_code=404, 
            detail=f"Usuário com id {id} não encontrado!"
        )