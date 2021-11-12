#EXERCICIO 1
#Autor:  Luzia Silva - 12/11/2021 - Franco da Rocha, SP

print("Classificação sobre a participação da pessoa no crime.")
print("*******************************************")
print("DIGITE PARA 'SIM' 1  E 'NÃO' 0 ")
r1 = int(input("Telefonou para a vítima?"))
r2 = int(input("Esteve no local do crime?"))
r3 = int(input("Mora perto da vítima?"))
r3 = int(input("Devia para a vítima?"))
r4 = int(input("Já trabalhou com a vítima?"))
print("*******************************************")
if(r1<=1 and r2<=1 and r3<=1 and r4<=1 and r4<=1):
   cont = r1 + r2 + r3 + r4 + 1
   if(cont==5):
      print("ASSASSINO! XADREZ NELE!!")
   elif(cont==2):
      print("SUSPEITA")
   elif(cont>=3 or cont==4):
      print("Cúmplice")
   else:
      print("INOCENTE")

else:
   print("VALOR ERRADO! É 1 (SIM) OU 0 (NÃO)")