import re

from ..exceptions import MessageHearthMissingError
from ..use_cases.base import MoriLintCase


class ValidateHeartsIncludeCase(MoriLintCase):
    """
    В сообщении обязательно должны быть сердечки.
    Не менее, чем в заданной величине.
    """

    def __call__(self, clean_message: str) -> None:
        heart_pattern = re.compile(
            "|".join(re.escape(heart) for heart in self.lint_config.hearts)
        )
        if not self.lint_config.min_hearts_count <= len(heart_pattern.findall(clean_message)):
            raise MessageHearthMissingError(self.lint_config.min_hearts_count)
