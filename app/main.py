from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from app.src.run_model import pipeline_ejecucion   # <-- CORREGIDO

app = FastAPI(title="Predicción Retención Clientes")

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ejecutar", response_class=HTMLResponse)
async def ejecutar(request: Request, fecha: str = Form(...)):
    pipeline_ejecucion(fecha)
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request,
            "mensaje": f"Pipeline ejecutado correctamente. Archivo generado en output/resultados.xlsx"
        }
    )