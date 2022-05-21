'''
Remove Anagrams and Sort (from Fathom test 04/22)

Given an array of strings, remove each string that is an anagram of an earlier
string and return the remaining array in sorted order.
'''

def remove_anagrams_and_sort(text: list[str]) -> list[str]:
    sorted_set = set()
    anagramless = []
    for i in range(len(text)):
        sorted_string = ''.join(sorted(text[i]))
        if sorted_string not in sorted_set:
            sorted_set.add(sorted_string)
            anagramless.append(i)

    anagramless = list(map(lambda i: text[i], anagramless))
    anagramless.sort()
    return anagramless

if __name__ == '__main__':
    print(remove_anagrams_and_sort(['code', 'doce', 'ecod', 'framer', 'frame']))

