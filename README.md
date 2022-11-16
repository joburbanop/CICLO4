# CICLO4
proyecto mision tic ciclo 4
CODIGO



from fastapi import FastAPI  
from pydantic import BaseModel
#from typing importr list 
from uuid import uuid4


app = FastAPI ()

class Paquete(BaseModel):

 id: str 
 name: str
 lastname: str
 #skills: listt [str]:

paquetes =[]


 @app.get ("/paquetes")
 def get_paquetes():
    return paquetes


 @app.get("/paquetes/{id}")
 def get_paquetes (id: str):
     for paquetes in paquetes:
        if paquete ["id"]== id:
            return "No existe el paquete"


 @app.post ("/paquete/")
 def save_paquetes (paquete:paquete):
    paquete.id = str(uuid4())
    get_paquetes.append(paquete.dict())
    return "Paquete registrado"

 @app.put("/paquetes/{id}") 
 def update_paquetes(update_paquete: paquete, id:str):
    for paquete in paquetes:
        if paquete["id"]== id:
            paquete[name] = update_update.name
            paquete[lastname] = update_update.lastname
            #paquete["skils"] =  update_update.skills
            return "Paquete modificado"
    return "No existe el paquete"

 @app.delete ("/paquetes/{id}")
 def delete_paquete(id: str):
    for paquete in paquete:
        if paquete["id"]== id:
            paquete.remove(paquete)
            return "Paquete eliminado"
    return "No existe el paquete"
