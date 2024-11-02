import logging

from ....domain.dto import LintReportDTO
from ....domain.services.mori_lint_service import MoriLintService
from ....infrastructure.lint_config.config import LintConfig
from ....presentation.responses.lint_response import LintResponse

logger = logging.getLogger("__mori__")


class MoriLinter:
    """
    Интерфейс взаимодействия с сервисом.
    Проверяет одно сообщение и возвращает данные о проверке.
    """
    def __init__(self, config: LintConfig = None) -> None:
        if config is None:
            config = LintConfig()
        self.__service = MoriLintService(lint_config=config)

    def lint(self, message: str) -> LintResponse:
        try:
            report: LintReportDTO = self.__service.lint(message=message)
        except Exception as e:
            logger.error(f"Во время проверки произошла неизвестная ошибка")
            raise e

        return LintResponse(
            total_checks=report.total_checks,
            success=report.success,
            fail=report.fail,
            failed_checks_detail=report.failed_checks_detail
        )
