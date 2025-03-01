from argparse import _HelpAction, ArgumentParser, HelpFormatter, SUPPRESS


class CustomHelpAction(_HelpAction):
    def __init__(
        self,
        option_strings,
        dest=SUPPRESS,
        default=SUPPRESS,
        help=None,
        deprecated=False,
    ):
        super().__init__(option_strings, dest, default, help, deprecated)


class CustomHelpFormatter(HelpFormatter):
    def __init__(self, prog, indent_increment=2, max_help_position=50, width=None):
        super().__init__(prog, indent_increment, max_help_position, width)


class PassJennyArgumentParser:
    def __init__(self):
        self.parser = ArgumentParser(
            prog="passjenny",
            description="""
                PassJenny is an easy-to-use and customizable CLI passphrase
                generator.""",
            add_help=False,
            formatter_class=CustomHelpFormatter,
        )
        self._add_arguments()

    def _add_arguments(self):
        self.parser.add_argument(
            "-h", "--help", action=CustomHelpAction, help="Show this help menu and exit"
        )
        self.parser.add_argument(
            "-s", "--separator", type=str, help="Set separator character(s)"
        )
        self.parser.add_argument(
            "-w",
            "--num-words",
            dest="num_words",
            type=int,
            default=3,
            help="Set number of words",
        )

        bool_tags = {"default": True, "action": "store_false"}
        self.parser.add_argument(
            "--no-cap", dest="capitalize", help="Don't capitalize words", **bool_tags
        )
        self.parser.add_argument(
            "--no-num", dest="include_num", help="Don't include number", **bool_tags
        )

    def parse_args(self):
        return self.parser.parse_args()
