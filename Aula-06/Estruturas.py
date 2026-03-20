# Estrutura de Repetição 
# If (se) -> Verifica se uma condição é True (verdadeira). Se for, ele executa o código.
# Elif (senão se) -> É usado para testar várias condições. Ele só executa se todas as condições anterioeres forem falsas.
# Else (senão) -> Executa o código de se a condição if for false (falsa).

Idade = (int(input("Digite Sua Idade: ")))

if Idade >= 18:
               print(f" Você é de maior caba, fica esperto rapaz, que você ja tem {Idade} anos")
elif Idade >=  14 and Idade < 18:      
                  print(f"Tá ficando véio truta, é adolescente já, logo logo ta morrendo pois já tem {Idade} anos")
elif Idade >= 90:                   
                  print(f"Você é uma mumia? Dorme no Sarcófago? Possivelmente né? Enfim morra logo, afinal você já tem {Idade} anos ")
 
else:
                  print (f"Cê é criança rapaz, vai comer uma terra, pois você tem somente {Idade} anos")


 