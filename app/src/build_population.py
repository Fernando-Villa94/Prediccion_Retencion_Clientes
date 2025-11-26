import pandas as pd

def get_population(engine, fecha_u12):
    query = f"""
        SELECT * 
        FROM FactInternetSales 
        WHERE OrderDate >= '{fecha_u12}'
    """
    
    df = pd.read_sql(query, engine)
    df["codmes"] = df["OrderDateKey"] // 100
    return df