import argparse

from ...infrastructure.lint_config.config import LintConfig


class CommandLineParser:
    @classmethod
    def read_line_args(cls) -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            description="Чтение и обработка .mori файлов в указанной директории."
        )
        parser.add_argument(
            'directory',
            type=str,
            help="Путь к директории для поиска .mori файлов"
        )

        # Для дополнительных аргументов
        parser.add_argument(
            '--message_length',
            type=int,
            default=79,
            help="Максимальная длина сообщения"
        )
        parser.add_argument(
            '--min_hearts_count',
            type=int, default=1,
            help="Минимальное количество сердечек"
        )

        parser.add_argument(
            '--req_keywords',
            type=lambda s: list(s.split(',')),
            default=list(),
            help="Список обязательных ключевых слов, разделённых запятыми"
        )
        parser.add_argument(
            '--hearts',
            type=lambda s: frozenset(s.split(',')),
            default=frozenset(),
            help="Множество эмодзи сердечек, разделённых запятыми"
        )

        parser.add_argument(
            '--check_length',
            dest='check_length',
            action='store_const',
            const=True,
            default=None,
            help="Включить проверку длины"
        )
        parser.add_argument(
            '--no-check_length',
            dest='check_length',
            action='store_const',
            const=False,
            help="Отключить проверку длины"
        )
        parser.add_argument(
            '--check_keyword',
            dest='check_keyword',
            action='store_const',
            const=True,
            default=None,
            help="Включить проверку ключевых слов"
        )
        parser.add_argument(
            '--no-check_keyword',
            dest='check_keyword',
            action='store_const',
            const=False,
            help="Отключить проверку ключевых слов"
        )
        parser.add_argument(
            '--check_hearts',
            dest='check_hearts',
            action='store_const',
            const=True,
            default=None,
            help="Включить проверку сердечек"
        )
        parser.add_argument(
            '--no-check_hearts',
            dest='check_hearts',
            action='store_const',
            const=False,
            help="Отключить проверку сердечек"
        )

        return parser.parse_args()

    @classmethod
    def get_config(cls) -> tuple[str, LintConfig]:
        config: LintConfig = LintConfig()
        command_line_args: argparse.Namespace = cls.read_line_args()
        if command_line_args.message_length is not None:
            config.message_length = command_line_args.message_length
        if command_line_args.min_hearts_count is not None:
            config.min_hearts_count = command_line_args.min_hearts_count
        if len(command_line_args.req_keywords):
            config.req_keywords = command_line_args.req_keywords
        if len(command_line_args.hearts):
            config.hearts = command_line_args.hearts
        if command_line_args.check_length is not None:
            config.check_length = command_line_args.check_length
        if command_line_args.check_keyword is not None:
            config.check_keyword = command_line_args.check_keyword
        if command_line_args.check_hearts is not None:
            config.check_hearts = command_line_args.check_hearts

        return command_line_args.directory, config
