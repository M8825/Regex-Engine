def check_word(reg, text):

    if not reg:
        return True
    if not text:
        if reg == '$':
            return True
        return False

    if reg[0] == '\\':
        reg = reg[1:]

    if reg[0] != text[0] and reg[0] != '.':
        if reg[1:2] in ['?', '*']:  # matches the preceding character zero times
            return check_word(reg[2:], text)
        return False

    if reg[1:2] == '?':  # matches the preceding character once
        return check_word(reg[2:], text[1:])

    if reg[1:2] == '*' and reg[0] != '\\': # col.*r|colr
        # matches the preceding character once or more times
        return check_word(reg[2:], text) or check_word(reg, text[1:])

    if reg[1:2] == '+' and reg[0] != '\\':
        # matches the preceding character once or more times
        return check_word(reg[2:], text[1:]) or check_word(reg, text[1:])

    return check_word(reg[1:], text[1:])


def check_string(reg, text):
    if not reg:
        return True
    elif not text or len(text) < len(reg.replace('?','').replace('*','').replace('+','').replace('$','')) - 1:
        return False

    if reg.startswith('^'):
        return check_word(reg.lstrip('^'), text)

    if check_word(reg, text):
        return True
    else:
        return check_string(reg, text[1:])


regex, string = input().split('|')
print(check_string(regex, string))