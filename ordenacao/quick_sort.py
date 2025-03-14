from .strategy import SortStrategy

class QuickSort(SortStrategy):
    """Implementação do Quick Sort."""

    def sort(self, data):
        comparacoes = [0]  # Usamos uma lista para modificar dentro da recursão
        trocas = [0]
        self._quick_sort(data, 0, len(data) - 1, comparacoes, trocas)
        return data, comparacoes[0], trocas[0]

    def _quick_sort(self, data, low, high, comparacoes, trocas):
        """Método auxiliar recursivo para Quick Sort."""
        if low < high:
            pi = self._partition(data, low, high, comparacoes, trocas)
            self._quick_sort(data, low, pi - 1, comparacoes, trocas)
            self._quick_sort(data, pi + 1, high, comparacoes, trocas)

    def _partition(self, data, low, high, comparacoes, trocas):
        """Função que realiza a partição do Quick Sort."""
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            comparacoes[0] += 1
            if data[j] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
                trocas[0] += 1
        data[i + 1], data[high] = data[high], data[i + 1]
        trocas[0] += 1
        return i + 1