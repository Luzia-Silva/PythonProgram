#EXERCICIO 2
#Autor:  Luzia Silva - 12/11/2021 - Franco da Rocha, SP

print("um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.")
print("---------------------------------------------------------------------------------------")
a = int(input("INFORME O VALOR DE 'A':"))
b = int(input("INFORME O VALOR DE 'B':"))
c = int(input("INFORME O VALOR DE 'C':"))

if(a!=0):
    delta = (b*b) - 4 * a * c
    raiz = delta ** (1/2)
    x1 = (-b + raiz)/ 2 * a
    x2 = (-b - raiz) / 2 * a
    if(delta<0):
        print("------------------------------------RESULTADO---------------------------------------")
        print("A equação não possui raizes reais")
        print("Delta:",delta)
    elif(delta==0):
        print("------------------------------------RESULTADO---------------------------------------")
        print("A equação possui apenas uma raiz real")
        print("Delta:",delta)
        print("X1 & X2:",x1)
    else:
        print("------------------------------------RESULTADO---------------------------------------")
        print("DELTA:",delta)
        print("X1: ",x1)
        print("X2: ",x2)
else:
    print("ESSA EQUAÇÃO NÃO É DO 2º GRAU")
