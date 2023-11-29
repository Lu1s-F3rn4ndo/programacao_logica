# 1
% Base de conhecimento com nomes e idades de 10 pessoas
pessoa(joao, 25).
pessoa(maria, 35).
pessoa(ana, 28).
pessoa(pedro, 40).
pessoa(carla, 31).
pessoa(lucas, 22).
pessoa(beatriz, 30).
pessoa(marcos, 45).
pessoa(sara, 29).
pessoa(fernando, 33).

mais_de_30_anos(Nome) :-
    pessoa(Nome, Idade),
    Idade > 30.

?- mais_de_30_anos(Pessoa).

?- mais_de_30_anos(Pessoa).

#######################################################################
# 2
cor_objeto(vermelho, maca).
cor_objeto(azul, caneta).
cor_objeto(verde, caderno).
cor_objeto(amarelo, lápis).
cor_objeto(rosa, bloco_de_notas).
cor_objeto(roxo, carteira).
cor_objeto(preto, celular).
cor_objeto(branco, livro).
cor_objeto(laranja, caneca).
cor_objeto(marrom, chaveiro).

cor_associada_a_objeto(Cor) :-
    cor_objeto(Cor, _).

verde_associado_a_objeto :-
    cor_objeto(verde, Objeto),
    write('Verde está associado ao objeto: '), write(Objeto), nl.

?- verde_associado_a_objeto.

#######################################################################
# 3
cidade_pais(paris, franca).
cidade_pais(londres, reino_unido).
cidade_pais(nova_york, estados_unidos).
cidade_pais(tokyo, japao).
cidade_pais(roma, italia).
cidade_pais(sydney, australia).
cidade_pais(dubai, emirados_arabes).
cidade_pais(berlim, alemanha).
cidade_pais(cairo, egito).
cidade_pais(moscou, russia).

cidades_no_pais(Pais, ListaDeCidades) :-
    findall(Cidade, cidade_pais(Cidade, Pais), ListaDeCidades).

?- cidades_no_pais(franca, CidadesNaFranca).

#######################################################################
# 4
produto_estoque(teclado, 30, 5).
produto_estoque(monitor, 150, 3).
produto_estoque(mouse, 15, 0).
produto_estoque(headset, 40, 8).
produto_estoque(pendrive, 10, 2).
produto_estoque(cartao_memoria, 20, 0).
produto_estoque(celular, 300, 4).
produto_estoque(tablet, 200, 0).
produto_estoque(caixa_som, 50, 6).
produto_estoque(câmera, 250, 1).

produto_em_falta(Produto) :-
    produto_estoque(Produto, _, Quantidade),
    Quantidade =:= 0.

?- produto_em_falta(mouse).

#######################################################################
# 5
musica_genero(stairway_to_heaven, rock).
musica_genero(bohemian_rhapsody, rock).
musica_genero(yesterday, pop).
musica_genero(billie_jean, pop).
musica_genero(smells_like_teen_spirit, grunge).
musica_genero(black_hole_sun, grunge).
musica_genero(uptown_funk, funk).
musica_genero(superstition, funk).
musica_genero(shape_of_my_heart, pop).
musica_genero(hotel_california, rock).

musicas_do_genero(Genero, ListaDeMusicas) :-
    findall(Musica, musica_genero(Musica, Genero), ListaDeMusicas).

?- musicas_do_genero(pop, MusicasPop).

#######################################################################
# 6
animal_especie(leao, mamifero).
animal_especie(tigre, mamifero).
animal_especie(girafa, mamifero).
animal_especie(zebra, mamifero).
animal_especie(papagaio, ave).
animal_especie(coruja, ave).
animal_especie(tartaruga, reptil).
animal_especie(cobra, reptil).
animal_especie(sapo, anfibio).
animal_especie(salamandra, anfibio).

animais_da_especie(Especie, ListaDeAnimais) :-
    findall(Animal, animal_especie(Animal, Especie), ListaDeAnimais).

?- animais_da_especie(mamifero, Mamiferos).

#######################################################################
# 7
nota_aluno(alice, 7.5).
nota_aluno(bob, 6).
nota_aluno(carla, 4.5).
nota_aluno(david, 8).
nota_aluno(elena, 3).
nota_aluno(felipe, 5.5).
nota_aluno(gabriela, 9).
nota_aluno(henrique, 2).
nota_aluno(isabela, 6.5).
nota_aluno(joao, 4).

aprovado_aluno(Aluno) :-
    nota_aluno(Aluno, Nota),
    Nota >= 5.

?- aprovado_aluno(alice).

#######################################################################
# 8
distancia(cidade_a, cidade_b, 50).
distancia(cidade_a, cidade_c, 80).
distancia(cidade_a, cidade_d, 120).
distancia(cidade_b, cidade_c, 40).
distancia(cidade_b, cidade_d, 90).
distancia(cidade_c, cidade_d, 60).

cidade_mais_proxima(CidadeOrigem, CidadeMaisProxima, Distancia) :-
    findall(Dist, distancia(CidadeOrigem, _, Dist), Distancias),
    min_list(Distancias, Distancia),
    distancia(CidadeOrigem, CidadeMaisProxima, Distancia).

?- cidade_mais_proxima(cidade_a, CidadeMaisProxima, DistanciaMaisProxima).

#######################################################################
# 9
lingua_oficial(brasil, portugues).
lingua_oficial(eua, ingles).
lingua_oficial(canada, ingles).
lingua_oficial(franca, frances).
lingua_oficial(alemanha, alemao).
lingua_oficial(espanha, espanhol).
lingua_oficial(italia, italiano).
lingua_oficial(japao, japones).
lingua_oficial(china, mandarim).
lingua_oficial(india, hindi).

paises_com_lingua(Lingua, ListaDePaises) :-
    findall(Pais, lingua_oficial(Pais, Lingua), ListaDePaises).

?- paises_com_lingua(ingles, PaisesComIngles).

#######################################################################
# 10
receita(omelete, [ovos, queijo, tomate, cebola]).
receita(macarrao, [macarrao, molho_de_tomate, queijo_ralado]).
receita(salada, [alface, tomate, cenoura, cebola, azeite, vinagre]).
receita(bolo_de_chocolate, [farinha_de_trigo, ovos, chocolate, acucar, leite]).
receita(sopa_de_legumes, [cenoura, batata, abobrinha, cebola, alho, caldo_de_legumes]).
receita(torta_de_frango, [frango, massa_de_torta, creme_de_leite, milho, ervilha]).
receita(pure_de_batatas, [batata, leite, manteiga]).
receita(mousse_de_limao, [leite_condensado, creme_de_leite, suco_de_limao]).
receita(picanha_assada, [picanha, sal_grosso, alho, alecrim]).
receita(risoto_de_cogumelos, [arroz, cogumelos, cebola, caldo_de_legumes]).

receitas_com_ingrediente(Ingrediente, ListaDeReceitas) :-
    findall(Receita, (receita(Receita, Ingredientes), member(Ingrediente, Ingredientes)), ListaDeReceitas).

?- receitas_com_ingrediente(tomate, ReceitasComTomate).
