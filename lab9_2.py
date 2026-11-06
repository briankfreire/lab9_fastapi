from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Lab9 RESTful API",
    description="API RESTful criada com FastAPI",
    version="1.0.0"
)

# Modelo de dados usando Pydantic para validação do corpo da requisição
class ItemCreate(BaseModel):
    mensagem: str
    origem: Optional[str] = "Postman"

# Banco de dados temporário em memória
mensagens = [
    {"id": 1, "mensagem": "Hello, World!", "origem": "FastAPI RESTful API"}
]

# Rota raiz
@app.get("/", status_code=status.HTTP_200_OK)
def index():
    return {"status": "success", "message": "API FastAPI RESTful ativa. Acesso disponível em /items"}

# Rota GET: Listar todos os itens
@app.get("/items", status_code=status.HTTP_200_OK)
def get_items():
    return {"status": "success", "data": mensagens}

# Rota POST: Criar um novo item
@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    novo_item = {
        "id": len(mensagens) + 1,
        "mensagem": item.mensagem,
        "origem": item.origem
    }
    mensagens.append(novo_item)
    return {"status": "success", "data": novo_item}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("lab9_2:app", host="127.0.0.1", port=5000, reload=True)