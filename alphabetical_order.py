"""
Lexicographical order is often known as alphabetical order when dealing with strings.
A string is greater than another string if it comes later in a lexicographically sorted list.
Given a word, create a new word by swapping some or all of its characters.
This new word must meet two criteria:
●  It must be greater than the original word
●  It must be the smallest word that meets the first condition
Example w = abcd
------------------------------------------------------------------------------------------------------------------------------------------
The next largest word is abdc.
Create the function bigger_Is_greater and return the new string meeting the criteria. If it is not possible, return no answer.
Function Description
Function has the following parameter(s): string word: a word
Returns - string: the smallest lexicographically higher string possible or no answer
Input Format
The first line of input contains T, the number of test cases. Each of the next T lines contains w.
Constraints
●   	1 ≤ T ≤ 105
●   	1 ≤ length of w ≤ 100
●   	word will contain only letters in the range ascii[a...z]
Sample Input:
5
ab
bb
hefg
dhck
dkhc

Sample Output
ba
no answer
hegf
dhkc
hcdk
"""


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
