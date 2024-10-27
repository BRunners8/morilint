import string
import logging
import re

from src.mori_lint.domain.constants import HEARTS, REQUIRED_KEYWORDS
from src.mori_lint.domain.exceptions import (
    MoriLintException,
    MessageTooShortError,
    MessageRequiredKeywordMissingError,
    MessageHearthMissingError
)
from src.mori_lint.infrastructure.logger.logger import configure_logger

configure_logger()

logger = logging.getLogger("__mori__")


class MoriLinter:
    def __init__(
        self,
        message_length: int = 79,
        req_keyword: tuple[str] = REQUIRED_KEYWORDS
    ) -> None:
        self.message_length = message_length
        self.req_keyword = req_keyword

    def __call__(self, message: str, **kwargs) -> None:
        clean_message: str = self.clear_message(message)
        if not self.validate_length(clean_message):
            raise MessageTooShortError(len(clean_message), self.message_length)
        if not self.validate_required_keywords(clean_message):
            raise MessageRequiredKeywordMissingError(self.req_keyword)
        if not self.validate_hearts_exclude(clean_message):
            raise MessageHearthMissingError()

    def validate_required_keywords(self, clean_message) -> bool:
        pattern = re.compile(r'\b(' + '|'.join(map(re.escape, self.req_keyword)) + r')\b', re.IGNORECASE)
        return pattern.search(clean_message) is not None

    def validate_length(self, clean_message: str) -> bool:
        return len(clean_message.split()) < self.message_length

    @staticmethod
    def validate_hearts_exclude(clean_message: str) -> bool:
        heart_pattern = re.compile("|".join(re.escape(heart) for heart in HEARTS))
        return bool(heart_pattern.search(clean_message))

    @staticmethod
    def clear_message(message: str) -> str:
        return message.translate(
            str.maketrans('', '', string.punctuation)
        ).replace("  ", " ")


linter = MoriLinter()

try:
    linter("Привет, денис,    пенис, !!??:?* милая" * 20)
except MoriLintException as e:
    logger.error(e.message)
else:
    logger.info("Проверки успешно пройдены!")
