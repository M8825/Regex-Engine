from re import match
# write your code here
usr_inp = input()

if not usr_inp:
    print(True)
elif len(usr_inp) < 3:
    if usr_inp[0] == '|':
        print(True)
    elif usr_inp[1] == '|':
        print(False)
else:
    result = bool(match(usr_inp[0], usr_inp[2]))
    print(result)
