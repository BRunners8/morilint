def main():
    from .infrastructure.logger.logger import configure_logger
    from .presentation.utils.command_line_parser import CommandLineParser
    from .presentation.api.file_linter.mori_file_linter import MoriFileLinter

    configure_logger()
    directory, config = CommandLineParser.get_config()
    linter = MoriFileLinter(config=config)

    linter.lint(directory=directory)
