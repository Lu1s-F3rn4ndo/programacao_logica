# 1
base_conhecimento = {
    "Joao": 25,
    "Maria": 40,
    "Pedro": 33,
    "Ana": 29,
    "Carlos": 45,
    "Mariana": 31,
    "Jose": 28,
    "Lucia": 37,
    "Felipe": 22,
    "Beatriz": 42
}

pessoas_mais_de_30 = [nome for nome, idade in base_conhecimento.items() if idade > 30]

print("Pessoas com mais de 30 anos:")
for pessoa in pessoas_mais_30:
    print(pessoa)
#######################################################################
# 2
base_conhecimento_cores_objetos = {
    "vermelho": "maçaa",
    "azul": "ceu",
    "verde": "grama",
    "amarelo": "sol",
    "roxo": "uva",
    "laranja": "abobora",
    "rosa": "flor",
    "preto": "noite",
    "branco": "neve",
    "marrom": "terra"
}

cor_verde_associada = "verde" in base_conhecimento_cores_objetos.keys()

if cor_verde_associada:
    objeto_associado_verde = base_conhecimento_cores_objetos["verde"]
    print(f"A cor verde está associada ao objeto: {objeto_associado_verde}")
else:
    print("A cor verde não está associada a nenhum objeto na base de conhecimento.")

#######################################################################
# 3
base_conhecimento_cidades_paises = {
    "Paris": "Franca",
    "Londres": "Reino Unido",
    "Berlim": "Alemanha",
    "Roma": "Italia",
    "Madrid": "Espanha",
    "Toquio": "Japao",
    "Pequim": "China",
    "Moscou": "Russia",
    "Cairo": "Egito",
    "Nova York": "Estados Unidos"
}

def encontrar_cidades_por_pais(pais_procurado, base_conhecimento):
    cidades_no_pais = [cidade for cidade, pais in base_conhecimento.items() if pais == pais_procurado]
    return cidades_no_pais

pais_desejado = "França"

cidades_no_pais_desejado = encontrar_cidades_por_pais(pais_desejado, base_conhecimento_cidades_paises)

if cidades_no_pais_desejado:
    print(f"As cidades no país '{pais_desejado}' são: {', '.join(cidades_no_pais_desejado)}")
else:
    print(f"Não há informações sobre cidades no país '{pais_desejado}' na base de conhecimento.")

#######################################################################
# 4
base_conhecimento_produtos = {
    "Camiseta": {"preco": 25.0, "quantidade_estoque": 5},
    "Calca Jeans": {"preco": 50.0, "quantidade_estoque": 3},
    "Tenis": {"preco": 80.0, "quantidade_estoque": 0},
    "Bone": {"preco": 15.0, "quantidade_estoque": 10},
    "Meias": {"preco": 8.0, "quantidade_estoque": 0},
    "Moletom": {"preco": 45.0, "quantidade_estoque": 7},
    "Saia": {"preco": 30.0, "quantidade_estoque": 2},
    "Blusa": {"preco": 35.0, "quantidade_estoque": 4},
    "Jaqueta": {"preco": 70.0, "quantidade_estoque": 1},
    "Shorts": {"preco": 20.0, "quantidade_estoque": 6}
}

def verificar_produto_em_falta(produto, base_conhecimento):
    if produto in base_conhecimento:
        quantidade_estoque = base_conhecimento[produto]["quantidade_estoque"]
        return quantidade_estoque == 0
    else:
        return None  

produto_verificar = "Tenis"

esta_em_falta = verificar_produto_em_falta(produto_verificar, base_conhecimento_produtos)

if esta_em_falta is not None:
    if esta_em_falta:
        print(f"O produto '{produto_verificar}' está em falta.")
    else:
        print(f"O produto '{produto_verificar}' não está em falta.")
else:
    print(f"O produto '{produto_verificar}' não foi encontrado na base de conhecimento.")

#######################################################################
# 5
base_conhecimento_musicas = {
    "Bohemian Rhapsody": "Rock",
    "Shape of You": "Pop",
    "Smells Like Teen Spirit": "Rock",
    "Billie Jean": "Pop",
    "Stairway to Heaven": "Rock",
    "Uptown Funk": "Funk",
    "November Rain": "Rock",
    "Wonderwall": "Rock",
    "Back in black": "Rock",
    "Thriller": "Pop"
}

def listar_musicas_por_genero(genero, base_conhecimento):
    musicas_do_genero = [musica for musica, gen in base_conhecimento.items() if gen == genero]
    return musicas_do_genero

genero_desejado = "Rock"

musicas_do_genero_desejado = listar_musicas_por_genero(genero_desejado, base_conhecimento_musicas)

if musicas_do_genero_desejado:
    print(f"As musicas do genero '{genero_desejado}' sao:")
    for musica in musicas_do_genero_desejado:
        print(musica)
else:
    print(f"Nao ha informações sobre musicas do genero '{genero_desejado}' na base de conhecimento.")

#######################################################################
# 6
base_conhecimento_animais = {
    "Leao": "Mamifero",
    "Girafa": "Mamifero",
    "Tigre": "Mamifero",
    "Pinguim": "Ave",
    "Aguia": "Ave",
    "Baleia": "Mamífero",
    "Tubarao": "Peixe",
    "Elefante": "Mamifero",
    "Cobra": "Reptil",
    "Crocodilo": "Reptil"
}

def encontrar_animais_por_especie(especie, base_conhecimento):
    animais_da_especie = [animal for animal, esp in base_conhecimento.items() if esp == especie]
    return animais_da_especie

especie_desejada = "Mamifero"

animais_da_especie_desejada = encontrar_animais_por_especie(especie_desejada, base_conhecimento_animais)

if animais_da_especie_desejada:
    print(f"Os animais da espécie '{especie_desejada}' sao:")
    for animal in animais_da_especie_desejada:
        print(animal)
else:
    print(f"Nao ha informaçoes sobre animais da especie '{especie_desejada}' na base de conhecimento.")

#######################################################################
# 7
base_conhecimento_alunos = {
    "Alice": 7.5,
    "Luis": 4.8,
    "Carol": 6.8,
    "Daniel": 3.2,
    "Ana": 5.5,
    "Fernando": 9.0,
    "Maria": 2.5,
    "Hugo": 6.0,
    "Isabela": 4.7,
    "Joao": 8.3
}

def verificar_aprovacao_aluno(aluno, base_conhecimento):
    if aluno in base_conhecimento:
        nota_aluno = base_conhecimento[aluno]
        return nota_aluno >= 5.0
    else:
        return None  

aluno_verificar = "Alice"

aprovado = verificar_aprovacao_aluno(aluno_verificar, base_conhecimento_alunos)

if aprovado is not None:
    if aprovado:
        print(f"O aluno '{aluno_verificar}' foi aprovado na disciplina.")
    else:
        print(f"O aluno '{aluno_verificar}' foi reprovado na disciplina.")
else:
    print(f"O aluno '{aluno_verificar}' nao foi encontrado na base de conhecimento.")

#######################################################################
# 8
base_conhecimento_distancias = {
    "Cidade_A": {"Cidade_B": 50, "Cidade_C": 30, "Cidade_D": 80, "Cidade_E": 120},
    "Cidade_B": {"Cidade_A": 50, "Cidade_C": 40, "Cidade_D": 90, "Cidade_E": 100},
    "Cidade_C": {"Cidade_A": 30, "Cidade_B": 40, "Cidade_D": 60, "Cidade_E": 70},
    "Cidade_D": {"Cidade_A": 80, "Cidade_B": 90, "Cidade_C": 60, "Cidade_E": 110},
    "Cidade_E": {"Cidade_A": 120, "Cidade_B": 100, "Cidade_C": 70, "Cidade_D": 110}
}

def encontrar_cidade_mais_proxima(cidade_origem, base_conhecimento):
    distancias_da_cidade = base_conhecimento[cidade_origem]
    cidade_mais_proxima = min(distancias_da_cidade, key=distancias_da_cidade.get)
    return cidade_mais_proxima

cidade_origem_especificada = "Cidade_A"

cidade_mais_proxima = encontrar_cidade_mais_proxima(cidade_origem_especificada, base_conhecimento_distancias)

print(f"A cidade mais proxima de '{cidade_origem_especificada}' e '{cidade_mais_proxima}'.")

#######################################################################
# 9
base_conhecimento_paises = {
    "Brasil": {"Capital": "Brasilia", "Linguas": ["Portugues"]},
    "Estados Unidos": {"Capital": "Washington, D.C.", "Linguas": ["Ingles"]},
    "França": {"Capital": "Paris", "Linguas": ["Frances"]},
    "Espanha": {"Capital": "Madri", "Linguas": ["Espanhol"]},
    "Alemanha": {"Capital": "Berlim", "Linguas": ["Alemao"]},
    "Japao": {"Capital": "Toquio", "Linguas": ["Japonês"]},
    "China": {"Capital": "Pequim", "Linguas": ["Mandarim"]},
    "India": {"Capital": "Nova Delhi", "Linguas": ["Hindi"]},
    "Russia": {"Capital": "Moscou", "Linguas": ["Russo"]},
    "Itália": {"Capital": "Roma", "Linguas": ["Italiano"]}
}

def encontrar_paises_por_lingua(lingua, base_conhecimento):
    paises_com_lingua = [pais for pais, info in base_conhecimento.items() if lingua in info["Linguas"]]
    return paises_com_lingua

lingua_especifica = "Ingles"

paises_com_lingua_especifica = encontrar_paises_por_lingua(lingua_especifica, base_conhecimento_paises)

if paises_com_lingua_especifica:
    print(f"Os paises onde se fala '{lingua_especifica}' sao:")
    for pais in paises_com_lingua_especifica:
        print(pais)
else:
    print(f"Nenhum pais foi encontrado onde se fala '{lingua_especifica}' na base de conhecimento.")

#######################################################################
# 10
base_conhecimento_receitas = {
    "Farinha": ["Bolo de Chocolate", "Pao", "Panqueca"],
    "Leite": ["Bolo de Chocolate", "Cafe com Leite", "Panqueca"],
    "Ovos": ["Bolo de Chocolate", "Pao", "Omelete"],
    "Açucar": ["Bolo de Chocolate", "Cha Gelado", "Sobremesa de Frutas"],
    "Chocolate": ["Bolo de Chocolate", "Sorvete de Chocolate", "Mousse"],
    "Tomate": ["Molho de Tomate", "Salada", "Sopa"],
    "Queijo": ["Pizza", "Sanduiche", "Lasanha"],
    "Peixe": ["Sushi", "Ceviche", "Peixe Grelhado"],
    "Arroz": ["Arroz de Forno", "Sushi", "Risoto"],
    "Cebola": ["Molho de Tomate", "Sopa", "Guacamole"]
}

def listar_receitas_por_ingrediente(ingrediente, base_conhecimento):
    receitas_com_ingrediente = [receita for ing, receitas in base_conhecimento.items() if ing == ingrediente for receita in receitas]
    return receitas_com_ingrediente

ingrediente_especifico = "Chocolate"

receitas_com_ingrediente_especifico = listar_receitas_por_ingrediente(ingrediente_especifico, base_conhecimento_receitas)

if receitas_com_ingrediente_especifico:
    print(f"As receitas que contem '{ingrediente_especifico}' sao:")
    for receita in receitas_com_ingrediente_especifico:
        print(receita)
else:
    print(f"Nenhuma receita foi encontrada que contenha '{ingrediente_especifico}' na base de conhecimento.")
