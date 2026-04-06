class Node:

    # Inicializa um nó com valor e filhos vazios.
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    
    # Cria a árvore com ou sem nó raiz inicial.
    def __init__(self, value):

        if value is not None:
            self.root = Node(value)
        else:
            self.root = None

    # Insere um novo valor na árvore.
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)

    # Monta a chave de ordenação usando nome e artista.
    def _build_key(self, name, artist):
        return (name.casefold().strip(), artist.casefold().strip())

    # Retorna a chave de ordenação de uma música.
    def _get_music_key(self, value):
        return self._build_key(value.name, value.artist)

    # Insere recursivamente o valor na posição correta da árvore.
    def _insert_recursively(self, current_Node, value):
        if self._get_music_key(value) < self._get_music_key(current_Node.value):
            if current_Node.left is None:
                current_Node.left = Node(value)
            else:
                self._insert_recursively(current_Node.left, value)
        else:
            if current_Node.right is None:
                current_Node.right = Node(value)
            else:
                self._insert_recursively(current_Node.right, value)

    # Função para buscar por nome e, opcionalmente, artista em modo exato.
    def search_music(self, name, artist=None):
        results = []

        if self.root is None:
            return results

        name = name.casefold().strip()
        artist = artist.casefold().strip() if artist is not None else None

        if artist is not None:
            found = self._search_exact_music(self.root, self._build_key(name, artist))
            return [found] if found is not None else []

        self._collect_exact_name(self.root, name, results)
        return results

    # Busca exatamente uma música pela chave nome + artista.
    def _search_exact_music(self, current_Node, key):
        if current_Node is None:
            return None

        current_key = self._get_music_key(current_Node.value)

        if key == current_key:
            return current_Node.value
        if key < current_key:
            return self._search_exact_music(current_Node.left, key)
        return self._search_exact_music(current_Node.right, key)

    # Coleta recursivamente músicas com nome exatamente igual, com poda pela ordenação.
    def _collect_exact_name(self, current_Node, name, results):
        if current_Node is None:
            return

        current_name = current_Node.value.name.casefold().strip()

        if name < current_name:
            self._collect_exact_name(current_Node.left, name, results)
            return

        if name > current_name:
            self._collect_exact_name(current_Node.right, name, results)
            return

        results.append(current_Node.value)
        self._collect_exact_name(current_Node.left, name, results)
        self._collect_exact_name(current_Node.right, name, results)

    # Retorna todas as músicas com o mesmo nome.
    def search_musics_by_name(self, name):
        results = []
        self._collect_by_name(self.root, name.casefold().strip(), results)
        return results

    # Coleta recursivamente todas as músicas com o nome informado.
    def _collect_by_name(self, current_Node, name, results):
        if current_Node is None:
            return

        current_name = current_Node.value.name.casefold().strip()


        self._collect_by_name(current_Node.left, name, results)

        if name == current_name:
            results.append(current_Node.value)

        self._collect_by_name(current_Node.right, name, results)

    # Retorna todas as músicas de um artista em modo exato.
    def search_by_artist(self, artist):
        results = []
        self._collect_by_artist(self.root, artist.casefold().strip(), results)
        return results

    # Coleta recursivamente todas as músicas do artista informado.
    def _collect_by_artist(self, current_Node, artist, results):
        if current_Node is None:
            return

        self._collect_by_artist(current_Node.left, artist, results)

        current_artist = current_Node.value.artist.casefold().strip()
        if current_artist == artist:
            results.append(current_Node.value)

        self._collect_by_artist(current_Node.right, artist, results)