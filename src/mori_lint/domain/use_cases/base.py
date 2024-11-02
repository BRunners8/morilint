from abc import ABC

from ..interfaces.lint_config import ILintConfig


class MoriLintCase(ABC):
    def __init__(self, lint_config: ILintConfig) -> None:
        self.lint_config = lint_config

    def __call__(self, *args, **kwargs):
        raise NotImplementedError
