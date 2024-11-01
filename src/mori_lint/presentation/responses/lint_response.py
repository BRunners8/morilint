from dataclasses import dataclass, field


@dataclass(frozen=True)
class LintResponse:
    total_checks: int
    success: int
    fail: int
    failed_checks_detail: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        return (
            f"Проверка завершена {'успешно' if self.fail == 0 else 'неуспешно'}.\n"
            f"Проверок выполнено: {self.total_checks}\n"
            f"Успешно: {self.success}\n"
            f"Ошибки: {self.fail}\n"
            f"Детали по ошибкам: \n-{
                '\n-'.join(self.failed_checks_detail)
            }"
        )
