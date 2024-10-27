from dataclasses import dataclass

from src.mori_lint.domain.exceptions.base import MoriLintException


@dataclass
class MessageRequiredKeywordMissingError(MoriLintException):
    keywords: tuple[str]

    @property
    def message(self) -> str:
        return super().message % f"В сообщении НЕ содержатся обязательные слова/выражения: {self.keywords}"
