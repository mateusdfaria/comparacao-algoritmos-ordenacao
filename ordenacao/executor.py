import time
from ordenacao.bubble_sort import BubbleSort
from ordenacao.insertion_sort import InsertionSort

def carregar_dados(arquivo):
    """Carrega os números do arquivo para uma lista."""
    with open(arquivo, "r") as f:
        return [int(line.strip()) for line in f.readlines()]

def executar_ordenacao(algoritmo, arquivo):
    """Executa um algoritmo de ordenação e mede tempo e operações."""
    dados = carregar_dados(arquivo)
    
    inicio = time.time()
    resultado, comparacoes, trocas = algoritmo.sort(dados)
    fim = time.time()

    print(f"Algoritmo: {algoritmo.__class__.__name__}")
    print(f"Arquivo: {arquivo}")
    print(f"Tempo de execução: {fim - inicio:.6f} segundos")
    print(f"Comparações: {comparacoes}")
    print(f"Trocas: {trocas}")
    print("-" * 40)

# Executar diferentes algoritmos
if __name__ == "__main__":
    arquivos = ["dados_1000.txt", "dados_10000.txt"]
    
    bubble_sort = BubbleSort()
    insertion_sort = InsertionSort()

    for arquivo in arquivos:
        executar_ordenacao(bubble_sort, arquivo)
        executar_ordenacao(insertion_sort, arquivo)
