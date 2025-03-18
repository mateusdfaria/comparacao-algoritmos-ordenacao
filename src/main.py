import time
from data_generator import gerar_dados, ler_dados
from context import Contexto
from bubble_sort import BubbleSort
from quick_sort import QuickSort
from merge_sort import MergeSort
from metrics import iniciar_servidor_prometheus, registrar_metricas

def testar_algoritmo(contexto, dados, nome):
    inicio = time.time()
    resultado, comparacoes, trocas = contexto.executar_ordenacao(dados)
    tempo = (time.time() - inicio) * 1000  # ms
    print(f"{nome}: {tempo:.2f}ms, Comparações: {comparacoes}, Trocas: {trocas}")
    registrar_metricas(nome, tempo, comparacoes, trocas)
    return {"nome": nome, "tempo": tempo, "comparacoes": comparacoes, "trocas": trocas}

if __name__ == "__main__":
    iniciar_servidor_prometheus(8000)
    gerar_dados(10000)
    dados = ler_dados()
    contexto = Contexto(BubbleSort())
    resultados = []
    resultados.append(testar_algoritmo(contexto, dados, "Bubble Sort"))
    contexto.set_strategy(QuickSort())
    resultados.append(testar_algoritmo(contexto, dados, "Quick Sort"))
    contexto.set_strategy(MergeSort())
    resultados.append(testar_algoritmo(contexto, dados, "Merge Sort"))