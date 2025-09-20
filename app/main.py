from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from typing import List
from . import schemas, services
from .exceptions import InconsistentDataError 
app = FastAPI(
    title="Sparta - Teste técnico",
    description="API para o teste de backend da Sparta"
)

@app.get("/")
def read_root():
    return {"message": "Teste técnico - Caio Dib :)"}

@app.post("/calcular", response_model=List[float])
def calcular_taxa_endpoint(data: schemas.InputData):
    """Recebe os dados do fundo e retorna a taxa de administração por cotista."""
    return services.calcular_taxa_administracao(data)


# Lança exceção personalizada
@app.exception_handler(InconsistentDataError)
async def inconsistent_data_handler(request: Request, exc: InconsistentDataError):
    return JSONResponse(
        status_code=400,  
        content={"detail": f"Erro nos dados fornecidos: {exc}"}
    )