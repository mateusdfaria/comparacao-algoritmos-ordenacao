import random
import time
from prometheus_client import Counter, Histogram, start_http_server
from sorting import (
    SortingContext, BubbleSort, BubbleSortOptimized, InsertionSort, SelectionSort, 
    QuickSort, MergeSort, HeapSort, TimSort
)

# Definir métricas do Prometheus
COMPARACOES = Counter('sorting_comparisons_total', 'Total de comparações por algoritmo', ['algorithm'])
TROCAS = Counter('sorting_swaps_total', 'Total de trocas por algoritmo', ['algorithm'])
TEMPO = Histogram('sorting_execution_time_seconds', 'Tempo de execução em segundos por algoritmo', ['algorithm'])

def generate_data(size):
    """Gera uma lista de números aleatórios para teste."""
    return [random.randint(0, 100000) for _ in range(size)]

def measure_sorting_time(sorting_strategy, data):
    """Mede o tempo de execução e coleta métricas."""
    context = SortingContext(sorting_strategy)
    start_time = time.time()
    sorted_data, comparisons, swaps = context.execute_sort(data.copy())
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # Tempo em ms
    tempo_segundos = elapsed_time / 1000  # Converter para segundos
    # Registrar as métricas
    COMPARACOES.labels(algorithm=sorting_strategy.__class__.__name__).inc(comparisons)
    TROCAS.labels(algorithm=sorting_strategy.__class__.__name__).inc(swaps)
    TEMPO.labels(algorithm=sorting_strategy.__class__.__name__).observe(tempo_segundos)
    return sorted_data, elapsed_time, comparisons, swaps

def main():
    start_http_server(8000)
    sizes = [1000, 10000, 100000]
    algorithms = [
        ("Bubble Sort", BubbleSort()),
        ("Bubble Sort Optimized", BubbleSortOptimized()),
        ("Insertion Sort", InsertionSort()),
        ("Selection Sort", SelectionSort()),
        ("Quick Sort", QuickSort()),
        ("Merge Sort", MergeSort()),
        ("Heap Sort", HeapSort()),
        ("Tim Sort", TimSort()),  # Adicionado aqui
    ]

    print("Iniciando testes de ordenação. Pressione Ctrl+C para parar.")
    try:
        while True:
            for size in sizes:
                print(f"\nTestando com {size} elementos...")
                data = generate_data(size)
                for name, algorithm in algorithms:
                    _, elapsed_time, comparisons, swaps = measure_sorting_time(algorithm, data)
                    print(f"{name}: {elapsed_time:.2f} ms | Comparações: {comparisons} | Trocas: {swaps}")
            print("Testes concluídos. Repetindo em 30 segundos...")
            time.sleep(30)
    except KeyboardInterrupt:
        print("\nParando o servidor de métricas.")

if __name__ == "__main__":
    main()