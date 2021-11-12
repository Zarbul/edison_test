from pynames.generators.russian import PaganNamesGenerator
import random


class Psychics:
    def __init__(self):
        self.name = PaganNamesGenerator().get_name_simple()
        self.trust_level = {}
        self.psy_num = {}
        self.all_number = {}

    def make_choice(self, username):
        self.psy_num[username] = random.randint(10, 99)

    def get_rating(self, username):
        return self.trust_level.setdefault(username, 0)

    def change_rating(self, username, increase_number):
        self.trust_level[username] = self.get_rating(username) + increase_number

    def check_answer(self, user_answer, username):
        all_number = self.all_number.setdefault(username, [])
        all_number.append({'psy_num': self.psy_num[username]})
        if user_answer == self.psy_num[username]:
            self.change_rating(username, 1)
        else:
            self.change_rating(username, -1)


class PsyController:
    def __init__(self):
        self.psychics = [Psychics() for i in range(2, 6)]

    def get_choices(self, username):
        return [{'psy_name': psychic.name,
                 'psy_num': psychic.make_choice(username)}
                for psychic in self.psychics]

    def check_all(self, number, username):
        for psychics in self.psychics:
            psychics.make_choice(username)
            psychics.check_answer(number, username)
        return self.get_all(username)

    def get_all(self, username):
        return [{'psy_name': psychic.name,
                 'psy_all_number': psychic.all_number.get(username),
                 'psy_trust_level': psychic.get_rating(username)}
                for psychic in self.psychics]
