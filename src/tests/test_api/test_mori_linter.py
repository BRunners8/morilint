from src.mori_lint.presentation.responses.lint_response import LintResponse


class TestMoriLinter:
    """
    Тест класса MoriLinter - основного публичного класса
    для проверки сообщения
    """
    def test_lint_success(self, linter, msg_correct):
        assert linter.lint(msg_correct) == LintResponse(
            total_checks=3,
            success=3,
            fail=0,
            failed_checks_detail=[]
        )

    def test_lint_failed(self, linter, msg_incorrect):
        assert linter.lint(msg_incorrect) == LintResponse(
            total_checks=3,
            success=0,
            fail=3,
            failed_checks_detail=[
                "Lint Error: [Длина сообщения(слов) 2 | Минимально-допустимая длина 30]",
                "Lint Error: [В сообщении НЕ содержатся обязательные слова/выражения: testword, thewoooooorld]",
                "Lint Error: [В сообщении должно быть минимум 2 сердечек.]",
            ]
        )

    def test_lint_failed_length(self, linter, msg_too_short):
        assert linter.lint(msg_too_short) == LintResponse(
            total_checks=3,
            success=2,
            fail=1,
            failed_checks_detail=[
                "Lint Error: [Длина сообщения(слов) 13 | Минимально-допустимая длина 30]"
            ]
        )

    def test_lint_failed_keywords(self, linter, msg_no_keywords):
        assert linter.lint(msg_no_keywords) == LintResponse(
            total_checks=3,
            success=2,
            fail=1,
            failed_checks_detail=[
                "Lint Error: [В сообщении НЕ содержатся обязательные слова/выражения: testword, thewoooooorld]"
            ]
        )

    def test_lint_failed_no_hearts(self, linter, msg_no_hearts):
        assert linter.lint(msg_no_hearts) == LintResponse(
            total_checks=3,
            success=2,
            fail=1,
            failed_checks_detail=[
                "Lint Error: [В сообщении должно быть минимум 2 сердечек.]"
            ]
        )

    def test_lint_failed_hearts_not_enough(self, linter, msg_hearts_not_enough):
        assert linter.lint(msg_hearts_not_enough) == LintResponse(
            total_checks=3,
            success=2,
            fail=1,
            failed_checks_detail=[
                "Lint Error: [В сообщении должно быть минимум 2 сердечек.]"
            ]
        )
