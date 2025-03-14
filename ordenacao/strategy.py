from abc import ABC, abstractmethod

class SortStrategy(ABC):
    """Classe abstrata para os algoritmos de ordenação."""

    @abstractmethod
    def sort(self, data):
        """Método que será implementado pelos algoritmos concretos."""
        pass
