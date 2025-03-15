import random
import time
from sorting import (
    SortingContext, BubbleSort, BubbleSortOptimized, InsertionSort, SelectionSort, 
    QuickSort, MergeSort, HeapSort, CountingSort, RadixSort, ShellSort
)

def generate_data(size):
    """Gera uma lista de números aleatórios para teste."""
    return [random.randint(0, 100000) for _ in range(size)]

def measure_sorting_time(sorting_strategy, data):
    """Mede o tempo de execução e coleta métricas."""
    context = SortingContext(sorting_strategy)
    start_time = time.time()
    sorted_data, comparisons, swaps = context.execute_sort(data.copy())
    end_time = time.time()
    return sorted_data, (end_time - start_time) * 1000, comparisons, swaps  # Tempo em ms

def main():
    sizes = [1000, 10000]
    algorithms = [
        ("Bubble Sort", BubbleSort()),
        ("Bubble Sort Optimized", BubbleSortOptimized()),
        ("Insertion Sort", InsertionSort()),
        ("Selection Sort", SelectionSort()),
        ("Quick Sort", QuickSort()),
        ("Merge Sort", MergeSort()),
        ("Heap Sort", HeapSort()),
        # ("Counting Sort", CountingSort()),
        # ("Radix Sort", RadixSort()),
        # ("Shell Sort", ShellSort())
    ]
    
    for size in sizes:
        print(f"\nTestando com {size} elementos...")
        data = generate_data(size)
        
        for name, algorithm in algorithms:
            _, elapsed_time, comparisons, swaps = measure_sorting_time(algorithm, data)
            print(f"{name}: {elapsed_time:.2f} ms | Comparações: {comparisons} | Trocas: {swaps}")

if __name__ == "__main__":
    main()