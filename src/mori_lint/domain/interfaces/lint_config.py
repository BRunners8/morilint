from typing import Protocol, Tuple, FrozenSet


class ILintConfig(Protocol):
    message_length: int
    req_keywords: Tuple[str]
    hearts: FrozenSet[str]
    min_hearts_count: int
    # для выполнения только определённых проверок
    check_length: bool
    check_keyword: bool
    check_hearts: bool
