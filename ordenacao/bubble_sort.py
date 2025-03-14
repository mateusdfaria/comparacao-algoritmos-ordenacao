from .strategy import SortStrategy

class BubbleSort(SortStrategy):
    """Implementação do Bubble Sort."""

    def sort(self, data):
        n = len(data)
        comparacoes = 0
        trocas = 0
        for i in range(n):
            for j in range(0, n - i - 1):
                comparacoes += 1
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    trocas += 1
        return data, comparacoes, trocas
