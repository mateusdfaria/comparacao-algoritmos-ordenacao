from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app, start_http_server
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from flask import Flask
 
# Configurar OpenTelemetry para Prometheus
reader = PrometheusMetricReader()
provider = MeterProvider(metric_readers=[reader])
 
# Criar o servidor Flask para expor métricas
app = Flask(__name__)
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})
 
if __name__ == "__main__":
    print("🔥 Servidor de métricas rodando em http://localhost:7070/metrics")
    start_http_server(7070)  # Expõe as métricas na porta 8000
    app.run(host="0.0.0.0", port=7070)