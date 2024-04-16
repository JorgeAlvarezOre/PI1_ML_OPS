from fastapi.responses import JSONResponse
from fastapi import FastAPI
import pandas as pd
import numpy as np  
from sklearn.utils.extmath           import randomized_svd
from sklearn.metrics.pairwise        import cosine_similarity
from sklearn.metrics.pairwise        import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
#import json
from collections import defaultdict

# columnstouse=['item_id','playtime_forever','user_id']
df_steam_games = pd.read_parquet("df_steam_games_cleaned.parquet")
df_user_items = pd.read_parquet("df_user_items_cleaned.parquet") # columns=columnstouse
df_user_reviews = pd.read_parquet("df_user_reviews_cleaned.parquet")

df_SteamGames = df_steam_games
df_UserItems = df_user_items
df_UserReviews = df_user_reviews


app=FastAPI()

#http://127.0.0.1:8000

@app.get("/")
def index():
    return "Hola, bienvenido(a) a mi proyecto"

@app.get('/desarrolladora/{desarrollador}')
def developer(desarrollador:str):
    desarrollador=desarrollador
    desarrollador_lower = desarrollador.lower()
    df = df_SteamGames.loc[df_SteamGames['developer'] == f'{desarrollador_lower}'].sort_values('year')
    df=df.drop_duplicates()
    yearB = 0
    dict_años = defaultdict(list)  # Changed the dictionary value type to list
    items = 0
    items_free = 0
    for index, row in df.iterrows():
        year = row['year']
        price = row['price']
        if  year != yearB:
            items = 0  # Restablece la cuenta de elementos si es un nuevo año
            yearB = year
            items_free=0
              
        if price == 0.00:
            items_free+=1
            dict_años[year] = [items, f'{items_free}'] 
        else:
            items += 1
            dict_años[year] = [items, f'{items_free}']
    texto = ' Contenido Free (%)'

    df = pd.DataFrame(dict_años.values(), dict_años.keys()).rename(columns={0: 'Cantidad de Items', 1: f'{desarrollador}{texto}'})
    df[f'{desarrollador}{texto}'] = round((pd.to_numeric(df[f'{desarrollador}{texto}']) / df['Cantidad de Items']*100), 2)
    result = df.to_dict('index')
    return result

####
#Código necesario para el funcionamiento de la función userdata()
df_items_count = df_UserItems.groupby("user_id")['items_count'].mean().reset_index()
resultado = df_UserReviews[['user_id','recommend']]
df_user_recommend_ratio = resultado.groupby('user_id')['recommend'].mean().round(2).reset_index()
df_usuarios_items = df_UserItems.groupby('user_id')['item_id'].apply(list).reset_index()
game_id_to_price = df_SteamGames.set_index('item_id')['price'].to_dict()
df_usuarios_items['total_spent'] = df_usuarios_items['item_id'].apply(lambda items: sum(game_id_to_price.get(item, 0) for item in items))
df_gasto = df_usuarios_items.drop('item_id', axis=1)
lista = [df_gasto, df_user_recommend_ratio]
temp = df_items_count
for i in range(len(lista)):
    df_user_data = pd.merge(temp,lista[i], on='user_id', how='outer')
    temp = df_user_data
df_user_data.loc[:, 'recommend'] = df_user_data['recommend'] * 100
df_user_data.rename(columns={'recommend': 'recommend_ratio'})
###

@app.get('/datos_por_usuario/{user_id}')
def userdata(user_id:str):
    df = df_user_data.loc[df_user_data['user_id'] == f'{user_id}']
    #df.loc[:, 'recommend'] = df['recommend']
    #df = df.rename(columns={'user_id': 'Usuario', 'recommend': '% de recomendación',
    #             'items_count': 'Cantidad de items', 'total_spent':'Dinero gastado'})
    result = {'Usuario': df["user_id"].iloc[0], 'Dinero gastado': round(df["total_spent"].iloc[0],2),
              '% de recomendación': df["recommend"].iloc[0], 'Cantidad de items': df["items_count"].iloc[0]}
    return result

@app.get('/usuario_por_genero/{genero}')
def UserForGenre(genero:str):
    # Se crea un nuevo DataFrame llamado df_games que contiene solo las columnas relevantes
    game_columns = ['item_id', 'name', 'year', 'Indie', 'Action', 'Casual', 'Adventure', 'Strategy',
                    'Simulation', 'RPG', 'Free to Play', 'Early Access', 'Sports',
                    'Massively Multiplayer', 'Racing', 'Design &amp; Illustration', 'Utilities']
    df_games = df_SteamGames[game_columns]
    
    # Se hace un join entre df_games y df_UserItems utilizando 'item_id' como clave
    df_joined = pd.merge(df_games, df_UserItems[['item_id', 'playtime_forever','user_id']], on='item_id', how='inner')

    # Se filtra el DataFrame resultante para el género específico
    genre_df = df_joined[df_joined[genero] == 1]

    # Se agrupa por usuario y año, sumamos las horas jugadas y se encuentra el usuario con más horas jugadas para el género dado
    total_hours_by_user_and_year = genre_df.groupby(['user_id', 'year'])['playtime_forever'].sum()
    max_user = total_hours_by_user_and_year.groupby('user_id').sum().idxmax()

    # Se obtiene la lista de acumulación de horas jugadas por año para el usuario con más horas jugadas
    max_user_hours_by_year = total_hours_by_user_and_year.loc[max_user].reset_index()
    max_user_hours_list = [{"Año": int(row['year']), "Horas": row['playtime_forever']} for _, row in max_user_hours_by_year.iterrows()]

    # Se retorna el resultado en un formato específico
    result = {"Usuario con más horas jugadas para Género {}".format(genero): max_user, "Horas jugadas": max_user_hours_list}
    return result

@app.get('/top3_desarrolladoras_por_año/{anho}')
def best_developer_year(anho:int):
    # Se filtra el DataFrame resultante para el año específico
    reduce_df = df_UserReviews[(df_UserReviews['year'] == anho) & 
                               (df_UserReviews['recommend'] == True) & 
                               (df_UserReviews['sentiment_analysis'].isin([2]))]
    
    # Se hace un join entre df_UserReviews y df_steamgames utilizando 'item_id' como clave
    merged_reviews = pd.merge(reduce_df, df_SteamGames[['item_id', 'name','developer']], on='item_id', how='left')
   
    # Se calcula la frecuencia de cada juego
    game_count = merged_reviews['developer'].value_counts()

    # Se selecciona el top 3 de juegos más recomendados, estos estan ordenados de mayor a menor por el value_counts
    top_3_best_games = game_count.head(3)

    result = [{"Puesto {}".format(i+1): developer} for i, (developer, _) in enumerate(top_3_best_games.items())]
    return result

@app.get('/Analisis_reseña_desarrollador/{desarrolladora}')
def developer_reviews_analysis(desarrolladora:str):
    # Se hace un join entre df_UserReviews y df_games utilizando 'item_id' como clave
    merged_reviews = pd.merge(df_UserReviews,df_SteamGames[['item_id','developer']], on='item_id', how='left')

    # Se filtra el DataFrame de reseñas por la desarrolladora específica
    reviews_by_developer = merged_reviews[merged_reviews['developer'] == desarrolladora.lower()]

    # Se realiza el análisis de sentimiento
    sentiment_counts = reviews_by_developer['sentiment_analysis'].value_counts()

    # Se crea el diccionario de resultado
    result = {desarrolladora: [
        f'Negative = {sentiment_counts.get(0, 0)}',
        f'Positive = {sentiment_counts.get(2, 0)}' 
    ]}
    return result
