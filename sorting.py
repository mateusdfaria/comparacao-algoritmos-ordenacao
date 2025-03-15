from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    """Classe base para os algoritmos de ordenação."""
    
    def __init__(self):
        self.comparisons = 0  # Contador de comparações
        self.swaps = 0        # Contador de trocas/movimentações

    @abstractmethod
    def sort(self, data):
        pass

    def get_metrics(self):
        """Retorna as métricas do algoritmo."""
        return {"comparisons": self.comparisons, "swaps": self.swaps}


class BubbleSort(SortingStrategy):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.comparisons += 1
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    self.swaps += 1
        return data


class BubbleSortOptimized(SortingStrategy):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                self.comparisons += 1
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    self.swaps += 1
                    swapped = True
            if not swapped:
                break
        return data


class InsertionSort(SortingStrategy):
    def sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                self.comparisons += 1
                data[j + 1] = data[j]
                j -= 1
                self.swaps += 1
            data[j + 1] = key
        return data


class SelectionSort(SortingStrategy):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.comparisons += 1
                if data[j] < data[min_idx]:
                    min_idx = j
            if min_idx != i:
                data[i], data[min_idx] = data[min_idx], data[i]
                self.swaps += 1
        return data


class QuickSort(SortingStrategy):
    def sort(self, data):
        def quicksort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quicksort(arr, low, pi - 1)
                quicksort(arr, pi + 1, high)

        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                self.comparisons += 1
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    self.swaps += 1
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            self.swaps += 1
            return i + 1

        quicksort(data, 0, len(data) - 1)
        return data


class MergeSort(SortingStrategy):
    def sort(self, data):
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                left = arr[:mid]
                right = arr[mid:]

                merge_sort(left)
                merge_sort(right)

                i = j = k = 0
                while i < len(left) and j < len(right):
                    self.comparisons += 1
                    if left[i] < right[j]:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    self.swaps += 1
                    k += 1

                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1
                    self.swaps += 1

                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1
                    self.swaps += 1

        merge_sort(data)
        return data


class HeapSort(SortingStrategy):
    def sort(self, data):
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n:
                self.comparisons += 1
                if arr[left] > arr[largest]:
                    largest = left

            if right < n:
                self.comparisons += 1
                if arr[right] > arr[largest]:
                    largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                self.swaps += 1
                heapify(arr, n, largest)

        n = len(data)
        for i in range(n // 2 - 1, -1, -1):
            heapify(data, n, i)

        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            self.swaps += 1
            heapify(data, i, 0)

        return data


class SortingContext:
    """Gerencia a estratégia de ordenação escolhida."""
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        """Permite alterar o algoritmo de ordenação dinamicamente."""
        self.strategy = strategy

    def execute_sort(self, data):
        """Executa a ordenação e retorna os dados ordenados junto com as métricas."""
        sorted_data = self.strategy.sort(data)
        metrics = self.strategy.get_metrics()
        return sorted_data, metrics