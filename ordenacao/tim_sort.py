from .strategy import SortStrategy

class TimSort(SortStrategy):
    """Implementação do Tim Sort."""

    RUN = 32  # Tamanho dos subarrays para usar Insertion Sort

    def sort(self, data):
        comparacoes = [0]  # Lista para modificar dentro das funções
        trocas = [0]

        self._tim_sort(data, comparacoes, trocas)
        return data, comparacoes[0], trocas[0]

    def _insertion_sort(self, data, left, right, comparacoes, trocas):
        """Ordena pequenos blocos usando Insertion Sort."""
        for i in range(left + 1, right + 1):
            temp = data[i]
            j = i - 1
            while j >= left and data[j] > temp:
                comparacoes[0] += 1
                data[j + 1] = data[j]
                j -= 1
                trocas[0] += 1
            data[j + 1] = temp

    def _merge(self, data, left, mid, right, comparacoes, trocas):
        """Faz a fusão dos blocos ordenados."""
        left_part = data[left:mid + 1]
        right_part = data[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            comparacoes[0] += 1
            if left_part[i] <= right_part[j]:
                data[k] = left_part[i]
                i += 1
            else:
                data[k] = right_part[j]
                j += 1
                trocas[0] += 1
            k += 1

        while i < len(left_part):
            data[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            data[k] = right_part[j]
            j += 1
            k += 1

    def _tim_sort(self, data, comparacoes, trocas):
        """Implementação do Tim Sort."""
        n = len(data)

        # Aplica Insertion Sort em pequenos blocos
        for i in range(0, n, self.RUN):
            self._insertion_sort(data, i, min((i + self.RUN - 1), n - 1), comparacoes, trocas)

        size = self.RUN
        while size < n:
            for left in range(0, n, 2 * size):
                mid = left + size - 1
                right = min((left + 2 * size - 1), n - 1)

                if mid < right:
                    self._merge(data, left, mid, right, comparacoes, trocas)

            size *= 2
