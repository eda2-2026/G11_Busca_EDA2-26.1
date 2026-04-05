import streamlit as st
from models.Music import music
from structures.BST import BST
from services.lecture_dataset import get_musics_main

# -------------------------------
# 1. CARREGAR E CONSTRUIR A ÁRVORE
# -------------------------------

@st.cache_resource
def load_tree():
    musics = get_musics_main()
    tree = BST(None)

    for music_data in musics:
        music_obj = music(*music_data)
        tree.insert(music_obj)

    return tree

tree = load_tree()

# -------------------------------
# 2. INTERFACE
# -------------------------------

st.title("🎵 Sistema de Busca de Músicas com BST")

search_type = st.selectbox(
    "Selecione o tipo de busca:",
    ["Nome da Música", "Nome da Música + Artista", "Artista"]
)

input_value = st.text_input("Digite sua busca:")

# -------------------------------
# 3. EXECUTAR BUSCA
# -------------------------------

if st.button("Buscar"):

    if not input_value:
        st.warning("Digite um valor para buscar.")

    else:
        # -----------------------
        # Busca por Nome da Música
        # -----------------------
        if search_type == "Nome da Música":
            result = tree.search_music(input_value)

            if result:
                st.success(f"{len(result)} músicas encontradas")
                for item in result[:10]:
                    st.write(f"🎵 Nome: {item.name} || Artista/Grupo: {item.artist} || Ano: {item.year} || Gênero:{item.genre}")
            else:
                st.error("Música não encontrada.")

        # -----------------------
        # Nome da Música + artista
        # -----------------------
        elif search_type == "Nome da Música + Artista":
            try:
                name, artist = map(str.strip, input_value.split(","))
                result = tree.search_music(name, artist)

                if result:
                    st.success(f"{len(result)} músicas encontradas")
                    for item in result[:10]:
                        st.write(f"🎵 Nome: {item.name} || Artista/Grupo: {item.artist} || Ano: {item.year}")
                else:
                    st.error("Música não encontrada.")

            except:
                st.error("Formato inválido. Use: Nome, Artista")

        # -----------------------
        # Busca por artista
        # -----------------------
        elif search_type == "Artista":
            results = tree.search_by_artist(input_value)

            if results:
                st.success(f"{len(results)} músicas encontradas")
                
                for item in results[:10]:
                    st.write(f"🎵Nome: {item.name} || Artista/Grupo: {item.artist} || Ano: {item.year}")

            else:
                st.error("Nenhuma música encontrada.")