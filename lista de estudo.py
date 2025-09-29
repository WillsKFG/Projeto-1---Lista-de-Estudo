#8. Conversão de Horas para Minutos: 
#Escreva um programa que solicite ao usuário uma quantidade de horas e 
#converta esse valor para minutos.
import os
def limpar_tela(): #Essa função irá limpar o terminal toda vez que for chamada
    os.system('cls' if os.name == 'nt' else 'clear')   

def inicio(): #Essa função é por onde qual lista de exercício irá ser feita
    limpar_tela()
    while True:
        print("\n\t ~ Listas de Exercício - Python ~\n")
        print("[1] - Lista I\n[2] - Lista II\n")
        try:
            escolha_lista = int(input("Escolha qual lista de exercícios você gostaria de ver: "))
            if escolha_lista == 1:
                menu_um()
            elif escolha_lista == 2:
                menu_dois()
            else:
                print("\nOpção Inválida, tente novamente.\n")
        except ValueError:
            print("\nDigite apenas números inteiros!!!\n")

def menu_um(): #Aqui é a função com o menu da primeira lista de exercício
    limpar_tela()
    while True:
        try:
            print('''
                ~ Lista de Exercício I - Segundo Semestre ~
            
            [1] - Cálculo Área Quadrado.
            [2] - Conversão de Temperatura
            [3] - Cálculo de IMC
            [4] - Operações Matemáticas Básicas
            [5] - Cálculo de Média
            [6] - Verificação PAR OU ÍMPAR
            [7] - Cálculo de Fatorial
            [8] - Conversão de Horas para Minutos
            
            [9] - Voltar ao menu anterior

            [0] - Sair do Programa
            ''')
        
            menu_escolha = int(input("Digite a opção desejada: ")) #aqui será por onde eu escolherei a opção desejada da lista 1
            if menu_escolha == 1:
                opcao_um_um()
            elif menu_escolha == 2:
                opcao_um_dois()
            elif menu_escolha == 3:
                opcao_um_tres()
            elif menu_escolha == 4:
                opcao_um_quatro()
            elif menu_escolha == 5:
                opcao_um_cinco()
            elif menu_escolha == 6:
                opcao_um_seis()
            elif menu_escolha == 7:
                opcao_um_sete()
            elif menu_escolha == 8:
                opcao_um_oito()
            elif menu_escolha == 9:
                inicio()
            elif menu_escolha == 0:
                print("\nFinalizando programa ...\n")
                quit()
            else:
                print("\nOpção Inválida, Tente Novamente\n")
        except ValueError:
            print("Digite um número inteiro!!! ")

def menu_dois(): #Aqui é a função com o menu da segunda lista de exercício #não começado
    limpar_tela()
    while True:
        try:
            print('''
        ~ Lista de Exercício II - Segundo Semestre ~
    
    [1] - Cálculo Área Retângulo
    [2] - Verificador Idade
    [3] - Cálculo de Desconto
    [4] - Sistema de Avaliação de notas
    [5] - Determinar maior de dois números
    [6] - Verificador Ano Bissexto
    [7] - Cálculo Média Ponderada
    [8] - Verificador de Login

    [9] - Voltar ao menu anterior
    
    [0] - Sair do Programa
    ''')
        
            menu_escolha = int(input("Digite a opção desejada: "))
            if menu_escolha == 1:
                opcao_um_um()
            elif menu_escolha == 2:
                opcao_um_dois()
            elif menu_escolha == 3:
                opcao_um_tres()
            elif menu_escolha == 4:
                opcao_um_quatro()
            elif menu_escolha == 5:
                opcao_um_cinco()
            elif menu_escolha == 6:
                opcao_um_seis()
            elif menu_escolha == 7:
                opcao_um_sete()
            elif menu_escolha == 8:
                opcao_um_oito()
            elif menu_escolha == 9:
                inicio()
            elif menu_escolha == 0:
                print("\nFinalizando programa ...\n")
                quit()
            else:
                print("\nOpção Inválida, Tente Novamente\n")
        except ValueError:
            print("Digite um número inteiro!!! ")

def opcao_um_um(): #Aqui está a primeira questão da primeira lista #concluída
    limpar_tela()

    print('''\t~ Cálculo da Área do Quadrado ~
        ''')
    print("Este programa irá calcular a área do quadrado")
    while True:
        try:
            lado = float(input("\nDigite o comprimento do lado do quadrado, em metros: "))
            area = lado**2
            perimetro = lado * 4
            print(f"O seu quadrado mede {area:.2f}m² e seu perímetro {perimetro:.2f}\n")
            break
        except ValueError:
            limpar_tela()
            print("\nValor inválido, Digite um número\n")

    while True:
            try:
                escolha_continuar = int(input("Deseja Continuar, Voltar a lista ou Finalizar o programa?\n[1] - Continuar\n[2] - Retornar a Lista\n[3] - Finalizar Programa\n\n-> "))
                if escolha_continuar == 1:
                    limpar_tela()
                    opcao_um_um()
                elif escolha_continuar == 2:
                    limpar_tela()
                    menu_um()
                elif escolha_continuar == 3:
                    print("\nFinalizando programa ...\n")
                    exit()
                else:
                    print("Opção Inválida, Tente Novamente")
            except ValueError:
                print("Insira uma entrada válida.")

def opcao_um_dois(): #Aqui está a segunda questão da primeira lista #concluída
    limpar_tela()

    print('''\t~ Conversão de Temperatura ~
Este programa pode converter temperaturas °C, °F e K''')

    while True:
        unidade_um = ""
        unidade_dois = ""
        try:
            escolha_um = int(input("\nDeseja Converter qual forma de medida?\n[1] - Celsius(°C)\n[2] - Fahrenheit (°K)\n[3] - Kelvin (K)\n\n --> "))
            if escolha_um == 1:
                unidade_um = "Celsius (°C)"
                break
            elif escolha_um == 2:
                unidade_um = "Fahrenheit (°F)"
                break
            elif escolha_um == 3:
                unidade_um = "Kelvin (K)"
                break
            else:
                print("\nValor Inválido, tente novamente\n")
                opcao_um_dois()
        except ValueError:
            limpar_tela()
            print("\nValor Inválido, Insira um número inteiro.\n")
    while True:
        try:
            valor_original = float(input(f"\nInsira seu valor em {unidade_um}: "))
            break
        except ValueError:
            limpar_tela()
            print("\nValor invalido, tente novamente\n")
    
    while True:
        try:
            escolha_dois = int(input("\nDeseja Converter o valor para qual forma de medida?\n[1] - Celsius(°C)\n[2] - Fahrenheit (°K)\n[3] - Kelvin (K)\n\n --> "))   
            if escolha_dois == 1:
                unidade_dois = "Celsius (°C)"
                break
            elif escolha_dois == 2:
                unidade_dois = "Fahrenheit (°F)"
                break
                
            elif escolha_dois == 3:
                unidade_dois = "Kelvin (K)"
                break
    
            else:
                print("\nValor Inválido, tente novamente\n")
                return
        except ValueError:
            print("\nValor inválido, digite um número inteiro\n")
         
    cel_fah = (valor_original * (9/5))+32
    cel_kel = (valor_original) + 273.15
    fah_cel = (valor_original - 32)/(9/5)
    fah_kel = (valor_original - 32) * 5/9 + 273.15
    kel_cel = valor_original - 273.15
    kel_fah = (valor_original - 273.15) * 9/5 + 32

    if unidade_um == "Celsius (°C)" and unidade_dois == "Fahrenheit (°F)":
        print(f"\n{valor_original:.2f}°C em Fahrenheit é {cel_fah:.2f}°F.\n")

    elif unidade_um == "Celsius (°C)" and unidade_dois == "Kelvin (K)":
        print(f"\n{valor_original:.2f}°C em Kelvin é {cel_kel:.2f}K.\n")
    
    elif unidade_um == "Fahrenheit (°F)" and unidade_dois == "Celsius (°C)":
        print(f"\n{valor_original:.2f}°F em Celsius é {fah_cel:.2f}°C.\n")

    elif unidade_um == "Fahrenheit (°F)" and unidade_dois == "Kelvin (K)":
        print(f"\n{valor_original:.2f}°F em Kelvin é {fah_kel:.2f}K.\n")

    elif unidade_um == "Kelvin (K)" and unidade_dois == "Celsius (°C)":
        print(f"\n{valor_original:.2f}K em Celsius é {kel_cel:.2f}°C.\n")
    
    elif unidade_um == "Kelvin (K)" and unidade_dois == "Fahrenheit (°F)":
        print(f"\n{valor_original:.2f}K em Fahrenheit é {kel_fah:.2f}°F.\n")

    elif unidade_um == unidade_dois:
        print(f'\nComo é a mesma unidade de medida, o produto continua medindo {valor_original:.2f}\n.')

    while True:
            try:
                escolha_continuar = int(input("Deseja Continuar, Voltar a lista ou Finalizar o programa?\n[1] - Continuar\n[2] - Retornar a Lista\n[3] - Finalizar Programa\n\n-> "))
                if escolha_continuar == 1:
                    limpar_tela()
                    opcao_um_dois()
                elif escolha_continuar == 2:
                    limpar_tela()
                    menu_um()
                elif escolha_continuar == 3:
                    print("\nFinalizando programa ...\n")
                    exit()
                else:
                    print("Opção Inválida, Tente Novamente")
            except ValueError:
                print("Insira uma entrada válida.")

def opcao_um_tres(): #Aqui está a terceira questão da primeira lista #concluída
    limpar_tela()
    print(f'''\t~ Cálculo de IMC ~
    Este programa irá calcular seu IMC e ranqueará você em:
    - Magreza grave
    - Magreza moderada
    - Magreza leve
    - Saudável
    - Sobrepeso
    - Obesidade Grau I
    - Obesidade Grau II (severa)
    - Obesidade Grau III (mórbida)''')
    while True:
        try:
            peso = float(input("\nDigite seu Peso em Kg: "))
            print(f"{peso} KGs")
            break
        except ValueError:
            limpar_tela()
            print("\nValor Inválido, Digite um número\n")
    while True:
        try:
            altura = float(input("Digite sua altura em Metros (utilize . ao invés de ,): "))
            print(f"{altura:.2f} metros de altura.")
            break
        except ValueError:
            limpar_tela()
            print("\nValor Inválido, Digite um número\n")

    imc = peso / altura**2  
    print(f"\nSeu IMC é: {imc:.2f}\n")

    if imc < 16:
        print("Seu estado é de Magreza grave")
    elif imc < 17:
        print("Seu estado é de Magreza moderada")
    elif imc < 18.5:
        print("Seu estado é de Magreza leve")
    elif imc < 25:
        print("Você está Saudável")
    elif imc < 30:
        print("Seu estado é de Sobrepeso")
    elif imc < 35:
        print("Seu estado é de Obesidade Grau I")
    elif imc < 40:
        print("Seu estado é de Obesidade Grau II (severa)")
    else:
        print("Seu estado é de Obesidade Grau III (mórbida)")

    while True:
            try:
                escolha_continuar = int(input("Deseja Continuar, Voltar a lista ou Finalizar o programa?\n[1] - Continuar\n[2] - Retornar a Lista\n[3] - Finalizar Programa\n\n-> "))
                if escolha_continuar == 1:
                    opcao_um_tres()
                elif escolha_continuar == 2:
                    menu_um()
                elif escolha_continuar == 3:
                    print("\nFinalizando programa ...\n")
                    exit()
                else:
                    print("Opção Inválida, Tente Novamente")
            except ValueError:
                print("Insira uma entrada válida.")

def opcao_um_quatro(): #Aqui está a quarta questão da primeira lista
    limpar_tela()
    print('''\t~ Operações Matemáticas Simples ~
    
Iremos realizar a soma, subtração, multiplicação e divisão dos dois números que será inserido.''')
    while True:
        try:
            n1 = float(input("\nDigite o primeiro número: "))
            break
        except ValueError:
            limpar_tela()
            print("Valor inválido, digite um número")
            print(n1)
    while True:
        try:
            n2 = float(input("Digite o segundo número: "))
            break

        except ValueError:
            limpar_tela()
            print("Valor inválido, digite um número")
    print(f"\n {n1} + {n2} = {n1+n2}")
    print(f"{n1} - {n2} = {n1-n2}")
    print(f"{n1} x {n2} = {n1*n2}")
    print(f"{n1} / {n2} = {n1/n2:.2f}\n")
    while True:
            try:
                escolha_continuar = int(input("Deseja Continuar, Voltar a lista ou Finalizar o programa?\n[1] - Continuar\n[2] - Retornar a Lista\n[3] - Finalizar Programa\n\n-> "))
                if escolha_continuar == 1:
                    limpar_tela()
                    opcao_um_quatro()
                elif escolha_continuar == 2:
                    limpar_tela()
                    menu_um()
                elif escolha_continuar == 3:
                    print("\nFinalizando programa ...\n")
                    exit()
                else:
                    print("Opção Inválida, Tente Novamente")
            except ValueError:
                print("Insira uma entrada válida.")

def opcao_um_cinco(): #Aqui está a quinta questão da primeira lista
    limpar_tela()
    print('''\t~ Média Aritmética ~
    
Este programa irá calcular a média aritmética simples de 3 notas.
''')
    n1=float(input("Digite a primeira nota: "))
    n2=float(input("Digite a segunda nota: "))
    n3=float(input("Digite a terceira nota: "))
    m = (n1+n2+n3)/3
    print(f"A média é igual a {m:.2f}\n")
    if m >=7:
        print("Você está aprovado(a)!!!\n")
    else:
        print("Você está reprovado(a)!!!\n")

    while True:
            try:
                escolha_continuar = int(input("Deseja Continuar, Voltar a lista ou Finalizar o programa?\n[1] - Continuar\n[2] - Retornar a Lista\n[3] - Finalizar Programa\n\n-> "))
                if escolha_continuar == 1:
                    opcao_um_cinco()
                elif escolha_continuar == 2:
                    menu_um()
                elif escolha_continuar == 3:
                    print("\nFinalizando programa ...\n")
                    exit()
                else:
                    print("Opção Inválida, Tente Novamente")
            except ValueError:
                print("Insira uma entrada válida.")
def opcao_um_seis(): #Aqui está a sexta questão da primeira lista
    limpar_tela()
    print(''' ~ Verificação PAR e ÍMPAR ~
    
    Iremos verificar se o seu número é par ou é ímpar.''')
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            resultado = numero%2
            if resultado == 0:
                print("\nO número é par.\n")
                break
            else:
                print("\nO número é impar.\n")
                break
        except ValueError:
            print("\nValor inválido, digite um número inteiro\n")
    
    while True:
            try:
                escolha_continuar = int(input("Deseja Continuar, Voltar a lista ou Finalizar o programa?\n[1] - Continuar\n[2] - Retornar a Lista\n[3] - Finalizar Programa\n\n-> "))
                if escolha_continuar == 1:
                    limpar_tela()
                    opcao_um_seis()
                elif escolha_continuar == 2:
                    limpar_tela()
                    menu_um()
                elif escolha_continuar == 3:
                    print("\nFinalizando programa ...\n")
                    exit()
                else:
                    print("Opção Inválida, Tente Novamente")
            except ValueError:
                print("Insira uma entrada válida.")
def opcao_um_sete(): #Aqui está a sétima questão da primeira lista
    print("\n Cálculo de Fatorial \n") #sim daria pra utilizar biblioteca
    while True:
        try:
            numero = int(input("Digite um número inteiro e positivo para ser cálculado: "))
            
        except ValueError:
            print("Valor inválido tente novamente")
        if numero <0:
            print("Valor Inválido")
        else:
            break
    contador = 1
    fatorial = numero
    while(numero - contador)>1:
        fatorial=fatorial*(numero - contador)
        contador+=1
    print(f"\n{numero}! = {fatorial}\n")
    
    while True:
            try:
                escolha_continuar = int(input("Deseja Continuar, Voltar a lista ou Finalizar o programa?\n[1] - Continuar\n[2] - Retornar a Lista\n[3] - Finalizar Programa\n\n-> "))
                if escolha_continuar == 1:
                    limpar_tela()
                    opcao_um_sete()
                elif escolha_continuar == 2:
                    limpar_tela()
                    menu_um()
                elif escolha_continuar == 3:
                    print("\nFinalizando programa ...\n")
                    exit()
                else:
                    print("Opção Inválida, Tente Novamente")
            except ValueError:
                print("Insira uma entrada válida.")
def opcao_um_oito(): #Aqui está a oitava questão da primeira lista
    print("\n Conversor de Horas p/ minutos\n")
    while True:
        try:
            horas = int(input("Digite a hora: "))
            minutos = horas * 60
            break
        except ValueError:
            print("Valor Inválido, tente novamente.")
    print(f"\n{horas}h em minutos é {minutos}min\n")
    while True:
            try:
                escolha_continuar = int(input("Deseja Continuar, Voltar a lista ou Finalizar o programa?\n[1] - Continuar\n[2] - Retornar a Lista\n[3] - Finalizar Programa\n\n-> "))
                if escolha_continuar == 1:
                    limpar_tela()
                    opcao_um_oito()
                elif escolha_continuar == 2:
                    limpar_tela()
                    menu_um()
                elif escolha_continuar == 3:
                    print("\nFinalizando programa ...\n")
                    exit()
                else:
                    print("Opção Inválida, Tente Novamente")
            except ValueError:
                print("Insira uma entrada válida.")

inicio()