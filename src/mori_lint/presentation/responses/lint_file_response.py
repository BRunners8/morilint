from dataclasses import dataclass

from ..responses.lint_response import LintResponse


@dataclass(frozen=True)
class LintFileData:
    filename: str
    lint_detail: LintResponse


@dataclass(frozen=True)
class LintFilesResponse:
    total_files_checked: int
    checked_filenames: list[str]
    problems_found: int
    success: int
    failed: int
    detail: list[LintFileData]
