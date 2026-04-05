from models.Music import music
from structures.BST import BST
from services.lecture_dataset import get_musics_main

def main():

    # Carregar o dataset

    musics = get_musics_main() 

    # Criar a árvore binária de busca e inserir as músicas
    tree = BST(None)

    for music_data in musics:
        music_obj = music(*music_data)
        tree.insert(music_obj)
    
    if tree.root is None:
        print("A árvore está vazia.")
    else:
        print("Busca por música (nome):")
        input_name = input("Digite o nome da música: ")
        found_music = tree.search_music(input_name)
        if found_music is not None:
            print(found_music)
        else:
            print("Música não encontrada.")

        print("\nBusca por música (nome + artista):")
        input_neme_artist = input("Digite o nome da música e o artista (separados por vírgula): ")
        found_music_with_artist = tree.search_music(*map(str.strip, input_neme_artist.split(",")))
        if found_music_with_artist is not None:
            print(found_music_with_artist)
        else:
            print("Música com esse artista não encontrada.")

        print("\nBusca por artista:")
        input_artist = input("Digite o nome do artista: ")
        artist_musics = tree.search_by_artist(input_artist)
        print(f"Total encontrado para artista: {len(artist_musics)}")
        for item in artist_musics[:5]:
            print(f"- {item.name} ({item.year})")

if __name__ == "__main__":
    main()
    