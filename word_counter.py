"""
--- Task 1 ---
You are given words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.
Note: Each input line ends with a "\n" character.
Constraints:
1 ≤ n ≤ 105
The sum of the lengths of all the words do not exceed 106
All the words are composed of lowercase English letters only.
Input Format
The first line contains the integer, n.
The next n lines each contain a word.
Output Format
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences
for each distinct word according to their appearance in the input.
Sample Input:
4 bcdef abcdefg bcde bcdef
Sample Output
3
2 1 1
"""


def count_words() -> None:
    """
    A function that ensures the completion of the first
    :input -> (quantity{4} - int) (I str) (II str) (III str) (IV str)
    :output ->
     3
     2 1 1
     :returns -> None
    """
    list_of_words: list = []  # EMPTY LIST
    input_quantity: int = int(input('Enter the number of words you are going to input: '))

    for i in range(input_quantity):
        user_input: str = input(f'Word - {i + 1}: ')
        list_of_words.append(user_input)

    counted_words: dict = {item: list_of_words.count(item) for item in list_of_words}  # DICT COMPREHENSION

    print(len(counted_words))  # PRINTING LENGTH OF DICTIONARY ITEMS
    print(' '.join(str(q) for _, q in counted_words.items()))  # PRINTING QUANTITY OF EACH ITEM


if __name__ == '__main__':
    """ Driver Code """
    count_words()
