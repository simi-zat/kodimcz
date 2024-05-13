import json

output_dict = {}

with open("words.txt", 'r') as f:
    for w in f.readlines():

        if w[0] not in output_dict:
            output_dict[w[0]]=[]

        output_dict[w[0]].append(w.strip())

sorted_dict = dict(sorted(output_dict.items()))
print(sorted_dict)

with open("output.json", 'w') as f:
    json.dump(sorted_dict, f)




