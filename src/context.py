from strategy import OrdenacaoStrategy

class Contexto:
    def __init__(self, strategy: OrdenacaoStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: OrdenacaoStrategy):
        self._strategy = strategy

    def executar_ordenacao(self, dados):
        return self._strategy.ordenar(dados.copy())