from dateutil.relativedelta import relativedelta
import datetime as dt
import pandas as pd

def function_listas_periodos(codmes_actual, n):
    anio = codmes_actual // 100
    mes = codmes_actual % 100
    lista_periodos = []
    
    for i in range(n):
        nuevo_mes = mes - i
        nuevo_anio = anio
        if nuevo_mes <= 0:
            nuevo_mes += 12
            nuevo_anio -= 1
        lista_periodos.append(nuevo_anio * 100 + nuevo_mes)
    
    return lista_periodos


def calcular_promedio_movil(df_mensual, variable_mes, idcliente, col_variable, lista_periodos):
    df_filtrado = df_mensual[df_mensual[variable_mes].isin(lista_periodos)]

    df_agrupado = (
        df_filtrado.groupby(idcliente, as_index=False)[col_variable]
        .sum()
        .assign(promedio=lambda x: x[col_variable] / len(lista_periodos))
    )
    
    return df_agrupado[[idcliente, "promedio"]]


def shift_codmes(codmes: int, n_months: int) -> int:
    year = codmes // 100
    month = codmes % 100
    date = dt.date(year, month, 1)
    new_date = date + relativedelta(months=n_months)
    return new_date.year * 100 + new_date.month