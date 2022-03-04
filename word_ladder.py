from collections import deque
from string import ascii_letters
from typing import List


def word_ladder(begin: str, end: str, word_list: List[str]) -> int:
    words = set(word_list)
    queue = deque([begin])
    distance = 0
    while len(queue) > 0:
        distance += 1
        n = len(queue)
        for _ in range(n):
            current_word = queue.popleft()
            for i in range(len(current_word)):
                for letter in ascii_letters:
                    next_word = current_word[:i] + letter + current_word[i + 1:]
                    if next_word not in words:
                        continue
                    if next_word == end:
                        return distance
                    queue.append(next_word)
                    words.remove(next_word)
    return 0


if __name__ == '__main__':
    begin = 'cold'
    end = 'warm'
    word_list = 'cold  gold  cord  card  ward  warm  tard  sold'.split()
    res = word_ladder(begin, end, word_list)
    print(res)
