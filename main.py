import random
from sorting import BubbleSort, QuickSort, execute_sorting
 
# Gerar uma lista de números aleatórios
data_size = 1000
data = [random.randint(1, 10000) for _ in range(data_size)]
 
# Criar instâncias das estratégias
bubble_sort = BubbleSort()
quick_sort = QuickSort()
 
# Executar algoritmos de ordenação
print("Executando Bubble Sort...")
sorted_data_bubble = execute_sorting(bubble_sort, data.copy())
 
print("Executando Quick Sort...")
sorted_data_quick = execute_sorting(quick_sort, data.copy())
 
print("Ordenação concluída. Métricas registradas no Prometheus.")