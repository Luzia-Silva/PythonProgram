#EXERCICIO 1
#Autor:  Luzia Silva - 12/11/2021 - Franco da Rocha, SP

print("ORGANIZAÇÃO TABAJARA - AUMENTO SALARIAL")
print("-----------------------------------------")
salario = float(input("INFORME O SEU SALÁRIO:"))
print("-----------------------------------------")

if(salario<=280):
    result = salario * 0.2
    aumento = salario + result
    print("o salário antes do reajuste: ",salario)
    print("o percentual de aumento aplicado: 20%")
    print("o valor do aumento: ",result)
    print("o novo salário, após o aumento: ",aumento)
elif(salario>280 and salario<=700):
    result = salario * 0.15
    aumento = salario + result
    print("o salário antes do reajuste: ", salario)
    print("o percentual de aumento aplicado: 15%")
    print("o valor do aumento: ", result)
    print("o novo salário, após o aumento: ", aumento)
elif(salario>700 and salario<=1500):
    result = salario * 0.10
    aumento = salario + result
    print("o salário antes do reajuste: ", salario)
    print("o percentual de aumento aplicado: 10%")
    print("o valor do aumento: ", result)
    print("o novo salário, após o aumento: ", aumento)

else:
    result = salario * 0.05
    aumento = salario + result
    print("o salário antes do reajuste: ", salario)
    print("o percentual de aumento aplicado: 5%")
    print("o valor do aumento: ", result)
    print("o novo salário, após o aumento: ", aumento)