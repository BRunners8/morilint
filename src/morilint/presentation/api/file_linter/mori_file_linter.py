import logging
from pathlib import Path

from rich.table import Table
from rich.console import Console

from ....domain.constants import MORIFILE
from ....infrastructure.lint_config.config import LintConfig
from ....presentation.api.base.mori_linter import MoriLinter
from ....presentation.responses.lint_file_response import LintFilesResponse, LintFileData
from ....presentation.responses.lint_response import LintResponse

logger = logging.getLogger("__mori__")


class MoriFileLinter:
    def __init__(self, config: LintConfig = None) -> None:
        self.__linter = MoriLinter(config=config)
        self.__file_ext = MORIFILE
        self.__console = Console()

    @staticmethod
    def load_file(filepath: Path) -> str:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()

    def lint(self, directory: str, print_lint_result: bool = True) -> LintFilesResponse:
        try:
            files_lint_result: LintFilesResponse = self.lint_files_from_dir(directory)
            if print_lint_result:
                self.print_report_to_console(files_lint_result)
            return files_lint_result
        except Exception as e:
            logger.error(f"Во время проверки файлов произошла неизвестная ошибка: {e}")
            raise e

    def lint_files_from_dir(self, directory: str) -> LintFilesResponse:
        files_lint_result: list[LintFileData] = []
        directory = Path(directory)
        mori_files = directory.glob(self.__file_ext)
        total_files_checked: int = 0
        checked_filenames: list[str] = []
        problems_found: int = 0
        success: int = 0
        failed: int = 0

        for mori_file in mori_files:
            file_res: LintResponse = self.__linter.lint(
                self.load_file(mori_file)
            )
            files_lint_result.append(
                LintFileData(
                    filename=str(mori_file),
                    lint_detail=file_res
                )
            )
            if file_res.fail:
                failed += 1
                problems_found += len(file_res.failed_checks_detail)
            else:
                success += 1
            checked_filenames.append(str(mori_file))
            total_files_checked += 1

        return LintFilesResponse(
            total_files_checked=total_files_checked,
            checked_filenames=checked_filenames,
            problems_found=problems_found,
            success=success,
            failed=failed,
            detail=files_lint_result
        )

    def print_report_to_console(self, file_lint_response: LintFilesResponse) -> None:
        table = Table(title="Mori file lint report")
        table.add_column("Файл", justify="left", style="cyan", no_wrap=True)
        table.add_column("Успешно", style="green")
        table.add_column("Неуспешно", style="red")
        table.add_column("Детали", justify="left", style="bright_red")

        for f_data in file_lint_response.detail:
            table.add_row(
                f_data.filename,
                str(f_data.lint_detail.success),
                str(f_data.lint_detail.fail),
                f"-{
                    '\n-'.join(f_data.lint_detail.failed_checks_detail)
                }\n"
            )

        self.__console.print(table)
