#5. Cálculo de Média: 
#Escreva um programa que solicite ao usuário três notas de um aluno, calcule a 
#média aritmética e exiba o resultado. 
#6. Verificação de Par ou Ímpar: 
#Desenvolva um programa que solicite ao usuário um número inteiro e informe 
#se ele é par ou ímpar. 
#7. Cálculo de Fatorial: 
#Crie um programa que solicite ao usuário um número inteiro positivo e calcule 
#o fatorial desse número. 
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


def opcao_um_um(): #Aqui está a primeira questão da primeira lista
    limpar_tela()

    print('''\t~ Cálculo da Área do Quadrado ~
        ''')
    print("Este programa irá calcular a área do quadrado")
    lado = float(input("\nDigite o comprimento do lado do quadrado, em metros: "))
    area = lado**2
    perimetro = lado * 4
    print(f"O seu quadrado mede {area:.2f}m² e seu perímetro {perimetro:.2f}\n")

    while True:
            try:
                escolha_continuar = int(input("Deseja Continuar, Voltar a lista ou Finalizar o programa?\n[1] - Continuar\n[2] - Retornar a Lista\n[3] - Finalizar Programa\n\n-> "))
                if escolha_continuar == 1:
                    opcao_um_um()
                elif escolha_continuar == 2:
                    menu_um()
                elif escolha_continuar == 3:
                    print("\nFinalizando programa ...\n")
                    exit()
                else:
                    print("Opção Inválida, Tente Novamente")
            except ValueError:
                print("Insira uma entrada válida.")

    

def opcao_um_dois(): #Aqui está a segunda questão da primeira lista
    limpar_tela()

    print('''\t~ Conversão de Temperatura ~
Este programa pode converter temperaturas °C, °F e K''')

    unidade_um = ""
    unidade_dois = ""
    escolha_um = int(input("\nDeseja Converter qual forma de medida?\n[1] - Celsius(°C)\n[2] - Fahrenheit (°K)\n[3] - Kelvin (K)\n\n --> "))
    if escolha_um == 1:
        unidade_um = "Celsius (°C)"
    elif escolha_um == 2:
        unidade_um = "Fahrenheit (°F)"
    elif escolha_um == 3:
        unidade_um = "Kelvin (K)"
    else:
        print("Valor Inválido, tente novamente")
        opcao_um_dois()

    valor_original = float(input(f"\nInsira seu valor em {unidade_um}: "))

    escolha_dois = int(input("\nDeseja Converter o valor para qual forma de medida?\n[1] - Celsius(°C)\n[2] - Fahrenheit (°K)\n[3] - Kelvin (K)\n\n --> "))
    
    if escolha_dois == 1:
        unidade_dois = "Celsius (°C)"
    elif escolha_dois == 2:
        unidade_dois = "Fahrenheit (°F)"
    elif escolha_dois == 3:
        unidade_dois = "Kelvin (K)"
    else:
        print("Valor Inválido, tente novamente")
        return
    
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
                    opcao_um_dois()
                elif escolha_continuar == 2:
                    menu_um()
                elif escolha_continuar == 3:
                    print("\nFinalizando programa ...\n")
                    exit()
                else:
                    print("Opção Inválida, Tente Novamente")
            except ValueError:
                print("Insira uma entrada válida.")


def opcao_um_tres(): #Aqui está a terceira questão da primeira lista
    limpar_tela()
    print(f'''\t~ Cálculo de IMC ~
    Este programa irá calcular seu IMC e ranqueará você em:
    - Abaixo do Peso
    - Peso Normal
    - Sobrepeso
    - Obesidade''')
    peso = float(input("\nDigite seu Peso em Kg: "))
    altura = float(input("Digite sua altura em Metros: "))
    imc = peso / altura**2
    print(f"Seu IMC é: {imc:.2f}")
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
    n1 = float(input("\nDigite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print(f"\n {n1} + {n2} = {n1+n2}")
    print(f"{n1} - {n2} = {n1-n2}")
    print(f"{n1} x {n2} = {n1*n2}")
    print(f"{n1} / {n2} = {n1/n2:.2f}")

def opcao_um_cinco(): #Aqui está a quinta questão da primeira lista
    limpar_tela()
    print('''\t~ Média Aritmética ~
    
Este programa irá calcular a média aritmética simples de 3 notas.''')
    celsius = float(input("Insira a tempera em °C a ser convertida: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"\n {celsius:.2f}°C em Fahrenheit é {fahrenheit:.2f}.\n")
def opcao_um_seis(): #Aqui está a sexta questão da primeira lista
    print('''~ Conversão de Temperatura ~
    
    Irá ser convertida o valor de °C para °F''')
    celsius = float(input("Insira a tempera em °C a ser convertida: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"\n {celsius:.2f}°C em Fahrenheit é {fahrenheit:.2f}.\n")
def opcao_um_sete(): #Aqui está a sétima questão da primeira lista
    print('''~ Conversão de Temperatura ~
    
    Irá ser convertida o valor de °C para °F''')
    celsius = float(input("Insira a tempera em °C a ser convertida: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"\n {celsius:.2f}°C em Fahrenheit é {fahrenheit:.2f}.\n")
def opcao_um_oito(): #Aqui está a oitava questão da primeira lista
    print('''~ Conversão de Temperatura ~
    
    Irá ser convertida o valor de °C para °F''')
    celsius = float(input("Insira a tempera em °C a ser convertida: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"\n {celsius:.2f}°C em Fahrenheit é {fahrenheit:.2f}.\n")



inicio()