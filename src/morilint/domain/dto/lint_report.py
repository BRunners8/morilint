from dataclasses import dataclass, field


@dataclass(frozen=True)
class LintReportDTO:
    total_checks: int
    success: int
    fail: int
    failed_checks_detail: list[str] = field(default_factory=list)
