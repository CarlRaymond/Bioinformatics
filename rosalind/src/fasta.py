'''
Created on Dec 11, 2012

@author: Carl Raymond
'''
def read(data):
    contents = [];
    line = data.readline();
    name = line[1:].strip();
    for line in data:
        if (line[0] == '>'):
            yield name, "".join(contents);
            name = line[1:].strip();
            contents = [];
        else:
            contents.append(line.strip());
    yield name, "".join(contents);
