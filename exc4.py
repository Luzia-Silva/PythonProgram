#EXERCICIO 4
#Autor:  Luzia Silva - 12/11/2021 - Franco da Rocha, SP


while 1:
    print("\nFORMULÁRIO")
    print("-------------------------------------------------------------")
    nome = input("Informe o seu nome:")
    idade = int(input("Informe a sua idade:"))
    salario = float(input("Informe o seu salário:"))
    sexo = input("Informe o seu sexo: (F/M)")
    civil = input("Informe seu Estados Civil: ")
    if(len(nome)<3):
     print("Nome Incorreto! \nPreencha novamente o Formulário")
    elif(idade<0 or idade>150):
     print("idade Incorreto! \nPreencha novamente o Formulário")
    elif(salario<0):
     print("Salário Incorreto! \nPreencha novamente o Formulário")
    elif(sexo!='f' and sexo!='m'):
     print("Sexo Incorreto! \nPreencha novamente o Formulário")
    elif(civil!='s'and civil!='c' and civil!='v'and civil!='d'):
      print("Estado Civil Incorreto! \nPreencha novamente o Formulário")
    else:
     print("\n\nDADOS CADASTRADOS")
     print("-------------------------------------------------------------")
     print("Seus dados são:\nNome:",nome,"\nIdade:",idade,"\nSalário:",salario,"\nSexo:",sexo,"\nEstado Civil:",civil)
     break