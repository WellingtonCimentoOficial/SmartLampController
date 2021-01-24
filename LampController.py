##########################################
#    Developed by: Wellington Cimento    #
#    Contact: search my github profile   #
##########################################

"""
# Português
ESSE SCRIPT CONSEGUIRÁ CONTROLAR SUA LÂMPADA YEELIGHT SMART LED BULB (COLOR) ATRAVÉS DE UM TERMINAL LINUX OU WINDOWS UTILIZANDO FUNÇÕES BÁSICAS COMO LIGAR,
DESLIGAR, BRILHO, SATURAÇÃO, TEMPERATURA E CORES PRÉ DEFINIDAS, PODENDO ASSIM SER DESENVOLVIDO SOFTWARES MAIS COMPLEXOS COM BASE NESSE CÓDIGO.
ATRAVÉS DESSA IDEIA PODERÁ SER CRIADO SOFTWARES, COMO ALGUM PROGRAMA DE AÚDIO QUE TEM COMO FUNCIONALIDADE FAZER COM QUE A LÂMPADA EXECUTE UMA FUNÇÃO DESEJADA
DE ACORDO COM A BATIDA DE UMA MÚSICA, PODERÁ UTILIZAR JUNTO A UMA INTELIGÊNCIA ARTIFICIAL EXECUTANDO ASSIM COMANDOS DE VOZ E ETC. ESSES FORAM APENAS 2 EXEMPLOS,
DAQUI PARA FRENTE VAI DA SUA CRIATIVIDADE CRIAR ALGUM SOFTWARE QUE TENHA OUTRAS FUNCIONALIDADES E OUTROS OBJETIVOS.
OBS: ESSE CÓDIGO NÃO FOI TESTADO EM OUTRO MODELO ALÉM DO DESCRITO ACIMA.

# English
THIS SCRIPT WILL BE ABLE TO CONTROL YOUR YEELIGHT SMART LED BULB (COLOR) LAMP THROUGH A LINUX OR WINDOWS TERMINAL USING BASIC FUNCTIONS HOW TO TURN ON,
TURN OFF, BRIGHTNESS, SATURATION, TEMPERATURE AND PRE-DEFINED COLORS, SO MORE COMPLEX SOFTWARE CAN BE DEVELOPED BASED ON THIS CODE.
THROUGH THIS IDEA SOFTWARES CAN BE CREATED, SUCH AS AN AUDIO PROGRAM WITH FUNCTIONALITY TO MAKE THE LAMP PERFORM A DESIRED FUNCTION
ACCORDING TO THE BEATING OF A MUSIC, YOU CAN USE IT WITH AN ARTIFICIAL INTELLIGENCE THROUGH PERFORMING VOICE COMMANDS AND ETC. THESE WERE ONLY 2 EXAMPLES,
Henceforth IT WILL BE YOUR CREATIVITY TO CREATE SOME SOFTWARE THAT HAS OTHER FUNCTIONALITIES AND OTHER OBJECTIVES.
NOTE: THIS CODE WAS NOT TESTED IN ANY MODEL OTHER THAN THE DESCRIBED ABOVE.
"""

import socket
import time
import getpass
import os

# MODOS DA LAMPADA / LAMP MODES
onlamp = '{"id":100,"method":"set_power","params":["on","smooth",0,0]}'
offlamp = '{"id":100,"method":"set_power","params":["off","smooth",0,0]}'

# CORES DA LAMPADA / LAMP COLORS
BRANCO = '{"id":100,"method":"set_hsv","params":[0,0,"smooth",0]}'
VERDE = '{"id":100,"method":"set_hsv","params":[123,86,"smooth",0]}'
AZUL = '{"id":100,"method":"set_hsv","params":[243,86,"smooth",0]}'
VERMELHO = '{"id":100,"method":"set_hsv","params":[0,86,"smooth",0]}'
AMARELO = '{"id":100,"method":"set_hsv","params":[40,100,"smooth",0]}'
ROXO = '{"id":100,"method":"set_hsv","params":[275,100,"smooth",0]}'

# LISTAS
lista1 = [] # recebe valores de 1 a 100 da função jogar_na_lista() / receives values from 1 to 100 of the function jogar_na_lista()
lista2 = [] # recebe valores de 1700 a 6500 da função jogar_na_lista2() / receives values from 1700 to 6500 of the function jogar_na_lista2()

porta = 55443  # porta que o dispositivo yeelight recebe conexões / port that the yeelight device receives connections

USUARIO = getpass.getuser()  # pegando o usuario do sistema e jogando na variavel / taking the system user and playing in the variable


def jogar_na_lista(): # função que adiciona numeros de 1 a 100 na variavel lista / function that adds numbers from 1 to 100 in the variable lista
    for numero in range(1, 101):
        lista1.append(str(numero))


jogar_na_lista() # iniciando a função / starting function


def jogar_na_lista2(): # função que adiciona numeros de 1700 a 6500 na variavel lista2 / function that adds numbers from 1700 to 6500 in the variable lista2
    for numero in range(1700, 6501):
        lista2.append(str(numero))


jogar_na_lista2() # iniciando a função / starting function


def limpar_menu(): # função para limpar o menu usando comando de acordo com o sistema operacional / function to clear the menu using command according to the operating system
    sistema = os.name
    if sistema == 'nt':
        os.system('cls')
        os.system('color F')
    else:
        os.system('clear')


def file_ip():  # função parar abrir e ler um arquivo que contem o ip do dispositivo yeelight, caso este arquivo não existir, então ele sera criado automaticamente
    try:  # dentro deste arquivo irá conter o ip que sera inserido através de um input abaixo no except
        with open("C:\\Users\\" + USUARIO + "\\Documents\\LampController_file_ip.txt", 'r') as file:
            ip = file.read().strip()
            return ip
    except:  # function to open and read a file containing the ip of the yeelight device, if this file does not exist, then it will be created automatically
        try:  # inside this file it will contain the ip that will be inserted through an input below in except
            with open("C:\\Users\\" + USUARIO + "\\Documents\\LampController_file_ip.txt", 'w') as file:
                limpar_menu()
                ip = str(input("Enter your Yeelight device's ip: "))
                file.write(ip)
                return ip
        except:
            print('ERROR: An error was caused while trying to create the file LampController_file_ip.txt')

def erro_arquivotxt(): # função que retorna uma mensagem de erro / function that returns an error message
    limpar_menu()
    print('ERROR: An error was caused while trying to create the file "LampController_file_ip.txt"')
    print('Closing in 10 seconds ...')
    time.sleep(10)
    exit()


def conexao(ip):  # função para efetuar a conexão com a lampada / function to connect to the lamp
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, porta))
        return s
    except Exception as e:
        print("ERROR: " + e)
        exit()


def enviar(s, opcao):  # função para enviar os dados para a lampada como MODOS DA LAMPADA e CORES DA LAMPADA / function to send data to the lamp such as LAMP MODES and LAMP COLORS
    s.send(opcao.encode() + b'\r\n')


def receber(s):  # função que recebe os dados que a lampada retornar depois de ter enviado um comando / function that receives the data that the lamp returns after having sent a command
    data = s.recv(1024)
    s.close()
    receber_resposta = ''
    if 'ok' in str(data):
        receber_resposta += 'ok'
        return receber_resposta


def temperatura_cor(s, escolha):  # função para escolher a temperatura da cor da lampada / function to choose the temperature of the lamp color
    color_temperatura = '{"id":100,"method":"set_ct_abx","params":[' + str(escolha) + ',"smooth",0]}'
    enviar(s, color_temperatura)  # essa função só irá funcionar caso a lâmpada esteja ligada / this function will only work if the lamp is on
    s.close()


def brilho(s, escolha):  # função para escolher a intensidade do brilho da lampada / function to choose the brightness intensity of the lamp
    brilho_lamp = '{"id":100,"method":"set_bright","params":[' + str(escolha) + ',"smooth",0]}'
    enviar(s, brilho_lamp)  # essa função só irá funcionar caso a lâmpada esteja ligada / this function will only work if the lamp is on
    s.close()


def saturacao(s, escolha):  # função para escolher a intensidade da saturação do brilho da lampada / function to choose the intensity of saturation of the brightness of the lamp
    brilho_lamp = '{"id":100,"method":"set_hsv","params":[0,' + str(escolha) + ',"smooth",0]}'
    enviar(s, brilho_lamp)  # essa função só irá funcionar caso a lâmpada esteja ligada / this function will only work if the lamp is on
    s.close()


def cores(s, escolha):  # função para enviar as cores já pré definidas que estão nas variaveis CORES DA LAMPADA no começo do código / function to send the pre-defined colors that are in the variable LAMP COLORS at the beginning of the code
    enviar(s, escolha)  # essa função só irá funcionar caso a lâmpada esteja ligada / this function will only work if the lamp is on
    s.close()


def menu_brilho():  # função para mostrar um menu com as opções de escolher um numero de 1 á 100 para mudar o brilho da lampada / function to show a menu with the options to choose a number from 1 to 100 to change the brightness of the lamp
    print("Note: this option will only work if the lamp is already on\n")
    print("0 - RETURN\n00 - EXIT\n")
    while True:
        try:
            ip = file_ip()
            try:
                s = conexao(ip)
            except:
                erro_arquivotxt()
        except:
            print('ERROR: An error occurred while attempting to establish a connection.')
            exit()
        escolha = input("Enter a desired value of 1/100: ")
        if escolha == 'return' or escolha == "RETURN" or escolha == "0":
            limpar_menu()
            logo()
            menu1(ip)
        elif escolha == 'exit' or escolha == "EXIT" or escolha == "00":
            exit()
        elif escolha in lista1:
            brilho(s, escolha)
        else:
            print("Invalid option!")


def menu_temperature():  # função para mostrar um menu com as opções de escolher um numero de 1 á 100 para mudar o brilho da lampada / function to show a menu with the options to choose a number from 1 to 100 to change the brightness of the lamp
    print("Note: This option will only work if the lamp is already on\n")
    print("0 - RETURN\n00 - EXIT\n")
    while True:
        try:
            ip = file_ip()
            try:
                s = conexao(ip)
            except:
                erro_arquivotxt()
        except:
            print('ERROR: An error occurred while attempting to establish a connection.')
            exit()
        escolha = input("Enter a desired value of 1700/6500: ")
        if escolha == 'return' or escolha == "RETURN" or escolha == "0":
            limpar_menu()
            logo()
            menu1(ip)
        elif escolha == 'exit' or escolha == "EXIT" or escolha == "00":
            exit()
        elif escolha in lista2:
            temperatura_cor(s, escolha)
        else:
            print("Invalid option!")


def menu_saturacao():  # função para mostrar um menu com as opções de escolher um numero de 1 á 100 para mudar a saturação da lampada / function to show a menu with the options to choose a number from 1 to 100 to change the saturation of the lamp
    print("Note: This option will only work if the lamp is already on\n")
    print("0 - RETURN\n00 - EXIT\n")
    while True:
        try:
            ip = file_ip()
            try:
                s = conexao(ip)
            except:
                erro_arquivotxt()
        except:
            print('ERROR: An error occurred while attempting to establish a connection.')
            exit()
        escolha = input("Enter a desired value of 1/100: ")
        if escolha == 'return' or escolha == "RETURN" or escolha == "0":
            limpar_menu()
            logo()
            menu1(ip)
        elif escolha == 'exit' or escolha == "EXIT" or escolha == "00":
            exit()
        elif escolha in lista1:
            saturacao(s, escolha)
        else:
            print("Invalid option!")


def menu_cores():  # função para exibir um menu com opções de cores pré definidas / function to display a menu with pre-defined color options
    print("1 - WHITE\n2 - BLUE\n3 - RED\n4 - YELLOW\n5 - PURPLE\n6 - GREEN\n0 - RETURN\n00 - EXIT\n")
    while True:
        try:
            ip = file_ip()
            try:
                s = conexao(ip)
            except:
                erro_arquivotxt()
        except:
            print('ERROR: An error occurred while attempting to establish a connection.')
            exit()

        escolha = input("Enter the desired value: ")
        if escolha == 'return' or escolha == "RETURN" or escolha == "0":
            limpar_menu()
            logo()
            menu1(ip)
        elif escolha == 'exit' or escolha == "EXIT" or escolha == "00":
            exit()
        elif escolha == 'WHITE' or escolha == 'white' or escolha == '1':
            cores(s, BRANCO)
        elif escolha == 'BLUE' or escolha == 'blue' or escolha == '2':
            cores(s, AZUL)
        elif escolha == 'RED' or escolha == 'red' or escolha == '3':
            cores(s, VERMELHO)
        elif escolha == 'YELLOW' or escolha == 'yellow' or escolha == '4':
            cores(s, AMARELO)
        elif escolha == 'PURPLE' or escolha == 'purple' or escolha == '5':
            cores(s, ROXO)
        elif escolha == 'GREEN' or escolha == 'green' or escolha == '6':
            cores(s, VERDE)
        else:
            print("Invalid option!")


def menu1(ip):  # função para mostrar um menu principal de opções / function to show a main menu of options
    print("[1] - ON\n[2] - OFF\n[3] - BRIGHTNESS\n[4] - SATURATION\n[5] - TEMPERATURE\n[6] - COLORS\n")
    while True:
        try:
            s = conexao(ip)
        except:
            limpar_menu()
            print('ERROR: An error occurred during the connection attempt. Check if the registered IP address is the same as the YEELIGHT device.\n'
                  'If the problem persists try to delete the file "LampController_file_ip.txt"' + ' in the directory' + ' C:\\Users\\' + USUARIO + '\\Documents')
            print('Leaving in 10 seconds ...')
            time.sleep(10)
            exit()

        escolha = input("Choose one of the options above or EXIT to close: ")
        if escolha == 'ON' or escolha == 'on' or escolha == '1':
            enviar(s, onlamp)
            receber(s)
        elif escolha == 'off' or escolha == 'OFF' or escolha == '2':
            enviar(s, offlamp)
            receber(s)
        elif escolha == 'brightness' or escolha == 'BRIGHTNESS' or escolha == '3':
            limpar_menu()
            logo()
            menu_brilho()
        elif escolha == 'saturation' or escolha == 'SATURATION' or escolha == '4':
            limpar_menu()
            logo()
            menu_saturacao()
        elif escolha == 'temperature' or escolha == 'TEMPERATURE' or escolha == '5':
            limpar_menu()
            logo()
            menu_temperature()
        elif escolha == 'colors' or escolha == 'COLORS' or escolha == '6':
            limpar_menu()
            logo()
            menu_cores()
        elif escolha == 'exit' or escolha == 'EXIT' or escolha == '00':
            s.close()
            exit()
        else:
            print("Invalid option!")


def logo(): # função que mostra a logo do script / function that shows the script logo
    print('$═════════════════════════════════════#')
    print('$          Lamp Controller            #')
    print('$            Version 1.0              $')
    print('#    Created By: Wellington Cimento   $')
    print('#═════════════════════════════════════$')
    print('')


def main():  # função principal que roda o programa / main function that runs the program
    file_ip()
    limpar_menu()
    ip = file_ip()
    logo()
    menu1(ip)


main()  # chamando a função principal (main) / calling the main function
