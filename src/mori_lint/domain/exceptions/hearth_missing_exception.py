from dataclasses import dataclass

from src.mori_lint.domain.exceptions.base import MoriLintException


@dataclass
class MessageHearthMissingError(MoriLintException):
    @property
    def message(self) -> str:
        return super().message % f"В сообщении нет сердечка!"
