from opentelemetry import metrics

from opentelemetry.sdk.metrics import MeterProvider

from opentelemetry.exporter.prometheus import PrometheusMetricReader

from opentelemetry.sdk.metrics.export import ConsoleMetricExporter
 
# Configurar o leitor Prometheus

reader = PrometheusMetricReader()

meter_provider = MeterProvider(metric_readers=[reader])

metrics.set_meter_provider(meter_provider)

meter = metrics.get_meter(__name__)
 
# Criar uma métrica

execution_time = meter.create_histogram(

    name="sorting_execution_time",

    description="Tempo de execução dos algoritmos de ordenação",

)
 
# Simular coleta de dados

import time

import random
 
def run_sorting_algorithm():

    start_time = time.time()

    time.sleep(random.uniform(0.01, 0.1))  # Simulando execução do algoritmo

    execution_time.record(time.time() - start_time)
 
# Simulação contínua

while True:

    run_sorting_algorithm()

    time.sleep(1)

 