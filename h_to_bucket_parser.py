import json
import yaml


json_data = open('hw.json', 'r')
dictionary_of_ppl = json.load(json_data)

ppl_ages_dic = {}
buckets_list = []

final_dic = {"0-11": [], "11-25": [], "25-40": [], "40-100": []}

for key, value in dictionary_of_ppl.items():
    if key == 'buckets':
        buckets_list.append(value)
        clear_list = buckets_list[0]
        clear_list.sort()

    if key == 'ppl_ages':
        ppl_ages_dic.update(dictionary_of_ppl['ppl_ages'])
        sorted(ppl_ages_dic)
        for name, age in ppl_ages_dic.items():
            if age < 11:
                final_dic["0-11"].append({"name": name, "age": age})
            elif 25 > age >= 11:
                final_dic["11-25"].append({"name": name, "age": age})
            elif 25 <= age < 40:
                final_dic["25-40"].append({"name": name, "age": age})
            elif 40 < age or age < 100:
                final_dic["40-100"].append({"name": name, "age": age})
            else:
                break

with open('ages.yaml', 'w') as outfile:
    yaml.dump(final_dic, outfile, default_flow_style=False)
