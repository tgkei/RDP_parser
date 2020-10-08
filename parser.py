from error import print_error


class Parser:
    def __init__(self, scanner):
        self.scanner = scanner
        self.is_matched = False
        self.next_symbol = scanner.get_next_symbol()

    def pD(self):
        if self._p_label():
            self._pL()
        elif self._p_integer():
            self._pL()
        else:
            print_error(1)

    def _is_id(self):
        for keyword in ["label", "integer"]:
            if self.next_symbol == keyword:
                return False

        alpha = "abcdefghijklmnopqrstuvwxyz"

        for letter in self.next_symbol:
            if letter not in alpha + alpha.upper():
                return False

        return True

    def _pL(self):
        if self._is_id():
            self._p_id()
            self._pR()
        else:
            print_error(2)

    def _pR(self):
        if self._p_comma():
            self._pL()
        elif self._p_semicolon():
            if self.next_symbol != "$":
                print_error(4)
            else:
                self.is_matched = True
        else:
            print_error(3)

    def _p_label(self):
        if self.next_symbol == 'label':
            self.next_symbol = self.scanner.get_next_symbol()
            return True
        return False

    def _p_integer(self):
        if self.next_symbol == "integer":
            self.next_symbol = self.scanner.get_next_symbol()
            return True
        return False

    def _p_id(self):
        if self._is_id():
            self.next_symbol = self.scanner.get_next_symbol()

    def _p_semicolon(self):
        if self.next_symbol == ';':
            self.next_symbol = self.scanner.get_next_symbol()
            return True
        return False

    def _p_comma(self):
        if self.next_symbol == ',':
            self.next_symbol = self.scanner.get_next_symbol()
            return True
        return False


class Parser2:
    def __init__(self, scanner):
        self.scanner = scanner
        self.is_matched = False
        self.next_symbol = scanner.get_next_symbol()

    def pD(self):
        if self.next_symbol in ["label", "integer"]:
            self.next_symbol = self.scanner.get_next_symbol()
            self._pL()
        else:
            print_error(1)

    def _is_id(self):
        for keyword in ["label", "integer"]:
            if self.next_symbol == keyword:
                return False

        alpha = "abcdefghijklmnopqrstuvwxyz"

        for letter in self.next_symbol:
            if letter not in alpha + alpha.upper():
                return False

        return True

    def _pL(self):
        if self._is_id():
            self.next_symbol = self.scanner.get_next_symbol()
            self._pR()
        else:
            print_error(2)

    def _pR(self):
        if self.next_symbol == ',':
            self.next_symbol = self.scanner.get_next_symbol()
            self._pL()
        elif self.next_symbol == ";":
            self.next_symbol = self.scanner.get_next_symbol()
            if self.next_symbol != "$":
                print_error(4)
            else:
                self.is_matched = True
        else:
            print_error(3)


PARSER = {
    1: Parser,
    2: Parser2
}
