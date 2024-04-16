# Proyecto Individual N° 1: Machine Learning Operations (MLOps)

Resolución del primer proyecto individual del BootCamp Data Science (dataft21) de Soy Henry

<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png" height=300><br>


## Introducción

Este trabajo explora de forma exhaustiva la función de un Ingeniero de Datos MLOps, abarcando las tres fases clave de: la Ingeniería de Datos, el Análisis y Procesamiento Exploratorio de Datos, y la Creación de Modelos utilizando Métodos de Aprendizaje Automático.

Durante la fase inicial, establecemos técnicas de Ingeniería de Datos para asegurar el acceso y análisis de los datos (ETL), creando consultas detalladas para extraer datos significativos.

La fase intermedia se dedica al Análisis Exploratorio de Datos (EDA), en el cual depuramos y examinamos los datos para su posterior uso en recomendaciones. Este proceso es vital para identificar cómo se relacionan las variables y para descubrir tendencias y desviaciones.

Finalmente, en la última fase, nos enfocamos en el corazón del proyecto: el Modelo de Recomendación de ML. Utilizamos algoritmos de aprendizaje automático para formular un sistema de recomendaciones para juegos en Steam, aplicando métodos para evaluar la similitud. Asimismo, creamos una API utilizando FastAPI para hacer accesibles los datos y elaboramos una serie de consultas interactivas, y finalmente se realiza un Deploy en el servicio de Render para que el modelo este disponible en la red para todos.

## Tareas Realizadas

### ETL

Ejecutamos un procedimiento de Extracción, Transformación y Carga (ETL), recolectando datos de múltiples fuentes, modificándolos para ajustarse a los requisitos del proyecto y almacenándolos en una ubicación designada. Empleamos tecnologías como Python, Pandas y TextBlob.

Se pueden revisar el código detallado en los notebooks 01_ETL_australian_user_reviews.ipynb , 02_ETL_australian_users_items.ipynb y 03_ETL_output_steam_games.ipynb .

### EDA

Realizamos un Análisis Exploratorio de Datos (EDA) para examinar interacciones y hallar tendencias. Recurrimos a herramientas como Numpy, Pandas, Matplotlib, Seaborn, Wordcloud, NLTK y scikit-learn.

Se pueden revisar el código detallado en el notebook 04_EDA.ipynb .

### Deployment de la API

Construimos una API utilizando FastAPI para hacer accesibles los datos, estableciendo consultas tales como developer, userdata, UserForGenre, best_developer_year, developer_reviews_analysis y recomendacion_juego. Implementamos soluciones como FastAPI, Uvicorn y Render.

Se pueden revisar el código de prueba y mejor documentado en los notebooks 05_Modelo_item.ipynb , 06_Funciones.ipynb , 07_CSV_to_PARQUET.ipynb y el deploy exacto en el archivo Python main.py .

## Modelo de Machine Learning

Desarrollamos un sistema de Aprendizaje Automático para ofrecer sugerencias de videojuegos. Empleamos métodos y algoritmos para examinar las tendencias en la información de usuarios y juegos, con el fin de entregar recomendaciones a medida. El sistema fue capacitado utilizando un conjunto de datos de 14000 registros.

Este proyecto demuestra un método completo que abarca desde el procesamiento inicial de los datos hasta la puesta en marcha de un sofisticado sistema de recomendaciones.

## Enlaces

Render: <https://pi1-ml-ops-5vx7.onrender.com/docs>

Video: 

