import pandas as pd
from sqlalchemy import create_engine
import os
from datetime import datetime

from app.src.build_population import get_population  
from app.src.make_features import build_features       
from app.src.prediction import score_model       


def pipeline_ejecucion(fecha):
    """
    Orquesta las fases del pipeline y genera un Excel final.
    """
    print("Conectando a SQL Server...")

    # CONFIGURA TU CADENA DE CONEXIÓN
    driver = "ODBC Driver 17 for SQL Server"
    #server = "DESKTOP-1D079GJ\\FERNANDOVILLA"
    server = "192.168.100.11,65033"
    database = "AdventureWorksDW2019"
    username = "sa"
    password = "Clevancf10"
    #conn_str = f"mssql+pyodbc://@{server}/{database}?driver={driver}&trusted_connection=yes"
    conn_str = f"mssql+pyodbc://api_user:TuPassword123!@192.168.100.11,65033/AdventureWorksDW2019?driver=ODBC+Driver+17+for+SQL+Server"
    engine = create_engine(conn_str)

    try:
        fecha_dt = datetime.strptime(fecha, "%Y-%m-%d")
    except:
        fecha_dt = datetime.now()

    fecha_inicio = fecha_dt.replace(year=fecha_dt.year - 1, day=1).strftime("%Y-%m-%d")
    periodo = int(fecha_dt.strftime("%Y%m"))

    print("1. Extrayendo población...")
    df_sales = get_population(engine, fecha)

    print("2. Construyendo features...")
    df_features = build_features(df_sales, periodo)

    print("3. Scoring del modelo...")
    df_scores = score_model(df_features)

    os.makedirs("output", exist_ok=True)
    df_scores.to_excel("output/resultados.xlsx", index=False)