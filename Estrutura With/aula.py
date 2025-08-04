# Estrutura With

# sem with
# arquivo = open("meu_arquivo.txt", "w")
# arquivo.write("Eita Lirinha, manda vídeo novo pra gente aí")
# arquivo.close()

# com o with
with open("meu_arquivo.txt", "w") as arquivo:
    arquivo.write("E aí Lira, tranquilão?")

with open("meu_arquivo.txt", "r") as arquivo:
    print(arquivo.read())