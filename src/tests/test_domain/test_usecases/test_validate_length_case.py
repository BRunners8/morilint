import pytest

from src.mori_lint.domain.exceptions import MessageTooShortError


class TestValidateLengthCase:
    def test_call_success(self, validate_length_case, msg_correct):
        assert validate_length_case(msg_correct) is None

    def test_call_message_too_short(self, validate_length_case, msg_too_short):
        with pytest.raises(MessageTooShortError):
            validate_length_case(msg_too_short)

