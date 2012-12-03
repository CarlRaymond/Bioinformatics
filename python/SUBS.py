import re;

with open("rosalind_subs.txt") as input:
    data = input.readline().strip();
    pattern = input.readline().strip();

pos = 0;
match = re.search(pattern, data);
while match:
    pos = match.start() + pos + 1;
    print pos;
    match = re.search(pattern, data[pos:]);


raw_input()
