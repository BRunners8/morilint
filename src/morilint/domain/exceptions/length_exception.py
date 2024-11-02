from dataclasses import dataclass

from ..exceptions.base import MoriLintException


@dataclass
class MessageTooShortError(MoriLintException):
    msg_length: int
    permissible_length: int

    @property
    def message(self) -> str:
        return (
                super().message %
                f"Длина сообщения(слов) {self.msg_length} | Минимально-допустимая длина {self.permissible_length}"
        )
