from dataclasses import dataclass

from ..exceptions.base import MoriLintException


@dataclass
class MessageHearthMissingError(MoriLintException):
    hearth_count: int

    @property
    def message(self) -> str:
        return super().message % f"В сообщении должно быть минимум {self.hearth_count} сердечек."
