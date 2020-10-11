# def f(a, b):
#     if not a and not b:
#         return True
#     if not b:
#         return a.islower()
#     if not a:
#         return False
#     if (a[0].isupper()):
#         return False if a[0] != b[0] else f(a[1:], b[1:])
#     return f(a[0].upper() + a[1:], b) or f(a[1:], b)

def f(a, b):
    if not a and not b:
        return True
    if not b:
        return a.islower()
    if not a:
        return False
    if (a[0].isupper()):
        return False if a[0] != b[0] else f('', b)
    return f(a[0].upper() + a[1:], b) or f(a[1:], b)


# def abbreviation(a, b):
#     return 'YES' if f(a, b) else 'NO'

def abbreviation(a, b):
    dp = [[False for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    dp[0][0] = True

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if j != i:
                continue
            dp[j][i] = dp[j - 1][i - 1] and f(a[i - 1], b[j - 1])
    for j in range(len(dp)):
        print(dp[j])
    return 'YES' if f(a, b) else 'NO'


if __name__ == '__main__':
    # print(sys.getrecursionlimit())
    # sys.setrecursionlimit(10 ** 6)
    # print(sys.getrecursionlimit())
    # a = 'hHhAhhcahhacaccacccahhchhcHcahaahhchhhchaachcaCchhchcaccccchhhcaahhhhcaacchccCaahhaahachhacaahhaachhhaaaCalhhchaccaAahHcchcazhachhhaaahaahhaacchAahccacahahhcHhccahaachAchahacaahcahacaahcahacaHhccccaahaahacaachcchhahhacchahhhaahcacacachhahchcaAhhcaahchHhhaacHcacahaccccaaahacCHhChchhhahhchcahaaCccccahhcaachhhacaaahcaaaccccaacaaHachaahcchaahhchhhcahahahhcaachhchacahhahahahAahaAcchahaahcaaaaahhChacahcacachacahcchHcaahchhcahaachnachhhhcachchahhhacHhCcaHhhhcaCccccaaahcahacahchahcaachcchaachahhhhhhhhcahhacacCcchahccaaaaaHhhccaAaaaCchahhccaahhacaccchhcahhcahaahhgacahcahhchcaaAccchahhhaahhccaaHcchaccacahHahChachhcaaacAhacacaacacchhchchacchchcacchachacaahachccchhhaccahcacchaccaahaaaccccccaaaaaaaHhcahcchmcHchcchaaahaccchaaachchHahcaccaaccahcacacahAhaacaacaccaccaaacahhhcacAhaCchcaacCcccachhchchcchhchahchchahchchhchcacaachahhccacachaAhaaachchhchchchhaachahaahahachhaaaccacahhcacchhhaaachaaacAahhcachchachhhcacchacaaChCahhhccahChaachhcahacchanaaacchhhccacacchcahccchAcahacaaachhacchachccaaHacaacAhahcCh'
    # b = 'HAHHCHAACCCAHCHHAHHAHCACCHCCHHCAAHHCACCCAHHHACAAHHHHCHHCAHHAHHAAAHAACAAHAHHCAHAHACHACHCHACACHAAHHAAAHCAHHACACAACHHHCHAHCAHCHHHAHAHACCAAAHCHHCHHCCAACCCCAACHACAACAAHACHCHAHHACCHCAHHHAAACHACAACHCACACAHHCCHAHACCCACCAACHCHHHCCCCCHCCAHHCAAHHAHHHHHHHAACCCCAHCCAAAAAHHHAAAACCAHHCAHACACCHHCHAHAHHCHAACHHHHHCCHCCAHAHCHCAAACCACCCCHACCACHHACHHACACHACCAACCCCAAAAHHAHCHHHCCAHCCHACHHAHCCACACCHAHAAACACCCCAHCCAHACCCCCCHCCHHCHHHHCHCHCAHHHACHAHAACCCAAAACHAACAAAHHAAHAAAHACHHCACHCCHCHAACHACACHHCCCCCAHCACHAAAHCHCAHACAAC'
    a = 'AB'
    b = 'AB'
    print(abbreviation(a, b))
