
categorias = [ "Profissão", "Fruta", "Animal", "País", "Objeto", "Cidade" ]

import random
import string

jogar = "a"

while jogar == "a":

    erros = 0
    letras_escolhidas = []
    categoria = random.choice(categorias)

    def escolha_pal(nome, max_):
        global palavra
        global palavra_escondida
        global letras
        with open(nome, 'r') as f:
            linha = f.readlines()
            numero = random.randint(0, max_)
            palavra_escondida = linha[numero]
            letras = len(palavra_escondida) - 1
            palavra = "_ " * letras
        
    if categoria == "Profissão":
        escolha_pal("Profissões.txt", 135)

    elif categoria == "Fruta":
        escolha_pal("Frutas.txt", 33)
        
    elif categoria == "Animal":
        escolha_pal("Animais.txt", 139)

    elif categoria == "País":
        escolha_pal("Países.txt", 39)

    elif categoria == "Cidade":
        escolha_pal("Cidades.txt", 43)

    elif categoria == "Objeto":
        escolha_pal("Objetos.txt", 162)
 
    def info():
        print("Categoria: ", categoria)
        print("Erros: ", erros)
        print("Letras Escolhidas: ", letras_escolhidas)
        print("")
        print(palavra)

    def str_to_list(string):
        pal_list = list(string.split(" "))
        return pal_list

    def list_to_str(s):
        str1 = " "
        return(str1.join(s))

    list_ = str_to_list(palavra)


    while (erros < 6) and ("_ " in palavra):
        info()
        user_letra = str(input("Escolha uma letra: "))
        letras_escolhidas.append(user_letra)
        if user_letra not in palavra_escondida:
            erros += 1
        else:
            for c in range(0, letras):
                if palavra_escondida[c] == user_letra:
                    list_[c] = user_letra
                elif palavra_escondida[c] == "":
                    list_[c] = ""
        
        palavra = list_to_str(list_)
        print("")
        print("")
        
    if erros == 6:
        print("Perdeste! :( A palavra era:", palavra_escondida)
    else:
        print("Parabéns! Acertaste! :) Palavra:", palavra_escondida)

    erros = 0    
    msg = "Prima (a) para jogar novamente, (s) para sugerir uma palavra, (e) para reportar um erro, outra tecla para terminar"
    print(msg)
    jogar = input()

    while (jogar == "s") or (jogar == "e"):

        if jogar == "s":
            with open("Sugestões.txt", 'a') as f:
                sugestao = input("Sugestão de palavra (palavras sem acentos e sem espaços): ")
                f.write(sugestao)
                f.write(" | ")
                
        
        elif jogar == "e":
            with open("Erros.txt", 'a') as f:
                erro = input("Erro (palavra mal escrita ou bugs no jogo): ")
                f.write(erro)
                f.write(" | ")
                
        
        print(msg)
        jogar = input()





    

