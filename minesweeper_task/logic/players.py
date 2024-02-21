import json
from operator import itemgetter


class Players:
    def __init__(self, name, time):
        self.__name = name
        self.__time = time

    @property
    def name(self):
        return self.__name

    @property
    def time(self):
        return self.__time

    def add_player(self):
        with open('data/high_scores.json', 'r') as file:
            high_scores = json.load(file)
            high_scores.append([self.__name, round(self.__time, 1)])
        with open('data/high_scores.json', 'w') as file:
            json.dump(high_scores, file)

    @staticmethod
    def load_scores():
        with open('data/high_scores.json', 'r') as file:
            return sorted(json.load(file), key=itemgetter(1))[:10]
