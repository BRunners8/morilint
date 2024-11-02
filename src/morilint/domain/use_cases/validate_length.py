from ..exceptions import MessageTooShortError
from ..use_cases.base import MoriLintCase


class ValidateLengthCase(MoriLintCase):
    """
    Сообщение должно быть не менее, чем заданная длина
    """

    def __call__(self, clean_message: str) -> None:
        clean_message_len = len(clean_message.split())
        if clean_message_len < self.lint_config.message_length:
            raise MessageTooShortError(clean_message_len, self.lint_config.message_length)
