# **Pipeline de los datos generados por las estaciones metereológicas**


Pipeline automatizado en Python para la unión de bases de dato provenientes de 3 estaciones meteorológicas de monitoreo. Este proyecto está gestionado mediante **uv** para garantizar un control de entornos virtuales eficiente y reproducibles. Se diseñó para agilizar la unión de los datos generados por cada estacion metereológica en un solo archivo. Uno de sus principales utilidades es cambiar el nombre de las variables originales que contienen caracteres especiales por nombres identificadores nombrados por el equipo de investigación. Además crea un metadato donde se describe cada una de las variables. 

## El proyecto se estructura de la siguiente manera
```text
meteo_data_pipeline/
|
|---.venv/                          # Entorno virtual gestionado por uv 
|--- data/                          # Almacenamiento de resultados y metadatos 
|     |--- 2026-10-07_Chetumal.csv  # Archivo csv final
|     |--- metadato_. . ._Chetumal.txt #Diccionario de metadatos
|--- src/                           # Contiene el codigo fuente del núcle del pipeline
|     |--- meteo_data_pipeline/
|          |--- __init.py
|          |--- tools.py            # Funciones utilizadas como herramientas de preprocesamiento
|--- pyproject.toml                 # Configuración del proyecto y dependencias de uv 
|--- uv.lock                        # Bloqueo de versiones de dependencias 
|--- main.py                        # Script principal 
|--- README.md                      # Documentación del proyecto
```