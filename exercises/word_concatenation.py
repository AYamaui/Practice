"""
An array of N words is given. Each word consists of small letters ('a' − 'z'). Our goal is to concatenate the words in such a way as to obtain a single word with the longest possible substring composed of one particular letter. Find the length of such a substring.

Write a function:

def solution(words)

that, given an array words containing N strings, returns the length of the longest substring of a word created as described above.

Examples:

1. Given N=3 and words=["aabb", "aaaa", "bbab"], your function should return 6. One of the best concatenations is words[1] + words[0] + words[2] = "aaaaaabbbbab". The longest substring is composed of letter 'a' and its length is 6.

2. Given N=3 and words=["xxbxx", "xbx", "x"], your function should return 4. One of the best concatenations is words[0] + words[2] + words[1] = "xxbxxxxbx". The longest substring is composed of letter 'x' and its length is 4.

3. Given N=4 and words=["dd", "bb", "cc", "dd"], your function should return 4. One of the best concatenations is words[0] + words[3] + words[1] + words[2] = "ddddbbcc". The longest substring is composed of letter 'd' and its length is 4.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
all the words are non−empty and consist only of lowercase letters (a−z);
S denotes the sum of the lengths of words; S is an integer within the range [1..100,000].
"""


def categorize_words(words):
    same_letter_words = {}
    first_letter_words = {}
    last_letter_words = {}
    letters = set()

    for idx, word in enumerate(words):

        first_letter = word[0]
        last_letter = word[-1]
        letters.add(first_letter)
        letters.add(last_letter)
        first_letter_count = 0
        last_letter_count = 0

        for letter in word:
            if letter == first_letter:
                first_letter_count += 1
            else:
                break

        for i in range(len(word) - 1, -1, -1):
            if word[i] == last_letter:
                last_letter_count += 1
            else:
                break

        if first_letter_count == len(word):
            same_letter_words.setdefault(word[0], [])
            same_letter_words[word[0]].append((idx, len(word)))
        else:
            first_letter_words.setdefault(word[0], [])
            last_letter_words.setdefault(word[-1], [])

            first_letter_words[word[0]].append((idx, first_letter_count))
            last_letter_words[word[-1]].append((idx, last_letter_count))

    return letters, first_letter_words, same_letter_words, last_letter_words


def solution(words):
    max_substring_length = 0
    max_substring_letter = None

    letters, first_letter_words, same_letter_words, last_letter_words = categorize_words(words)

    for letter in letters:
        idx, length = max(last_letter_words.get(letter, []), key=lambda x: x[1], default=(None, 0))
        substring_length = (length +
                            sum(length for _, length in same_letter_words.get(letter, [])) +
                            max(first_letter_words.get(letter, []),
                                key=lambda x: x[1] if x[0] != idx else 0, default=(None, 0))[1])

        if substring_length > max_substring_length:
            max_substring_length = substring_length
            max_substring_letter = letter

    for letter in letters:
        idx, length = max(first_letter_words.get(letter, []), key=lambda x: x[1], default=(None, 0))
        substring_length = (max(last_letter_words.get(letter, []),
                                key=lambda x: x[1] if x[0] != idx else 0, default=(None, 0))[1] +
                            sum(length for _, length in same_letter_words.get(letter, [])) +
                            length)

        if substring_length > max_substring_length:
            max_substring_length = substring_length
            max_substring_letter = letter

    return max_substring_letter, max_substring_length


if __name__ == '__main__':
    # words = ["aabb", "aaaa", "bbab"]
    # words = ["xxbxx", "xbx", "x"]
    # words = ["dd", "bb", "cc", "dd"]
    # words = ['a', 'b', 'c']
    # words = ["aabb", "ccccc", "bbaa"]
    # words = ["aabb", "ab", "bbaaccccc"]
    words = ["aaaaabb", "ab", "bbaacc"]

    print(solution(words))
