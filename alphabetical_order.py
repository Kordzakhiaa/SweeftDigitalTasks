def lex_order(word: str) -> str:
    """
    This function provides to order string in lexicographical(alphabetical) order

    :param word: :type -> String
    :return alphabetically ordered and reversed string:
    """
    n: int = len(word)
    x: int = n - 2
    word = list(word)

    while x >= 0 and word[x] >= word[x + 1]:
        x -= 1

    if x < 0:
        return 'No Answer'
    y = n - 1

    while y >= x and word[y] <= word[x]:
        y -= 1

    word[x], word[y] = word[y], word[x]  # noqa
    word = ''.join(word)

    return word[:x + 1] + word[x + 1:][::-1]


def test_lex_order():
    """ Function that tests lex_order function """
    assert lex_order('ab') == 'ba'
    assert lex_order('bb') == 'No Answer'
    assert lex_order('hefg') == 'hegf'
    assert lex_order('dkhc') == 'hcdk'
    assert len(lex_order('aa')) == 9
    assert type(lex_order('ab')) == str


if __name__ == '__main__':
    """Driver Code"""
    test_lex_order()
