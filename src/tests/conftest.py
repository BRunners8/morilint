import pytest

from src.tests.msg_fixtures import (
    msg_correct,
    msg_incorrect,
    msg_too_short,
    msg_no_keywords,
    msg_no_hearts,
    msg_hearts_not_enough
)

from src.morilint.domain.use_cases import (
    ValidateHeartsIncludeCase,
    ValidateLengthCase,
    ValidateRequiredKeywordsCase
)


from src.morilint.infrastructure.lint_config.config import LintConfig
from src.morilint.presentation.api.base.mori_linter import MoriLinter


@pytest.fixture
def config() -> LintConfig:
    return LintConfig(
        message_length=30,
        req_keywords=["testword", "thewoooooorld"],
        hearts=frozenset(["❤️", "💖"]),
        min_hearts_count=2,
        check_length=True,
        check_keyword=True,
        check_hearts=True
    )


@pytest.fixture
def linter(config) -> MoriLinter:
    return MoriLinter(config=config)


@pytest.fixture
def validate_hearts_include_case(config) -> ValidateHeartsIncludeCase:
    return ValidateHeartsIncludeCase(config)


@pytest.fixture
def validate_length_case(config) -> ValidateLengthCase:
    return ValidateLengthCase(config)


@pytest.fixture
def validate_required_keywords_case(config) -> ValidateRequiredKeywordsCase:
    return ValidateRequiredKeywordsCase(config)
