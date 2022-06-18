import pandas
from random import randint

data = pandas.read_csv("./data/french_words.csv")

# todo 1. 카드 보여주기
# 랜덤으로 로우 하나 선택
rand_n = randint(0,101)

rand_all = data.iloc[rand_n]
rand_french = data["French"][rand_n]
rand_english = data["English"][rand_n]


# 프렌치 보여주고 3초 후에 영어 보여주면 됨

