from fastapi import FastAPI
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fatura Takip Sistemi")

@app.get("/")
def root():
    return {"mesaj": "Fatura Takip Sistemi çalışıyor ✅"}