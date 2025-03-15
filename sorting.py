from abc import ABC, abstractmethod
import time
from opentelemetry import metrics
 
# Criar provedor de métricas
meter = metrics.get_meter(__name__)
 
# Definir métricas
execution_time = meter.create_histogram(
    name="sorting_execution_time",
    description="Tempo de execução dos algoritmos de ordenação",
)
 
comparisons = meter.create_counter(
    name="sorting_comparisons",
    description="Número de comparações realizadas pelos algoritmos",
)
 
swaps = meter.create_counter(
    name="sorting_swaps",
    description="Número de trocas realizadas pelos algoritmos",
)
 
 
# Interface para o padrão Strategy
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass
 
 
# Implementação do Bubble Sort
class BubbleSort(SortingStrategy):
    def sort(self, data):
        start_time = time.time()
        n = len(data)
        swap_count = 0
        comparison_count = 0
 
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                comparison_count += 1
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    swap_count += 1
                    swapped = True
            if not swapped:
                break
 
        execution_time.record(time.time() - start_time)
        comparisons.add(comparison_count)
        swaps.add(swap_count)
        return data
 
 
# Implementação do QuickSort
class QuickSort(SortingStrategy):
    def sort(self, data):
        start_time = time.time()
        comparison_count = [0]
        swap_count = [0]
 
        def quicksort(arr, low, high):
            if low < high:
                pi, comp, swaps = partition(arr, low, high)
                comparison_count[0] += comp
                swap_count[0] += swaps
                quicksort(arr, low, pi-1)
                quicksort(arr, pi+1, high)
 
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            comparisons = 0
            swaps = 0
 
            for j in range(low, high):
                comparisons += 1
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
            arr[i+1], arr[high] = arr[high], arr[i+1]
            swaps += 1
            return i+1, comparisons, swaps
 
        quicksort(data, 0, len(data) - 1)
 
        execution_time.record(time.time() - start_time)
        comparisons.add(comparison_count[0])
        swaps.add(swap_count[0])
        return data
 
 
# Função para executar a ordenação com uma estratégia específica
def execute_sorting(strategy: SortingStrategy, data):
    return strategy.sort(data)