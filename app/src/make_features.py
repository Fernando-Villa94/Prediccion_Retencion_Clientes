from app.utils.date_utils import function_listas_periodos, calcular_promedio_movil

def build_features(df_sales, periodo):

    u1m = function_listas_periodos(periodo, 1)
    u2m = function_listas_periodos(periodo, 2)
    u3m = function_listas_periodos(periodo, 3)
    u6m = function_listas_periodos(periodo, 6)
    u12m = function_listas_periodos(periodo, 12)

    df_1m = calcular_promedio_movil(df_sales, "codmes", "CustomerKey", "SalesAmount", u1m).rename(columns={"promedio": "ventas_ultimo_mes"})
    df_2m = calcular_promedio_movil(df_sales, "codmes", "CustomerKey", "SalesAmount", u2m).rename(columns={"promedio": "ventas_2m"})
    df_3m = calcular_promedio_movil(df_sales, "codmes", "CustomerKey", "SalesAmount", u3m).rename(columns={"promedio": "ventas_3m"})
    df_6m = calcular_promedio_movil(df_sales, "codmes", "CustomerKey", "SalesAmount", u6m).rename(columns={"promedio": "ventas_6m"})
    df_12m = calcular_promedio_movil(df_sales, "codmes", "CustomerKey", "SalesAmount", u12m).rename(columns={"promedio": "ventas_12m"})

    df_result = (
        df_1m.merge(df_2m, on="CustomerKey", how="left")
             .merge(df_3m, on="CustomerKey", how="left")
             .merge(df_6m, on="CustomerKey", how="left")
             .merge(df_12m, on="CustomerKey", how="left")
    )

    df_result["codmes"] = periodo
    return df_result