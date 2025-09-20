from pydantic import BaseModel
from typing import List

class ItemCota(BaseModel):
    valor: float
    quantidades: List[float]

class InputData(BaseModel): # o input deve ter esses dois campos
    taxa: float
    cotas: List[ItemCota]