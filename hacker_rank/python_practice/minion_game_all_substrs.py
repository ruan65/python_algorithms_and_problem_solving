def minion_game(s):
    v = 'AEIOU'
    stu, kev = 0, 0

    for i in range(len(s)):
        if s[i] in v:
            kev += len(s) - i
        else:
            stu += len(s) - i
    if stu > kev:
        print(f'Stuart {stu}')
    elif stu < kev:
        print(f'Kevin {kev}')
    else:
        print('Draw')


if __name__ == '__main__':
    minion_game('BANANANAAAS')
    # print(all_sub_strings('BANANANAAAS'))
