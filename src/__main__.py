if __name__ == "__main__":
    from src.mori_lint.presentation.utils.command_line_parser import CommandLineParser
    from src.mori_lint.presentation.api.file_linter.mori_file_linter import MoriFileLinter

    directory, config = CommandLineParser.get_config()
    linter = MoriFileLinter(
        directory=directory,
        config=config
    )

    linter.lint()
