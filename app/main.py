from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
import rag_module 
import json

app = FastAPI()
rag = rag_module.RAG("127.0.0.1", 6379)
document_keys = ["doc:1", "doc:2", "doc:3", "doc:4"]

# Definir el modelo para el vector
class VectorF(BaseModel):
    vector: List[float]
    
@app.post("/rag-redis-torch")
def rag_paradigm(pregunta: str):
    
    query = pregunta
    response = rag.generate_response(query, document_keys)
    
    j1 = {
        "pregunta": pregunta, 
        "respuesta": response
    }
    jj = json.dumps(str(j1))

    return jj
