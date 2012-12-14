def read(file):
    contents = [];
    line = file.readline();
    name = line[1:].strip();
    for line in file:
        if (line[0] == '>'):
            yield (name, "".join(contents));
            name = line[1:].strip();
            contents = [];
        else:
            contents.append(line.strip());
    yield (name, "".join(contents));

