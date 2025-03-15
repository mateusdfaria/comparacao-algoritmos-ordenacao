from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from prometheus_client import start_http_server
 
# Configurar o leitor Prometheus
reader = PrometheusMetricReader()
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)
meter = metrics.get_meter(__name__)
 
# Definir métricas
execution_time = meter.create_histogram(
    name="sorting_execution_time",
    description="Tempo de execução dos algoritmos de ordenação",
)
comparisons = meter.create_counter(
    name="sorting_comparisons",
    description="Número de comparações realizadas pelos algoritmos",
)
swaps = meter.create_counter(
    name="sorting_swaps",
    description="Número de trocas realizadas pelos algoritmos",
)
 
# Iniciar o servidor Prometheus para expor as métricas
start_http_server(8000)