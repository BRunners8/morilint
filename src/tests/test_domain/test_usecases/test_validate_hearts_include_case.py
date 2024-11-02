import pytest

from src.morilint.domain.exceptions import MessageHearthMissingError


class TestValidateHeartsIncludeCase:
    def test_call_success(self, validate_hearts_include_case, msg_correct):
        assert validate_hearts_include_case(msg_correct) is None

    def test_call_failed_no_hearths(self, validate_hearts_include_case, msg_no_hearts):
        with pytest.raises(MessageHearthMissingError):
            validate_hearts_include_case(msg_no_hearts)

    def test_call_failed_hearts_not_enough(self, validate_hearts_include_case, msg_hearts_not_enough):
        with pytest.raises(MessageHearthMissingError):
            validate_hearts_include_case(msg_hearts_not_enough)
