# **Pipeline de los datos generados por las estaciones metereológicas**


Pipeline automatizado en Python para la unión de bases de dato provenientes de 3 estaciones meteorológicas de monitoreo. Este proyecto está gestionado mediante **uv** para garantizar un control de entornos virtuales eficiente y reproducibles. Se diseñó para agilizar la unión de los datos generados por cada estacion metereológica en un solo archivo. Uno de sus principales utilidades es cambiar el nombre de las variables originales que contienen caracteres especiales por nombres identificadores nombrados por el equipo de investigación. Además crea un metadato donde se describe cada una de las variables. 

## El proyecto se estructura de la siguiente manera
```text
SAQ/
|
|---.venv/                          # Entorno virtual gestionado por uv 
|--- docs/
|     |--- Manual_uv.pdf
|--- data/                          # Almacenamiento de resultados y metadatos 
|     |--- 20261007_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos 
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261008_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261009_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos 
|     |     |--- metadata.txt       # ------> Metadatos
|     |--- 20261010_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261011_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos 
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261012_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261013_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos 
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261014_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos 
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261015_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos 
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261016_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261017_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261018_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261019_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261020_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261021_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos 
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261022_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos 
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261023_id1_Chetumal      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos 
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261030_id1_mahahual      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos
|     |      |--- gases.csv          # ------> Datos de los sensores de bases  
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261030_id2_mahahual      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos
|     |      |--- gases.csv          # ------> Datos de los sensores de bases  
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261030_id3_mahahual      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos
|     |      |--- gases.csv          # ------> Datos de los sensores de bases  
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261103_id1_mahahual      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos
|     |      |--- gases.csv          # ------> Datos de los sensores de bases  
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261103_id2_mahahual      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos
|     |      |--- gases.csv          # ------> Datos de los sensores de bases  
|     |      |--- metadata.txt       # ------> Metadatos
|     |--- 20261103_id3_mahahual      # Carpeta de almacenamiento de datos
|     |      |--- data.csv           # ------> Datos de los sensores metereologicos
|     |      |--- gases.csv          # ------> Datos de los sensores de bases  
|     |      |--- metadata.txt       # ------> Metadatos

|--- src/                           # Contiene el codigo fuente del núcle del pipeline
|     |--- meteo_data_pipeline/
|          |--- __init.py
|          |--- main.py            # Script principal 
|--- pyproject.toml                 # Configuración del proyecto y dependencias de uv 
|--- uv.lock                        # Bloqueo de versiones de dependencias 
|--- README.md                      # Documentación del proyecto
```