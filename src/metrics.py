from prometheus_client import Counter, Histogram, start_http_server

COMPARACOES = Counter('sorting_comparisons_total', 'Total de comparações', ['algoritmo'])
TROCAS = Counter('sorting_swaps_total', 'Total de trocas', ['algoritmo'])
TEMPO = Histogram('sorting_execution_time_seconds', 'Tempo de execução (s)', ['algoritmo'])

def iniciar_servidor_prometheus(port=8000):
    start_http_server(port)
    print(f"Servidor Prometheus rodando em :{port}")

def registrar_metricas(nome, tempo, comparacoes, trocas):
    TEMPO.labels(algoritmo=nome).observe(tempo / 1000)  # ms para s
    COMPARACOES.labels(algoritmo=nome).inc(comparacoes)
    TROCAS.labels(algoritmo=nome).inc(trocas)