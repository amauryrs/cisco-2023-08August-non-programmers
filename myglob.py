# import glob, the module that comes with Python (standard library).
# Ask the user to enter a globbing pattern.
# Use glob.glob to get the list of filenames matching that pattern.
# Print the list.

import glob
counts = {}

pattern = input('Enter a pattern: ').strip()
filenames = glob.glob(pattern)

# calculations
for one_filename in filenames:
    # I want to grab the final part of the string,
    # after the last . to appear there

    # (1) break up the string wherever there are dots, getting a list
    parts = one_filename.split('.')
    # (2) grab the final element of that list
    extension = parts[-1]

    # now:
    # - if we've seen this extension before, then add 1 to its value
    if extension in counts:
        counts[extension] += 1

    # - if this is the first time, then just set key-value to be 1
    else:
        counts[extension] = 1

# report
print(counts)