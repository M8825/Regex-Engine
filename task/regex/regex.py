from re import match


def match_it(regex, string):
    """
    Recursion function. Returns True if every character in regular exspressiona
    and in string matches.

    :param regex: Regular expression. String on the right side of '|'
    :param string:
    :return: True or False
    """
    if not regex:
        return True
    elif not string:
        return False
    is_same = bool(match(regex[0], string[0]))

    if is_same:
        return match_it(regex[1:], string[1:])

    return False


def main():
    regex, chars = input().split('|')
    result = match_it(regex, chars)
    print(result)


if __name__ == '__main__':
    main()
