from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Auth demo")

# Orígenes permitidos (Vue corre en 5173)
origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # en desarrollo puedes usar ["*"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    email: str
    password: str

# Base de datos simulada
fake_db = {"user@test.com": "Test123"}

# Ruta de registro
@app.post("/register")
async def register(user: User):
    if user.email in fake_db:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    fake_db[user.email] = user.password
    return {"message": "Usuario registrado con éxito"}

# Ruta de login
@app.post("/login")
async def login(user: User):
    if user.email not in fake_db or fake_db[user.email] != user.password:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"message": "Inicio de sesión exitoso"}
