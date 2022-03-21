from re import match


def match_it(regex, chars):
    """
    Recursion function. Returns True if every character in regular expression
    and in string match.

    :param regex: Regular expression.
    :param chars: String to match the regex
    :return: True or False
    """
    if not regex:
        return True
    elif not chars:
        return False
    is_same = bool(match(regex[0], chars[0]))

    if is_same:
        return match_it(regex[1:], chars[1:])

    return False


def slice_string(regex, chars):
    """
    Recursion function. Calls itself until length of the string is 0. or
    returns True if Regexp and String match.

    :param regex: Regular expression.
    :param chars: String to match the regex
    :return: True or False
    """
    if not regex:  # In case if empty regexp
        return True
    elif not chars:
        return False
    elif match_it(regex, chars):
        return True

    return slice_string(regex, chars[1:])


def main():
    regex, chars = input().split('|')
    print(slice_string(regex, chars))


if __name__ == '__main__':
    main()
