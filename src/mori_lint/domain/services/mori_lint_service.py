import string
from typing import TypeVar, List, Any

from src.mori_lint.domain.dto import LintReportDTO
from src.mori_lint.domain.exceptions import MoriLintException
from src.mori_lint.domain.interfaces.lint_config import ILintConfig
from src.mori_lint.domain.use_cases import (
    ValidateHeartsIncludeCase,
    ValidateLengthCase,
    ValidateRequiredKeywordsCase,
    MoriLintCase
)

T = TypeVar('T', bound=MoriLintCase)


class MoriLintService:
    def __init__(self, lint_config: ILintConfig) -> None:
        self.lint_config: ILintConfig = lint_config

    def lint(self, message: str) -> LintReportDTO:
        """
        Формирует список проверок, на основе конфигурации линтера.
        Передаёт проверки с заданными аргументами на выполнение и
        возвращает результат выполнения проверок.

        :param message: Сообщение от пользователя
        :return: Отчёт с данными о том, сколько всего
            было запущено проверок, сколько успешно/неуспешно, детали не прошедших проверок
        """

        clean_message: str = self.clear_message(message)
        lint_checks_cases: List[List[T | Any]] = []

        if self.lint_config.check_length:
            lint_checks_cases.append([ValidateLengthCase(self.lint_config), clean_message])
        if self.lint_config.check_keyword:
            lint_checks_cases.append([ValidateRequiredKeywordsCase(self.lint_config), clean_message])
        if self.lint_config.check_hearts:
            lint_checks_cases.append([ValidateHeartsIncludeCase(self.lint_config), clean_message])
        return self.__run_and_handle_checks(lint_case_and_args=lint_checks_cases)

    @staticmethod
    def __run_and_handle_checks(lint_case_and_args: List[List[T | Any]]) -> LintReportDTO:
        """
        Вызывает каждую проверку(коллбек) из списка lint_case_and_args с переданными аргументами.
        Обрабатывает возможные исключения, формирует и возвращает данные по проверкам.
        :param lint_case_and_args: Список, где первый элемент - коллбек,
            остальные - произвольное количество элементов для его вызова
        :return: LintReportDTO Отчёт с данными о том, сколько всего было запущено проверок,
            сколько успешно/неуспешно, детали не прошедших проверок
        """

        total = 0
        success = 0
        fail = 0
        failed_checks_detail = []
        for c in lint_case_and_args:
            try:
                total += 1
                c[0](*c[1:])
            except MoriLintException as e:
                fail += 1
                failed_checks_detail.append(e.message)
            else:
                success += 1
        return LintReportDTO(
            total_checks=total,
            success=success,
            fail=fail,
            failed_checks_detail=failed_checks_detail
        )

    @staticmethod
    def clear_message(message: str) -> str:
        """
        Принимает на вход сообщение, убирает из него все знаки препинания,
        лишние пробелы и возвращает очищенную строку.
        :param message: Исходное сообщение
        :return: строка без знаков препинания и лишних пробелов
        """
        return message.translate(
            str.maketrans("", "", string.punctuation)
        ).replace("  ", " ")
