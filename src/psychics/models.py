import random
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from pynames.generators.russian import PaganNamesGenerator
import random


class Psychics:
    def __init__(self):
        self.name = PaganNamesGenerator().get_name_simple()
        self.trust_level = 0
        self.psy_num = 0
        self.all_number = []

    def make_choice(self):
        """Делаем попытку отгадать число, загаданное пользователем"""
        self.psy_num = random.randint(10, 99)
        self.all_number.append(self.psy_num)

    def check_answer(self, user_answer):
        """Проверка правильности данного ответа"""
        if user_answer == self.psy_num:
            self.trust_level += 1
        else:
            self.trust_level -= 1


class PsyController:
    """Class represents psychics controller
    """

    def __init__(self):
        """ Initializer
        """
        self.psychics = [Psychics() for i in range(2, 6)]

    def get_choices(self):
        """ Get all psychics guesses
        """
        return [{'psy_name': psychic.name,
                 'psy_num': psychic.make_choice()}
                for psychic in self.psychics]

    def check_all(self, number):
        """ Check all psychics guesses
        """
        for psychics in self.psychics:
            psychics.make_choice()
            psychics.check_answer(number)
        return self.get_all()

    def get_all(self):
        """ Returns list of dict of all psychics
        """
        return [{'psy_name': psychic.name,
                 'psy_all_number': psychic.all_number,
                 'psy_trust_level': psychic.trust_level}
                for psychic in self.psychics]
