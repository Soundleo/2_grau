# crie um programa onde o usuário deida qual equação ele deseja usar: equção do primeiro grau ou equação do segundo grau

import math
def primeiro_grau (a, b):
    x = -b/a
    print (x)    

def equacao_segundo_grau(a, b, c):
    if a == 0: 
        print ('Equação impossível')
    else:
        delta = (b**2) - (4*a*c)
        if delta > 0:
            print ('A equação não possui soluções reais.')
        elif delta == 0:
            x = -b / (2*a)
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            
        # print (delta)


print("Informe qual tipo de equiação deseja utilizar.")
print("primeiro grau: Ax + B = 0")
print("segundo grau grau: ax^2 + bx + c = 0")
tipo_equação = int(input("Escolha o tipo de equação que deseja utitlizar 1 ou 2: "))

match tipo_equação:
    case 1:
        a = int(input('informe o valor de A: '))
        b = int(input('informe o valor de B: '))
        primeiro_grau(a, b) 
    case 2:
        a = int(input('informe o valor de A: '))
        b = int(input('informe o valor de B: '))
        c = int(input('informe o valor de C: '))

        equacao_segundo_grau(a, b, c)

    case _:
        print('valor errado informe novamente')



    