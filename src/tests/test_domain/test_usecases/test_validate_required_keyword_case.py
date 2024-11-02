import pytest

from src.morilint.domain.exceptions import MessageRequiredKeywordMissingError


class TestValidateRequiredKeywordsCase:
    def test_call_success(self, validate_required_keywords_case, msg_correct):
        assert validate_required_keywords_case(msg_correct) is None

    def test_call_message_required_keyword_missing(self, validate_required_keywords_case, msg_no_keywords):
        with pytest.raises(MessageRequiredKeywordMissingError):
            validate_required_keywords_case(msg_no_keywords)
