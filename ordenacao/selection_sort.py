from .strategy import SortStrategy

class SelectionSort(SortStrategy):
    """Implementação do Selection Sort."""

    def sort(self, data):
        comparacoes = 0
        trocas = 0
        n = len(data)

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                comparacoes += 1
                if data[j] < data[min_idx]:
                    min_idx = j

            if min_idx != i:
                data[i], data[min_idx] = data[min_idx], data[i]
                trocas += 1

        return data, comparacoes, trocas
