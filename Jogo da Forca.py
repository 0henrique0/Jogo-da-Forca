
categorias = [ "Profissão", "Fruta", "Animal", "País", "Objeto", "Cidade" ]

import random
import string

jogar = "s"

while jogar == "s":

    erros = 0
    letras_escolhidas = []
    categoria = random.choice(categorias)

    def escolha_pal():
        global palavra
        global palavra_escondida
        global letras
        f = open(nome, 'r')
        linha = f.readlines()
        numero = random.randint(0, max_)
        palavra_escondida = linha[numero]
        letras = len(palavra_escondida) - 1
        palavra = "_ " * letras
        
    if categoria == "Profissão":
        nome = 'Profissões.txt'
        max_ = 135
        escolha_pal()

    elif categoria == "Fruta":
        nome = "Frutas.txt"
        max_ = 33
        escolha_pal()
        
    elif categoria == "Animal":
        nome = "Animais.txt"
        max_ = 139
        escolha_pal()

    elif categoria == "País":
        nome = "Países.txt"
        max_ = 39
        escolha_pal()

    elif categoria == "Cidade":
        nome = "Cidades.txt"
        max_ = 43
        escolha_pal()

    elif categoria == "Objeto":
        nome = "Objetos.txt"
        max_ = 162
        escolha_pal()
 
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
    print("Prima (s) para jogar novamente, outra tecla para terminar")
    jogar = input()






    

