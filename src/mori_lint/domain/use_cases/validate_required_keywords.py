import re

from src.mori_lint.domain.exceptions import MessageRequiredKeywordMissingError
from src.mori_lint.domain.use_cases.base import MoriLintCase


class ValidateRequiredKeywordsCase(MoriLintCase):
    """
    В сообщении должно быть хотя-бы одно
    обязательное ключевое слово
    """

    def __call__(self, clean_message: str) -> bool:
        pattern = re.compile(
            r'\b(' + '|'.join(map(re.escape, self.lint_config.req_keywords)) + r')\b',
            re.IGNORECASE
        )
        if pattern.search(clean_message) is None:
            raise MessageRequiredKeywordMissingError(self.lint_config.req_keywords)
