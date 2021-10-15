from __future__ import annotations
from abc import ABC, abstractmethod


class Company(ABC):

    @abstractmethod
    def execute(self, driver) -> str:
        pass
