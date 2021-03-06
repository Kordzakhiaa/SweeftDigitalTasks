"""
Bomberman lives in a rectangular grid. Each cell in the grid either contains a bomb or nothing at all.
Each bomb can be planted in any cell of the grid but once planted, it will detonate after exactly 3 seconds.
Once a bomb detonates, it's destroyed — along with anything in its four neighboring cells.
This means that if a bomb detonates in cell i, j, any valid cells ( i ± 1, j ) and ( i, j ± 1 )  are cleared.
If there is a bomb in a neighboring cell, the neighboring bomb is destroyed without detonating,
so there's no chain reaction.
Bomberman is immune to bombs, so he can move freely throughout the grid. Here's what he does:
1.  Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
2.  After one second, Bomberman does nothing.
3.  After one more second, Bomberman plants bombs in all cells without bombs,
    thus filling the whole grid with bombs. No bombs detonate at this point.
4.  After one more second, any bombs planted exactly three seconds ago will detonate.
    Here, Bomberman stands back and observes.
5.  Bomberman then repeats steps 3 and 4 indefinitely.
Note that during every second Bomberman plants bombs, the bombs are planted simultaneously
(i.e., at the exact same moment), and any bombs planted at the same time will detonate at the same time.
Given the initial configuration of the grid with the locations of Bomberman's first batch of planted bombs,
determine the state of the grid after N seconds.
For example, if the initial grid looks like:
. . .
. O .
. . .
It looks the same after the first second. After the second second, Bomberman has placed all his charges:
O O O
O O O
O O O
At the third second, the bomb in the middle blows up, emptying all surrounding cells:
O . O
. . .
O . O
Function Description
Create the bomber_man function with following parameter(s):
●   int n: the number of seconds to simulate
●   string grid[r]: an array of string that represents the grid
<<<Returns>>>
●	string[r]: n array of string that represent the grid in its final state
<<<Sample Input>>>
3
. . . . . . .
. . . O . . .
. . . . O . .
. . . . . . .
OO . . . . .
OO . . . . .
<<<Sample Output>>>
OOO . OOO
OO . . . OO
OOO . . . O
. . OO . OO
. . . OOOO
. . . OOOO
"""
from typing import List


def print_output(r: int, c: int, n: int, grid: list) -> None:
    """
    :type r: :type int
    :type c: :type int
    :type n: :type int
    :type grid: :type list

    :return -> None
    """
    if n % 2 == 0:
        print('\n'.join('O' * c for _ in range(r)))
        return
    m = 2 * max(r, c)
    if n > m:
        n = m + (n - m) % 4
    for i in range(n // 2):
        grid = bomber_man(r, c, n, grid)
    print('\n'.join(''.join(g) for g in grid))


def bomber_man(r: int, c: int, n: int, grid) -> List[list]:
    """

    :type r: :type int
    :type c: :type int
    :type n: :type int
    :param grid:
    :return: g :type List[List]
    """
    g = [list('O' * c) for _ in range(r)]
    for y in range(r):
        for index, item in enumerate(grid[y]):
            if item == '.':
                continue
            g[y][index] = '.'
            if y > 0:
                g[y - 1][index] = '.'
            if y < r - 1:
                g[y + 1][index] = '.'
            if index > 0:
                g[y][index - 1] = '.'
            if index < c - 1:
                g[y][index + 1] = '.'
    return g


def main() -> None:
    r, c, n = input().split(' ')
    r, c, n = int(r), int(c), int(n)

    grid = [input(":?") for _ in range(r)]

    print_output(r, c, n, grid)


if __name__ == '__main__':
    """ Driver Code """
    main()
