from abc import ABC, abstractmethod


class TransformationStep(ABC):
    @abstractmethod
    def apply(self, record):
        """Apply transformation and return transformed record, or None if invalid."""
        pass
