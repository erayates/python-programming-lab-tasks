# Task3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

newDic = {**dic1, **dic2, **dic3}

print(newDic)


# Another way
def concat_dicts(*dicts):
    new_dict = {}
    for dictionary in dicts:
        new_dict.update(dictionary)
    return new_dict

output_dict = concat_dicts(dic1,dic2,dic3)
print(output_dict)