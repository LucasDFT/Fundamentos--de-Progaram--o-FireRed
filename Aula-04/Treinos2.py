Nome= (str(input("Informe seu nome, para prosseguirmos com os calculos: ")))


B1 = (float(input("Informe a nota de sua primeira prova do primeiro trimestre: ")))
B2 = (float(input("Informe a nota de sua segunda prova do primeiro trimestre: ")))
B3 = (float(input("Informe a nota de sua terceira prova do primeiro trimestre: ")))



N1 =  (float(input("Informe a nota de sua primeira prova do segundo trimestre: ")))
N2 =  (float(input("Informe a nota de sua segunda prova do segundo trimestre: ")))
N3 =  (float(input("Informe a nota de sua terceira prova do segundo trimestre: ")))



M1 = (float(input("Informe a nota de sua primeira prova do terceiro trimestre: ")))
M2 = (float(input("Informe a nota de sua primeira prova do terceiro trimestre: ")))
M3 = (float(input("Informe a nota de sua primeira prova do terceiro trimestre: ")))



M4 = (M1+M2+M3)/3
N4 = (N1+N2+N3)/3
B4 = (B1+B2+B3)/3
R =  (M4+N4+B4)/3

print ("-----------------------------------------------------------------------------")
print (f"{Nome} em sua primeira prova do T1 você obteve {M4} em sua segunda {N4} e em sua terceira {B4} e devido a isto, sua média do primeiro trimestre, é igual a {R} ")
print ("-----------------------------------------------------------------------------")

if B4 >= 7: 
           print ("----------------------------------------------------------------------------------------")
           print             (f"{Nome} você foi aprovado com sucesso, neste primeiro trimestre!")
           print ("----------------------------------------------------------------------------------------")
elif B4 >= 0:
           print ("----------------------------------------------------------------------------------------------------------------------------------------")
           print   (f" {Nome} Infelizmente, você ficou em recuperação no primeiro trimestre, pois sua média não alcançou os resultados necessários.") 
           print ("----------------------------------------------------------------------------------------------------------------------------------------")





if N4 >= 7: 
           print ("----------------------------------------------------------------------------------------")
           print             (f"{Nome} você foi aprovado com sucesso, neste segundo trimestre!")
           print ("----------------------------------------------------------------------------------------")
elif N4 >= 0:
           print ("----------------------------------------------------------------------------------------------------------------------------------------")
           print   (f" {Nome} Infelizmente, você ficou em recuperação no segundo trimestre, pois sua média não alcançou os resultados necessários.") 
           print ("----------------------------------------------------------------------------------------------------------------------------------------")







if M4 >= 7: 
           print ("----------------------------------------------------------------------------------------")
           print             (f"{Nome} você foi aprovado com sucesso, neste terceiro trimestre!")
           print ("----------------------------------------------------------------------------------------")
elif M4 >= 5:
           print ("----------------------------------------------------------------------------------------------------------------------------------------")
           print   (f" {Nome} Infelizmente, você ficou em recuperação no terceiro trimestre, pois sua média não alcançou os resultados necessários.") 
           print ("----------------------------------------------------------------------------------------------------------------------------------------")



if R >= 7:
         print ("----------------------------------------------------------------------------------------------------------------------------------------")
         print  (f"{Nome} felizmente, você obteve resultados positivos ao longo de seu ano letivo, e devido a isto, você foi aprovado ao fim deste ano.")
         print ("----------------------------------------------------------------------------------------------------------------------------------------")
elif R >= 5:
         print ("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
         print    (f"{Nome} Infelizmente, mesmo se esforçando ao longo do ano, você não conseguiu obter os resultados necessários para sua aprovação e ficou em estado de recuperação.")
         print ("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

else:    
        print ("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print    (f"{Nome} infelizmente, mesmo após tanto esforço nesse ano letivo, você não conseguiu obter os resultados necessários para atingir nem ao menos a recuperação e foi reprovado.")
        print ("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

 


