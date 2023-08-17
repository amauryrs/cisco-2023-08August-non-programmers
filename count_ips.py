# setup
counts = {}  # empty dict, soon to be filled with IP:count pairs

# calculations
for one_line in open('mini-access-log.txt'):
    ip_address = one_line.split()[0]

    if ip_address in counts:     # if we've seen this IP address before,
        counts[ip_address] += 1  # add 1 to the existing count
    else:
        counts[ip_address] = 1   # first time with this IP? Add the new key-value pair

# report
for key, value in counts.items():    # go through each key-value pair
    print(f'{key}:\t{value}')         # print the key and the value
