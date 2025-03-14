from .strategy import SortStrategy

class MergeSort(SortStrategy):
    """Implementação do Merge Sort."""

    def sort(self, data):
        comparacoes = [0]  # Usamos uma lista para modificar dentro da recursão
        trocas = [0]
        sorted_data = self._merge_sort(data, comparacoes, trocas)
        return sorted_data, comparacoes[0], trocas[0]

    def _merge_sort(self, data, comparacoes, trocas):
        """Método recursivo para Merge Sort."""
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            left_half = self._merge_sort(left_half, comparacoes, trocas)
            right_half = self._merge_sort(right_half, comparacoes, trocas)

            return self._merge(left_half, right_half, comparacoes, trocas)
        else:
            return data

    def _merge(self, left, right, comparacoes, trocas):
        """Função que realiza a fusão das listas ordenadas."""
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparacoes[0] += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                trocas[0] += 1  # Troca ocorre na fusão

        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
