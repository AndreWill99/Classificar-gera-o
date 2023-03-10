idade=int(input(f"\n\t digite a idade (maior ou igual a 15): "))

if (idade < 15):
    print("\n\t não existe classificação para essa idade")

elif (idade <= 20):
        print(f"\n\t pertence a geração Z")
elif (idade <= 35):
        print(f"\n\t pertence a geração y")
elif (idade <= 65):
        print(f"\n\t pertence a geração Boomers")
else:
    print(f"\n\t pertence a geração silenciosa")

#...#
sexo = input("\n\tDigite o sexo (M ou m para Masculino / F ou f para Feminino):")


if ((sexo == 'f') or (sexo == "F")):
    if(idade >= 21):
        print(f"\nAtingiu a maioridade")
    else:
        print(f"\n\tNão atingiu a maioridade")
elif ((sexo == 'm') or (sexo == "M")):
    if(idade >= 18): 
        print('\n\n\tAtingiu a maioridade')
    else:
        print('\n\n\t Não Atingiu a maioridade')
# Processamento e Saída:
else:
    print('\n\n\tSexo invalido')