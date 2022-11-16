from fastapi import FastAPI  
from pydantic import BaseModel
#intanciacion de la librria importada desde fastapi que esta en el entorno virtual creado
app = FastAPI ()

class Paquete(BaseModel):
    id: str 
    remitente: str
    receptor: str

paquetes =[]

@app.get("/paquetes")
def get_paquetes():
    return paquetes

@app.get("/paquetes/{id}")
def get_paquete (id: str):
    for paquete in paquetes:
        if paquete ["id"]== id:
         return "No existe el paquete"

@app.post("/paquete/")
def save_paquete (paquete:Paquete):
    paquete.id = str(uuid4())
    get_paquetes.append(paquetes.dict())
    return "Paquete registrado"

@app.put("/paquetes/{id}") 
def update_paquete(update_paquete: Paquete, id:str):
    for paquete in paquetes:
        if paquete["id"]== id:
            paquete[remitente] = update_update.remitente
            paquete[receptor] = update_update.receptor
            #paquete["skils"] =  update_update.skills
        return "Paquete modificado"
    return "No existe el paquete"

@app.delete("/paquetes/{id}/eliminar")
def delete_paquete(id: str):
    for paquete in paquetes:
        if paquete["id"]== id:
            paquetes.remove(paquete)
            return "Paquete eliminado"
    return "No existe el paquete"