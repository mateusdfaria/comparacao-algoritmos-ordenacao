# 📊 Comparação de Algoritmos de Ordenação

Este repositório contém a implementação e análise de desempenho de diversos algoritmos de ordenação em Python. Utilizamos o padrão **Strategy** para modularidade e o **Prometheus** para coleta de métricas.

---

## 🚀 Algoritmos Implementados
- Bubble Sort 🟡
- Bubble Sort Otimizado 🟡
- Insertion Sort 🟡
- Selection Sort 🟡
- Quick Sort 🔵
- Merge Sort 🔵
- Heap Sort 🔵
- Tim Sort 🟢 (mais eficiente)

🔵 **O(n log n) – Melhor desempenho**  
🟡 **O(n²) – Menos eficiente**

---

## 📂 Estrutura do Projeto
📦 sorting-algorithms ┣ 📜 sorting.py # Implementação dos algoritmos ┣ 📜 main.py # Execução e coleta de métricas ┣ 📜 README.md # Documentação do projeto ┗ 📜 requirements.txt # Dependências


---

## 🔧 Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
        git clone https://github.com/seu-usuario/sorting-algorithms.git
        cd sorting-algorithms
        pip install -r requirements.txt
        python main.py
        http://localhost:8000

🏗️ Implementação do Padrão Strategy
O padrão Strategy permite encapsular diferentes algoritmos de ordenação e torná-los intercambiáveis.

class SortingContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_sort(self, data):
        return self.strategy.sort(data.copy())

Exemplo de uso:
context = SortingContext(QuickSort())
sorted_data = context.execute_sort(data)


📊 Coleta e Visualização de Métricas
Utilizamos Prometheus para coletar métricas e Grafana para visualizá-las.

Métricas coletadas:
Tempo de execução
Número de comparações
Número de trocas
As métricas são expostas via HTTP em http://localhost:8000.

🏆 Resultados e Conclusão
Tim Sort foi o algoritmo mais eficiente na maioria dos cenários.
Quick Sort teve bom desempenho, mas piorou para listas já ordenadas.
Bubble Sort foi o menos eficiente.
📌 Para listas grandes, algoritmos de divisão e conquista (Quick Sort e Merge Sort) são mais eficientes que métodos simples.