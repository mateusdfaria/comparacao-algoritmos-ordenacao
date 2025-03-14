import random

def gerar_numeros(qtd, arquivo="dados.txt"):
    """Gera números aleatórios e salva em um arquivo de texto."""
    with open(arquivo, "w") as f:
        for _ in range(qtd):
            f.write(f"{random.randint(1, 100000)}\n")  # Gerando números de 1 a 100000

    print(f"{qtd} números gerados e salvos em {arquivo}")

# Tamanhos de dados solicitados
tamanhos = [1000, 10000, 100000]

for tamanho in tamanhos:
    gerar_numeros(tamanho, f"dados_{tamanho}.txt")
