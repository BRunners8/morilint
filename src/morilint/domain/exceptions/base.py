class MoriLintException(Exception):
    @property
    def message(self) -> str:
        return "Lint Error: [%s]"
