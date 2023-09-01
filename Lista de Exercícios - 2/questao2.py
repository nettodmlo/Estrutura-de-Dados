# 2. Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método 
# chamado “detalhes” que retorna uma string com as informações do livro.

class Livro:
    def detalhes(titulo, autor):
        print(f"Livro com titulo de {titulo}, escritor por {autor}")

livro1 = Livro
livro1.detalhes("E o vento levou", "Paulo Renan")