import json

with open('sample _json.txt', 'r') as file:
    file_content = file.read()

dictionary = json.loads(file_content)

dicty = {}
count = 0

for elem in dictionary:
    elem = dictionary[count]
    region = elem["boundingRegions"]
    poly = region[0]
    num = poly["polygon"]
    dicty[count] = num[0]
    count += 1

sorted_dict = dict(sorted(dicty.items(), key=lambda item: item[1]))
keys = list(sorted_dict.keys())

with open("final.json", 'w', encoding='utf-8') as outfile:
    outfile.write("[\n")
    for index in range(len(keys)):
        value = dictionary[keys[index]]
        value["content"] = value["content"].replace('\u00b7', '·')
        str_data = json.dumps(value, indent=2, ensure_ascii=False)
        outfile.write(f"  {str_data}")
        if index < len(keys) - 1:
            outfile.write(",\n")
        else:
            outfile.write("\n")
    outfile.write("]\n")
