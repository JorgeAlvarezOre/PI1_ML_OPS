# Resumen de lo pedido
- Notebooks > FastAPI > Deploy > Markdown > Video
- Repositorio (con readme.md)

# Comandos
- conda create --name PI1 python==3.11 fastapi fastparquet nltk numpy pandas pyarrow scikit-learn uvicorn gdown langdetect
- conda activate tu_entorno
- conda env export > environment.yml
- conda env create -f environment.yml
- uvicorn main:app --reload
- uvicorn main:app --host 0.0.0.0 --port 10000
- http://127.0.0.1:8000/docs

# Falta
- Video API https://www.youtube.com/watch?v=12NIB_RjxMo
- Video FastAPI https://youtu.be/12NIB_RjxMo?si=FNSPdqWNayEZxd0j
- Estructura: EDA > ETL > API
- EDA con el notebook de StarFront

# Tests
**developer(desarrollador : str)**
Id Software		1990                  1                       0.0
Capcom			2008                  2                       0.00

**userdata(User_id : str)**
--ionex-- {'Usuario': '--ionex--', 'Dinero gastado': 109.92, '% de recomendación': 100.0, 'Cantidad de items': 23.0}
zzoptimuszz {'Usuario': 'zzoptimuszz', 'Dinero gastado': 4.99, '% de recomendación': 100.0, 'Cantidad de items': 61.0}

**UserForGenre(genero : str)**
Casual {'Usuario con más horas jugadas para Género Casual': 'REBAS_AS_F-T', 'Horas jugadas': [{'Año': 2001, 'Horas': 0.18}, {'Año': 2007, 'Horas': 7.1}, {'Año': 2008, 'Horas': 22.5}, {'Año': 2009, 'Horas': 124.79}, {'Año': 2010, 'Horas': 845.0699999999999}, {'Año': 2011, 'Horas': 691.41}, {'Año': 2012, 'Horas': 1278.84}, {'Año': 2013, 'Horas': 655.63}, {'Año': 2014, 'Horas': 1527.92}, {'Año': 2015, 'Horas': 4094.92}, {'Año': 2016, 'Horas': 5627.18}, {'Año': 2017, 'Horas': 38.67}]}
Free to Play {'Usuario con más horas jugadas para Género Free to Play': 'REBAS_AS_F-T', 'Horas jugadas': [{'Año': 2009, 'Horas': 12.07}, {'Año': 2010, 'Horas': 0.05}, {'Año': 2011, 'Horas': 72.07}, {'Año': 2012, 'Horas': 281.65999999999997}, {'Año': 2013, 'Horas': 246.98000000000002}, {'Año': 2014, 'Horas': 116.67999999999999}, {'Año': 2015, 'Horas': 2120.36}, {'Año': 2016, 'Horas': 1697.0}, {'Año': 2017, 'Horas': 0.97}]}

**best_developer_year(año : int)**
2015 [{'Puesto 1': 'valve'}, {'Puesto 2': 'facepunch studios'}, {'Puesto 3': 'smartly dressed games'}]
2013 [{'Puesto 1': 'valve'}, {'Puesto 2': 'facepunch studios'}, {'Puesto 3': 're-logic'}]

**developer_reviews_analysis(desarrolladora : str)**
Valve {'Valve': ['Negative = 914', 'Positive = 4703']}
Ubisoft {'ubisoft': ['Negative = 32', 'Positive = 61']}