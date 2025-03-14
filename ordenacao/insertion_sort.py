from .strategy import SortStrategy

class InsertionSort(SortStrategy):
    """Implementação do Insertion Sort."""

    def sort(self, data):
        comparacoes = 0
        trocas = 0

        for i in range(1, len(data)):
            chave = data[i]
            j = i - 1
            comparacoes += 1

            while j >= 0 and data[j] > chave:
                data[j + 1] = data[j]
                j -= 1
                trocas += 1
                comparacoes += 1
            
            data[j + 1] = chave

        return data, comparacoes, trocas
