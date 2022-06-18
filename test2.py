import pandas
import random
list = []
data = pandas.read_csv("./data/french_words_2.csv")
print(f"DataFrame : {data}\n")
chosen_word = random.choice(data.to_dict(orient='records'))

list.append(a)
print(list)
# print(f"to_dict------->\n{data.to_dict()}\n")
# print(f"to_dict-------list>\n{data.to_dict('list')}\n")
# print(f"to_dict-------series>\n{data.to_dict('series')}\n")
# print(f"to_dict-------split>\n{data.to_dict('split')}\n")
# print(f"to_dict-------records>\n{data.to_dict(orient='records')}\n")
# print(f"to_dict-------records[0]>\n{data.to_dict(orient='records')[0]}\n")
# print(f"to_dict-------records[0]['French']>\n{data.to_dict(orient='records')[0]['French']}\n")

# print(f"loc------------boolean>\n{data.loc[[True, True, True]]}\n")
# print(f"loc------------boolea1n>\n{data.loc[[False, False, False]]}\n")
# print(f"loc------------boolean2>\n{data.loc[[False, False, True]]}\n")
# print(f"loc------------boolean3>\n{data.loc[[False, True, False]]}\n")
# print(f"loc------------boolean4>\n{data.loc[[True]]}\n")
#
# print(f"loc------------label>\n{data.loc[0]}\n")
# print(f"loc------------label,>\n{data.loc[:,'French']}\n")
# data.loc[:,'French'] = 'partie'
# print(data)