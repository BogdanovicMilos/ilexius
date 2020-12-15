
def vowels_count(arr):
    lowercase_array = arr.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = list(filter(lambda x: x in vowels, lowercase_array))
    return len(count)


if __name__ == '__main__':
    print(vowels_count('MILOS'))
    print(vowels_count('ilexius'))
    print(vowels_count('milos bogdanovic'))
