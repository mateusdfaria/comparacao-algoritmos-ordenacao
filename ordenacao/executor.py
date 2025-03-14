import time
from opentelemetry import trace
from tracing import tracer  # Importa o OpenTelemetry

from ordenacao.bubble_sort import BubbleSort
from ordenacao.insertion_sort import InsertionSort
from ordenacao.selection_sort import SelectionSort
from ordenacao.quick_sort import QuickSort
from ordenacao.merge_sort import MergeSort
from ordenacao.tim_sort import TimSort

def carregar_dados(arquivo):
    """Carrega os números do arquivo para uma lista."""
    with open(arquivo, "r") as f:
        return [int(line.strip()) for line in f.readlines()]

def executar_ordenacao(algoritmo, arquivo):
    """Executa um algoritmo de ordenação e registra métricas com OpenTelemetry."""
    dados = carregar_dados(arquivo)
    
    with tracer.start_as_current_span(algoritmo.__class__.__name__) as span:
        inicio = time.perf_counter()
        resultado, comparacoes, trocas = algoritmo.sort(dados)
        fim = time.perf_counter()

        tempo_execucao = (fim - inicio) * 1000  # Convertido para milissegundos

        # Adicionando métricas ao OpenTelemetry
        span.set_attribute("algoritmo", algoritmo.__class__.__name__)
        span.set_attribute("arquivo", arquivo)
        span.set_attribute("tempo_execucao_ms", tempo_execucao)
        span.set_attribute("comparacoes", comparacoes)
        span.set_attribute("trocas", trocas)

        # Exibição no console
        print(f"Algoritmo: {algoritmo.__class__.__name__}")
        print(f"Arquivo: {arquivo}")
        print(f"Tempo de execução: {tempo_execucao:.6f} ms")
        print(f"Comparações: {comparacoes}")
        print(f"Trocas: {trocas}")
        print("-" * 40)

# Executar diferentes algoritmos
if __name__ == "__main__":
    arquivos = ["dados_1000.txt", "dados_10000.txt"]
    
    bubble_sort = BubbleSort()
    insertion_sort = InsertionSort()
    selection_sort = SelectionSort()
    quick_sort = QuickSort()
    merge_sort = MergeSort()
    tim_sort = TimSort()

    for arquivo in arquivos:
        executar_ordenacao(bubble_sort, arquivo)
        executar_ordenacao(insertion_sort, arquivo)
        executar_ordenacao(selection_sort, arquivo)
        executar_ordenacao(quick_sort, arquivo)
        executar_ordenacao(merge_sort, arquivo)
        executar_ordenacao(tim_sort, arquivo)
