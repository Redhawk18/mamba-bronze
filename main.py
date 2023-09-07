import json 

from num2words import num2words

name = "Icon"
file_input = open("bootstrap-icons.json", "r")
file_output = open("output.rs", "w")
raw_json = json.loads(file_input.read())

# lint keys
linted_json = {}
for key, value in raw_json.items():
    # replace any numbers first
    for c in key:
        if c.isdigit():
            # add - to match split pattern
            key = key.replace(c, num2words(c) + "-")

    # capitalize second
    words = key.split("-")
    for i, word in enumerate(words):
        words[i] = word.capitalize()

    key = "".join(map(str, words))
    
    linted_json[key] = value

# sort keys
data = dict(sorted(linted_json.items()))

# pre-struct
file_output.write("// This File was generated by Mamba Bronze\n")
file_output.write("// https://github.com/Redhawk18/mamba-bronze\n\n")
file_output.write("#[derive(Copy, Clone, Debug)]\n")
file_output.write(f'pub enum {name} ' + "{\n")

for key, value in data.items():
    file_output.write(f'\t{key},\n')

file_output.write("}\n")



file_input.close()
file_output.close()