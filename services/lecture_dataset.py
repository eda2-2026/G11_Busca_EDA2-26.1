import pandas as pd
import numpy as np


# Carregar o dataset

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        if "Unnamed: 0" in df.columns:
            df = df.drop(columns=["Unnamed: 0"])
        return df
    except Exception as e:
        print(f"Erro ao carregar o dataset: {e}")
        return None

# Função que devolve uma lista de tuplas (id, nome, artista, genero, ano ) a partir do dataset

def get_music_list(df):

    music_list = []
    for index, row in enumerate(df.iterrows(), start=1):
        _, music_row = row
        music_list.append((index, music_row['track_name'], music_row['artist_name'], music_row['genre'], music_row['release_date']))
    return music_list

def get_music_dict(df):

    music_dict = {}
    for index, row in enumerate(df.iterrows(), start=1):
        _, music_row = row
        music_dict[index] = (music_row['track_name'], music_row['artist_name'], music_row['genre'], music_row['release_date'])
    return music_dict


def get_musics_main():
    file_path = './assets/tcc_ceds_music.csv'
    df = load_dataset(file_path)
    if df is not None:
        music_list = get_music_list(df)
        return music_list

    return []