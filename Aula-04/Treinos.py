
Player_1 = {
            "Hp": float(input("Digite o valor de seu Hp: ")),      
            "Defesa": float(input("Digite o valor de seu Defesa: ")),    
            "Velocidade": float(input("Digite o valor de seu Velocidade: ")),    
            "Stamina": float(input("Digite o valor de seu Stamina: ")), 
            "Força": float(input("Digite o valor de seu Forca: ")),  
            "Nome": str(input("Digite o valor de seu Nome: "))

}


Player_2 = {
            "Hp": float(input("Digite o valor de seu Hp: ")),      
            "Defesa": float(input("Digite o valor de seu Defesa: ")),    
            "Velocidade": float(input("Digite o valor de seu Velocidade: ")),    
            "Stamina": float(input("Digite o valor de seu Stamina: ")),
            "Força": float(input("Digite o valor de seu Forca: ")),     
            "Nome": str(input("Digite o valor de seu Nome: "))

}



Player_3 = {
            "Hp": float(input("Digite o valor de seu Hp: ")),      
            "Defesa": float(input("Digite o valor de seu Defesa: ")),    
            "Velocidade": float(input("Digite o valor de seu Velocidade: ")),    
            "Stamina": float(input("Digite o valor de seu Stamina: ")),
            "Força": float(input("Digite o valor de seu Forca: ")),      
            "Nome": str(input("Digite o valor de seu Nome: "))

}





if Player_1["Velocidade"] > Player_2 ["Velocidade"]: 
                                                      print(Player_1["Nome"], "é mais rápido, pois ele tem", Player_1["Velocidade"], "a mais que o", Player_2["Nome"], "e devido a isto ele irá aplicar o speedblitz.")
else: 
                                                      print(Player_2["Nome"], "é mais rápido, pois ele tem", Player_2["Velocidade"], "a mais que o", Player_1["Nome"], "e devido a isto ele irá aplicar o speedblitz.")

dano_1=(Player_1["Força"] + Player_1["Velocidade"])/2

dano_2=(Player_2["Força"] + Player_2["Velocidade"])/2



if dano_1 > dano_2:
                    print("O", Player_1["Nome"], "tem um dano maior que o", Player_2["Nome"]) 


else:

                    print("O", Player_2["Nome"], "tem um dano maior que o", Player_1["Nome"]) 




