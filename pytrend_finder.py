import json
import matplotlib.pyplot as plt

def merge_dicts(*dicts):
    merged_dict = {}
    for d in dicts:
        for key, value in d.items():
            merged_dict[key] = merged_dict.get(key, 0) + value
    return merged_dict

file_names = ["weekfile\\frequencies\\2024-02-11.json", "weekfile\\frequencies\\2024-02-12.json","weekfile\\frequencies\\2024-02-13.json","weekfile\\frequencies\\2024-02-15.json","weekfile\\frequencies\\2024-02-17.json"] #, "file3.json", "file4.json", "file5.json", "file6.json", "file7.json"]
all_dicts = []

for file_name in file_names:
    with open(file_name, 'r') as file:
        file_dict = json.load(file)
        all_dicts.append(file_dict)

big_dict = merge_dicts(*all_dicts)

keylist = dict(sorted(big_dict.items(), key=lambda item: item[1], reverse=True))

#print(keylist)

tenpairs = {key: keylist[key] for key in list(keylist.keys())[:10]}

 
xpoints = tenpairs.keys()
ypoints = tenpairs.values()

plt.pie(ypoints, labels = (xpoints),autopct='%1.1f%%', startangle=90)
plt.title("Trending Topics of the week")

plt.show()

