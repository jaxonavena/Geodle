import random
import math
from executive import Executive
from database import Database
class Guesser:
    def __init__(self):
        self.exc = Executive()
        self.exc.run()
        self.colist = self.exc.get_country_info()
        self.northhemi = self.exc.get_north_hemi()
        self.southhemi = self.exc.get_south_hemi()
        self.africa = self.exc.get_africa
        self.asia = self.exc.get_asia
        self.northamerica = self.exc.get_north_america
        self.southamerica = self.exc.get_south_america
        self.europe = self.exc.get_europe
        self.oceania = self.exc.oceania
        self.countryname = self.exc.get_country_names
        self.secretcountry = random.choice(self.countryname)

    #comparisons
    def win(self, guess):
        for co in self.colist:
            if guess == self.secretcountry:
                return True

    def compare_all(self,guess):
        comparison_list = []
        comparison_list.append(compare_continent(guess))
        comparison_list.append(compare_whatever(guess))
        return comparison_list

    def compare_continent(self, guess):
        if guess.get_continent() == self.secretguess.get_continent():
            return 'green'
        elif self.bordering(guess):
            return 'yellow'
        else:
            return 'grey'

    def bordering(self,guess):
        if guess.get_continent() == "NA":
            if self.secretcountry.get_continent() == "SA":
                return True
        if guess.get_continent == "SA":
            if self.secretcountry.get_continent() == "NA":
                return True
        if guess.get_continent == "OC":
            if self.secretcountry.get_continent() == "AS":
                return True
        if guess.get_continent == "AS":
            if self.secretcountry.get_continent() == "OC":
                return True
            elif self.secretcountry.get_continent() == "EU":
                return True
            elif self.secretcountry.get_continent() == "AF":
                return True
        if guess.get_continent() == "EU":
            if self.secretcountry.get_continent() == "AF":
                return True
            elif self.secretcountry.get_continent() == "AS":
                return True
        if guess.get_continent() == "AF":
            if self.secretcountry.get_continent() == "EU":
                return True
            elif self.secretcountry.get_continent() == "AS":
                return True
        return False

    def compare_hemi(self,guess):
        if guess.get_hemisphere() == self.secretcountry.get_hemisphere():
            return "green"
        else:
            return
    def compare_area(self,guess):
        if guess.get_area() == self.secretcountry.get_area():
            return "green"
        elif abs(guess.get_area() - self.secretcountry.get_area()) <= 250000:
            return "yellow"
        else:
            return "grey"

    def compare_pop(self, guess):
        if guess.get_pop() == self.secretcountry.get_pop():
            return "green"
        elif abs(guess.get_pop() - secretcountry.get_pop()) <= 10000000:
            return "yellow"
        else:
            return "grey"
