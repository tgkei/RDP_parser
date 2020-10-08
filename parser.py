from error import print_error


class Parser:
    def __init__(self, scanner):
        self.scanner = scanner
        self.is_matched = False

    def pD(self):
        next_symbol = self.scanner.get_next_symbol()

        if self._p_label(next_symbol):
            self._pL()
        elif self._p_integer(next_symbol):
            self._pL()
        else:
            print_error(1)

    def _pL(self):
        next_symbol = self.scanner.get_next_symbol()
        if self._p_id(next_symbol):
            self._pR()
        else:
            print_error(2)

    def _pR(self):
        next_symbol = self.scanner.get_next_symbol()
        if self._p_comma(next_symbol):
            self._pL()
        elif self._p_semicolon(next_symbol):
            if not self.scanner.is_finished():
                print_error(4)
            else:
                self.is_matched = True
        else:
            print_error(3)

    def _p_label(self, symbol):
        return symbol == "label"

    def _p_integer(self, symbol):
        return symbol == "integer"

    def _p_id(self, symbol):
        for keyword in ["label", "integer"]:
            if symbol == keyword:
                return False

        alpha = "abcdefghijklmnopqrstuvwxyz"

        for letter in symbol:
            if letter not in alpha + alpha.upper():
                return False

        return True

    def _p_semicolon(self, symbol):
        return symbol == ';'

    def _p_comma(self, symbol):
        return symbol == ','
