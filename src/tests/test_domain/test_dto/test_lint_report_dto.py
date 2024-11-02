from dataclasses import FrozenInstanceError

import pytest

from src.morilint.domain.dto import LintReportDTO


class TestLintReportDTO:
    def test_create(self):
        d = LintReportDTO(
            total_checks=5,
            success=3,
            fail=2,
            failed_checks_detail=[
                "Что-то пошло не так..."
            ]
        )
        assert d.total_checks == 5
        assert d.success == 3
        assert d.fail == 2
        assert d.failed_checks_detail == [
                "Что-то пошло не так..."
            ]

    def test_mutable(self):
        d = LintReportDTO(
            total_checks=5,
            success=3,
            fail=2,
            failed_checks_detail=[
                "Что-то пошло не так..."
            ]
        )
        with pytest.raises(FrozenInstanceError):
            d.fail = 10
