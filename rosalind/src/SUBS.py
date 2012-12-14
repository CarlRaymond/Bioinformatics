import re;

with open("rosalind_subs.txt") as data:
    seq = data.readline().strip();
    pattern = data.readline().strip();

pos = 0;
match = re.search(pattern, seq);
while match:
    pos = match.start() + pos + 1;
    print pos;
    match = re.search(pattern, seq[pos:]);


raw_input()
