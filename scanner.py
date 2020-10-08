class Scanner:
    TERMINAL_SYMBOLS = ["label", "integer", ";", ","]

    def __init__(self, string):
        self.string = string
        self.idx = 0
        self.N = len(string)
        self.token = None

    def print_token(self):
        print(self.token)

    def tokenize(self):
        string = self.string
        token = []
        while string:
            while string and string[0] == " ":
                string = string[1:]

            if self._is_terminal(string):
                terminal, string = self._tokenize_terminal(string)
                token.append(terminal)

        self.token = token

    def _is_terminal(self, string):
        """
        args:
            string: str, left string
        return:
            boolean, True if string is nonterminal else False
        """
        for term_symbol in Scanner.TERMINAL_SYMBOLS:
            if string.startswith(term_symbol):
                return True
        if self._is_identifier(string):
            return True
        return False

    def _is_identifier(self, string):
        idx = 0
        nums = "0123456789"
        alphas = "abcdefghijklmnopqrstuvwxyz"
        while idx < len(string) and string[idx] in "_" + nums + alphas + alphas.upper():
            idx += 1

        if idx:
            return True

    def _tokenize_terminal(self, string):
        """
        args:
            string, str: left string
        ret:
            (terminal, substring), (str, str)
        """
        def tokenize_id(string):
            idx = 0
            nums = "0123456789"
            alphas = "abcdefghijklmnopqrstuvwxyz"
            while idx < len(string) and string[idx] in "_" + nums + alphas + alphas.upper():
                idx += 1
            assert idx != 0, ValueError("idx should bigger than 0")
            return string[:idx]

        for term_symbol in Scanner.TERMINAL_SYMBOLS:
            if string.startswith(term_symbol):
                ret_str = string[len(term_symbol):]
                return term_symbol, ret_str

        identifier = tokenize_id(string)
        ret_str = string[len(identifier):]
        return identifier, ret_str

    def get_next_symbol(self):
        if self.idx >= len(self.token):
            raise Exception("already iterated all tokens")

        ret = self.token[self.idx]
        self.idx += 1
        return ret

    def is_finished(self):
        return self.idx == len(self.token)
