import pandas as pd
import numpy as np 
from pathlib import Path   



#======== Funciones ======================================= 
# función para unir bases de datos de la misma estación

def procesar_estacion(ruta_base: str, ruta_secundaria: str) -> pd. DataFrame:
    """
    Esta función procesa, filtra y une los archivos base y secundario generados por la estación
    metereológica
    """

    print(f" - Procesando archivos: \n  - Base: {ruta_base}\n  - Secundarios: {ruta_secundaria}")

    # Paso 1: Cargar los datos
    df_base = pd.read_csv(ruta_base)
    df_sec = pd.read_csv (ruta_secundaria)
    columna_union = "Time" 

    # Paso 2: Identificar y seleccionar las columnas deseadas del archivo secundario
    columna_deseada = [
        col for col in df_sec.columns
        if col.startswith('AQIN ') or col == columna_union
    ]

    df_filter = df_sec[columna_deseada]

    # Paso 3: Unir los archivos a partir del archivo filtrado}
    df_final = pd.merge(df_base, df_filter, on=columna_union, how='left')

    # Paso 4: Añadir las variables vacías estándar para sensores adicionales 
    nuevas_var = ['amon', 'H2S', 'CO']
    for varibale in nuevas_var:
        df_final[varibale] = np.nan

    return df_final


#función para renombrar las columnas 
def renom_colms (df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """
    Esta función renombra las columnas del dataframe original generado por las estaciones 
    metereologicas. Para este caso utilizaremos un diccionario predefinido.
    En el caso que que alguna columno no este en el diccionario, la deja tal cual esta.

    """

    col_unnamed = [col for col in df.columns if 'Unnamed' in str(col)]
    if col_unnamed:
        df = df.drop(columns=col_unnamed)



    #Diccionario 
    nom_prede = {
    'Time' : 'time',
    'Timestamp' : 'timestamp',
    'Indoor Temperature(°C)' : 'in_temp_c',
    'Indoor Humidity(%)' : 'in_hum',
    'Outdoor Temperature(°C)' : 'out_temp_c',
    'Outdoor Humidity(%)' : 'out_hum',
    'Dew Point(°C)' : 'dew_point_c',
    'Feels Like(°C)' : 'feels_like_c',
    'BGT(°C)' : 'bgt_c',
    'WBGT(°C)' : 'wbgt_c',
    'VPD(kPa)' : 'vpd_kpa',
    'Wind(m/s)' : 'wind_ms',
    'Gust(m/s)' : 'gust_ms',
    'windDir_10min_avg(deg)' : 'wind_dir_10min_deg',
    'Wind Direction(deg)' : 'wind_dir_deg',
    'ABS Pressure(hPa)' : 'abs_pres_hpa',
    'REL Pressure(hPa)' : 'rel_pres_hpa',
    'Solar Rad(W/m2)' : 'solar_rad_wm2',
    'UV-Index' : 'uv_index',
    'Rain Rate(mm/Hr)' : 'rain_rate_mmhr',
    '24h Rain(mm)' : '24h_rain_mm',
    'Hourly Rain(mm)' : 'hourly_rain_mm',
    'Event Rain(mm)' : 'event_rain_mm',
    'Daily Rain(mm)' : 'daily_rain_mm',
    'Weekly Rain(mm)' : 'weekly_rain_mm',
    'Monthly Rain(mm)' : 'monthly_rain_mm',
    'Yearly Rain(mm)' : 'yearly_rain_mm',
    'Total Rain(mm)' : 'tot_rain',
    'Rain Status' : 'rain_status',
    'Piezo Rate(mm/Hr)' : 'p_rate_mmhr',
    'Piezo 24h Rain(mm)' : 'p_24h_rain_mm',
    'Piezo Hourly Rain(mm)' : 'p_hourly_rain_mm',
    'Piezo Event Rain(mm)' : 'p_event_rain_mm',
    'Piezo Daily Rain(mm)' : 'p_daily_rain_mm',
    'Piezo Weekly Rain(mm)' : 'p_weekly_rain_mm',
    'Piezo Monthly Rain(mm)' : 'p_monthly_rain_mm',
    'Piezo Yearly Rain(mm)' : 'p_yearly_rain_mm',
    'Piezo Total Rain(mm)' : 'p_total_rain_mm',
    'Piezo srain' : 'p_srain',
    'AQIN Temperature(°C)' : 'a_temp_c',
    'AQIN Humidity(%)' : 'a_hum',
    'AQIN CO2(ppm)' : 'a_co2_ppm',
    'AQIN PM2.5(ug/m3)' : 'a_pm2_5_ugm3',
    'AQIN PM10(ug/m3)' : 'a_pm10_ugm3',
    'AQIN PM1.0(ug/m3)' : 'a_pm1_ugm3',
    'AQIN PM4.0(ug/m3)' : 'a_pm4_ugm3',
    'amon' : 'nh3',
    'temp_amon': 'temp_nh3',
    'hum_amon': 'hum_nh3',
    'H2S' : 'h2s',
    'O2': 'o2',
    'CO' : 'co',
    'LEL': 'lel'
    }

    #Se crea el remplazo solo para las columnas 
    remplazo = {col: nom_prede[col] for col in df.columns if col in nom_prede}

    #Renombrando el dataframe
    df_renom = df.rename(columns=remplazo)
    print("Columnas renombradas exitosamente")

    #Agregamos columnas apartir del diccionario
    for nombre_original, nombre_nuevo in nom_prede.items():
        if nombre_nuevo not in df_renom.columns:
            df_renom[nombre_nuevo]=0
    
    #Ordenamos las columnas mediante el diccionario 
    colum_ordenadas = [nombre_nuevo for nombre_nuevo in nom_prede.values() if nombre_nuevo in df_renom.columns] 
    otras_columnas = [col for col in df_renom.columns if col not in colum_ordenadas]
    df_renom = df_renom[colum_ordenadas + otras_columnas]

    #Rellenamos las celdas vacias y los NaN con un 0
    df_renom = df_renom.replace(r'^\s*--\s*$', np.nan, regex=True)
    df_renom = df_renom.replace(r'^\s*$', np.nan, regex=True)
    
    if 'time' in df_renom.columns:
        colum_tiempo = df_renom['time'].copy()
        df_renom = df_renom.fillna(0)
        df_renom['time' ]= colum_tiempo
    else:
        df_renom = df_renom.fillna(0)

    for col in df_renom.columns:
        if col != 'time':
            df_renom[col] = pd.to_numeric(df_renom[col], errors='coerce').fillna(0)

    return df_renom, remplazo

def generar_meta(remplazo: dict, ruta_salida: str):
    """
    Esta función genera un archivo .txt ordenado con el diccionario con el nombre de las columnas
    """
    catalogo_detallado = {
        'time': ("Fecha y hora de la medición", "Fecha y hora de la medición"),
        'timestamp': ("Marca de tiempo del registro", "Marca de tiempo del registro de los datos"),
        'in_temp_c': ("Temperatura de interior", "Temperatura de interior (tomada por el hub)"),
        'in_hum': ("Humedad de interior", "Humedad de interior (tomada por el hub)"),
        'out_temp_c': ("Temperatura de exterior", "Temperatura de exterior"),
        'out_hum': ("Humedad de exterior", "Humedad de exterior"),
        'dew_point_c': ("Punto de rocío", "Punto de rocío"),
        'feels_like_c': ("Sensación térmica", "Sensación térmica"),
        'bgt_c': ("Temperatura de globo negro", "Mide la temperatura combinando el calor del aire, la radiación solar y el viento"),
        'wbgt_c': ("Temperatura de bulbo húmedo y globo", "Índice compuesto utilizado para evaluar el riesgo de golpe de calor, considera temperatura, humedad, viento y radiación"),
        'vpd_kpa': ("Déficit de presión de vapor", "Mide la diferencia entre la cantidad de humedad en el aire y el punto de saturación"),
        'wind_ms': ("Velocidad del viento", "Mide la velocidad actual o sostenida del viento en metros por segundo"),
        'gust_ms': ("Ráfaga de viento", "Ráfaga de viento máxima registrada en el último intervalo"),
        'wind_dir_10min_deg': ("Dirección promedio del viento", "Mide la dirección promedio del viento en los últimos 10 minutos medida en grados"),
        'wind_dir_deg': ("Dirección instantánea del viento", "Mide la dirección instantánea del viento en grados (0° o 360° es norte, 90° es este)"),
        'abs_pres_hpa': ("Presión atmosférica absoluta", "Peso real del aire en el punto exacto donde está el sensor"),
        'rel_pres_hpa': ("Presión atmosférica relativa", "Presión corregida y ajustada al nivel del mar"),
        'solar_rad_wm2': ("Radiación solar", "Radiación solar total recibida por metro cuadrado"),
        'uv_index': ("Índice de radiación UV", "Índice de radiación ultravioleta"),
        'rain_rate_mmhr': ("Intensidad de la lluvia", "Intensidad de la lluvia medida en milímetros por hora"),
        '24h_rain_mm': ("Lluvia acumulada en 24h", "Lluvia acumulada en las últimas 24 horas consecutivas"),
        'hourly_rain_mm': ("Lluvia acumulada por hora", "Lluvia acumulada por hora"),
        'event_rain_mm': ("Lluvia acumulada en el evento", "Lluvia acumulada durante el evento"),
        'daily_rain_mm': ("Lluvia acumulada en el día", "Lluvia acumulada en el día"),
        'weekly_rain_mm': ("Lluvia acumulada en la semana", "Lluvia acumulada en la semana"),
        'monthly_rain_mm': ("Lluvia acumulada en el mes", "Lluvia acumulada en el mes"),
        'yearly_rain_mm': ("Lluvia acumulada en el año", "Lluvia acumulada en el año"),
        'tot_rain': ("Historial de lluvia acumulada", "Historial de lluvia desde que se encendió el sensor"),
        'rain_status': ("Estado de la lluvia", "Indica si está lloviendo o no"),
        'p_rate_mmhr': ("Intensidad de lluvia (Piezo)", "Variable medida por el sensor piezoeléctrico, mide el impacto físico de las gotas de agua"),
        'p_24h_rain_mm': ("Lluvia 24h (Piezo)", "Variable medida por el sensor piezoeléctrico, mide el impacto físico de las gotas de agua"),
        'p_hourly_rain_mm': ("Lluvia por hora (Piezo)", "Variable medida por el sensor piezoeléctrico, mide el impacto físico de las gotas de agua"),
        'p_event_rain_mm': ("Lluvia por evento (Piezo)", "Variable medida por el sensor piezoeléctrico, mide el impacto físico de las gotas de agua"),
        'p_daily_rain_mm': ("Lluvia diaria (Piezo)", "Variable medida por el sensor piezoeléctrico, mide el impacto físico de las gotas de agua"),
        'p_weekly_rain_mm': ("Lluvia semanal (Piezo)", "Variable medida por el sensor piezoeléctrico, mide el impacto físico de las gotas de agua"),
        'p_monthly_rain_mm': ("Lluvia mensual (Piezo)", "Variable medida por el sensor piezoeléctrico, mide el impacto físico de las gotas de agua"),
        'p_yearly_rain_mm': ("Lluvia anual (Piezo)", "Variable medida por el sensor piezoeléctrico, mide el impacto físico de las gotas de agua"),
        'p_total_rain_mm': ("Lluvia total (Piezo)", "Variable medida por el sensor piezoeléctrico, mide el impacto físico de las gotas de agua"),
        'p_srain': ("Lluvia acumulada (Piezo subperiodo)", "Lluvia acumulada en el subperiodo específico o registro específico del sensor"),
        'a_temp_c': ("Temperatura (AQIN)", "Variable medida a través del sensor de calidad del aire"),
        'a_hum': ("Humedad (AQIN)", "Variable medida a través del sensor de calidad del aire"),
        'a_co2_ppm': ("Dióxido de carbono (AQIN)", "Concentración de dióxido de carbono medida en partes por millón"),
        'a_pm2_5_ugm3': ("PM2.5 (AQIN)", "Partículas finas menores a 2.5 micras. Indicador estándar para medir contaminación por humo"),
        'a_pm10_ugm3': ("PM10 (AQIN)", "Partículas gruesas de hasta 10 micras. Indicador de polvo, cenizas y polen"),
        'a_pm1_ugm3': ("PM1.0 (AQIN)", "Partículas ultrafinas menores a 1 micra. Indicador de virus, bacterias y combustión"),
        'a_pm4_ugm3': ("PM4.0 (AQIN)", "Partículas menores a 4 micras. Indicador para evaluar polvo ambiental y polen"),
        'nh3': ("Amoníaco", "Indicador de los niveles de amoníaco"),
        'temp_nh3':("Temperatura", "Temperatura medida por el sensor de amoníaco"),
        'hum_nh3': ("Humedad", "Humedad medida por el sensor de amoníaco"),
        'h2s': ("Ácido sulfhídrico", "Indicador de los niveles de ácido sulfhídrico"),
        'o2':("Oxígeno", "Indicador de los niveles de oxígeno"),
        'co': ("Monóxido de carbono", "Indicador de los niveles de monóxido de carbono"),
        'lel': ("Limite inferior de explosividad", "Indicador de la concentración de un gas combustible")

    }

    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write("=" * 120 + "\n")
        f.write(" DICCIONARIO DE METADATOS Y VARIABLES - ESTACIONES METEOROLÓGICAS\n")
        f.write("=" * 120 + "\n\n")
        f.write(f"Responsable de procesamiento: Luis Arturo Trejo\n")
        f.write("-" * 120 + "\n")
        f.write(f"{'Identificador ':<22} | {'Nombre de la variable':<35} | {'Descripción'}\n")
        f.write("-" * 120 + "\n")
        
        
        for original, nuevo in remplazo.items():
            # Buscamos en el catálogo detallado; si no existe, asignamos un texto genérico
            nombre_var, descripcion = catalogo_detallado.get(nuevo, (nuevo, "Variable registrada por el sistema de monitoreo."))
            f.write(f"{nuevo:<22} | {nombre_var:<35} | {descripcion}\n")
            
        f.write("\n" + "=" * 120 + "\n")
        f.write(" Versión 1.0\n")
        
    print(f"-> Archivo de metadatos detallado guardado en: {ruta_salida}")

# ====================================================================================================================================================


# =================================== Ejecución =====================================================================================================

def main():
    print( "--- Inicio de procesamiento de estaciones ---")

    #Directorio de las bases de datos de las estaciones
    base_dir = Path("C:/Users/LuisA/Documents/Datos/pruebas_proyecto")
    dir_final = Path("data")

    #Definimos las rutas para las 3 estaciones 
    estaciones = {
        "Estación 1":{
            "base": base_dir/ "est_1/202609B.csv",
            "secundario": base_dir/ "est_1/202609Allsensors_B.csv",
            "id": 1

        },
        "Estación 2":{
            "base": base_dir/ "est_2/202609B.csv",
            "secundario": base_dir/ "est_1/202609Allsensors_B.csv",
            "id": 2

        },
        "Estación 3":{
            "base": base_dir/ "est_3/202609B.csv",
            "secundario": base_dir/ "est_1/202609Allsensors_B.csv",
            "id":3
        }
    }
    
    #Generamos una lista para almacenar temporalmente los dataframes limpios de cada estación
    lista_datas = []


    #Iteramos sobre cada estación para procesarlas automáticamente
    for nombre_estacion, rutas in estaciones.items() :
        print(f"\n--- Procesando {nombre_estacion} (ID: {rutas['id']}) ---")
        try:
            # Paso 1: Fusionar daros
            df_resultado = procesar_estacion(rutas["base"], rutas["secundario"])

            # Paso 2: Limpiar y renombrar columnas 
            df_limpio, _= renom_colms(df_resultado)

            # Paso 3: Generar metadatos
            #generar_meta(colums, rutas["Metadatos"])

            # Paso 3: Añadir la columna "id" al inicio del Dataframe con el número correspondiente 
            df_limpio.insert(0, 'id', rutas['id'])
            lista_datas.append(df_limpio)
        except Exception as e:
            print(f"[ERROR] en {nombre_estacion}:{e}") 



    if lista_datas:
        df_final = pd.concat(lista_datas, ignore_index=True)

        nombre_archivo_csv = "data.csv"
        nombre_metadato = "metadata.txt"
        nom_carp = "20261007_chetumal"  #-----------> Cambiar cada que se procese los datos

        carp_dir = dir_final/ nom_carp
        carp_dir.mkdir(parents=True, exist_ok=True)


        #Guardamos el archivo csv
        ruta_data = carp_dir/nombre_archivo_csv
        ruta_meta = carp_dir/nombre_metadato

        #Guardamos los archivos
        df_final.to_csv(ruta_data, index=False, na_rep='0')

        meta = {col:col for col in df_final.columns if col !='id'}
        generar_meta(meta, ruta_meta)

        print("\n--- Procesamiento finalizado ---")  
        print(f"Archivo CSV: {ruta_data}")
        print(f"Metadatos en: {ruta_meta}")  

if __name__ == "__main__":
    main()
