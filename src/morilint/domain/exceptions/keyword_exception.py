from dataclasses import dataclass

from ..exceptions.base import MoriLintException


@dataclass
class MessageRequiredKeywordMissingError(MoriLintException):
    keywords: list[str]

    @property
    def message(self) -> str:
        return super().message % f"В сообщении НЕ содержатся обязательные слова/выражения: {
            ', '.join(self.keywords)
        }"
