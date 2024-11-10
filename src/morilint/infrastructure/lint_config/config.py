from dataclasses import dataclass

from ...domain.constants import REQUIRED_KEYWORDS, HEARTS


@dataclass
class LintConfig:
    message_length: int = 34
    req_keywords: list[str] = REQUIRED_KEYWORDS
    hearts: frozenset[str] = HEARTS
    min_hearts_count: int = 1

    check_length: bool = True
    check_keyword: bool = True
    check_hearts: bool = True
