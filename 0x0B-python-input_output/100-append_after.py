#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, mode='r', encoding='utf-8') as f:
        text = f.readlines()
        new_t = []

        for line in text:
            new_t.append(line)

            if search_string in line:
                new_t.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as nf:
        for line in new_t:
            nf.write(line)
