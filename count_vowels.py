def count_vowels_file(filename):
    # setup
    number_of_vowels = 0

    # calculation
    for one_line in open(filename):     # go through each line in the file
        for one_character in one_line:  # go through each character in the line
            if one_character in 'aeiou':
                number_of_vowels += 1

    # report -- return value
    return number_of_vowels


print(count_vowels_file('/etc/passwd'))
