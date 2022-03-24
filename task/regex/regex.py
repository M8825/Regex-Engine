from re import match


class RegexEngine:

    def __init__(self, regex, chars):
        self.regex = regex
        self.chars = chars

    def equal_length(self):
        """
        Recursive method to compare the entire regex and string

        :return: bool output of comparison
        """
        if not self.regex:
            return True
        elif not self.chars:
            return False
        is_same = bool(match(self.regex[0], self.chars[0]))

        if is_same:
            self.regex = self.regex[1:]
            self.chars = self.chars[1:]
            return self.equal_length()

        return False

    def unequal_string(self):
        """
        Recursive method to compare the entire regex and string

        :return: bool output of comparison
        """
        if not self.regex:  # In case of empty regex
            return True
        elif not self.chars:
            return False
        elif self.equal_length():
            return True
        self.chars = self.chars[1:]

        return self.unequal_string()

    def metacharacters(self):
        if self.regex.startswith('^') and self.regex.endswith('$'):
            self.regex = self.regex.strip('^').strip('$')

            return self.equal_length() if len(self.regex) == len(self.chars) \
                else False
        elif self.regex.startswith('^'):
            self.regex = self.regex.strip('^')

            return self.equal_length()
        elif self.regex.endswith('$'):
            self.regex = self.regex.strip('$')
            self.chars = self.chars[-len(self.regex):]

            return self.equal_length()
        else:
            return self.unequal_string()


def main():
    regex, chars = input().split('|')
    regexeng = RegexEngine(regex, chars)
    print(regexeng.metacharacters())


if __name__ == '__main__':
    main()
