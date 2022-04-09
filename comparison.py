import random
import math

class Comparison:
  def __init__(self, country_info_list):
    self.country_info_list = country_info_list
    self.secretcountry = random.choice(country_info_list)

  #comparisons
  def win(self, guess):
    if guess == self.secretcountry.get_name():
      return True

  def compare_all(self,guess):
    invalid = True
    for country in self.country_info_list:
      if guess == country.get_name():
        invalid = False
        guess = country #turn str to country class
        comparison_list = ["grey"]
        comparison_list.append(self.compare_hemi(guess))
        comparison_list.append(self.compare_continent(guess))
        comparison_list.append(self.compare_area(guess))
        comparison_list.append(self.compare_pop(guess))
        return comparison_list
    if invalid:
      return "invalid"



  def compare_continent(self, guess):
      """ Returns feedback lettin user know if country guess is in same, bordering, or wrong continent """
      if guess.get_continent() == self.secretcountry.get_continent():
          return 'green'
      elif self.bordering_continent(guess):
          return 'yellow'    ## if country is in a bordering continent, return yellow, meaning 'close'
      else:
          return 'grey'

  def bordering_continent(self,guess):
      """ Creates relationships for bordering continent """
      if guess.get_continent() == "NA":
          if self.secretcountry.get_continent() == "SA":
              return True
      elif guess.get_continent() == "SA":
          if self.secretcountry.get_continent() == "NA":
              return True
      elif guess.get_continent() == "OC":
          if self.secretcountry.get_continent() == "AS":
              return True
      elif guess.get_continent() == "AS":
          if self.secretcountry.get_continent() == "OC":
              return True
          elif self.secretcountry.get_continent() == "EU":
              return True
          elif self.secretcountry.get_continent() == "AF":
              return True
      elif guess.get_continent() == "EU":
          if self.secretcountry.get_continent() == "AF":
              return True
          elif self.secretcountry.get_continent() == "AS":
              return True
      elif guess.get_continent() == "AF":
          if self.secretcountry.get_continent() == "EU":
              return True
          elif self.secretcountry.get_continent() == "AS":
              return True
      return False

  def compare_hemi(self,guess):
      """ Returns feedback telling user if guess in in same hemisphere or not """
      if guess.get_hemisphere() == self.secretcountry.get_hemisphere() or guess.get_hemisphere() == "B":
          return "green"
      else:
          return "grey"

  def compare_area(self,guess):
      """ Returns feedback telling user info about area of guess vs. answer """
      if guess.get_area() == self.secretcountry.get_area():
          return "green"
      elif abs(guess.get_area() - self.secretcountry.get_area()) <= 250000:
          return "yellow"      ## if guess country area is within 250,000 sq. km of answer area, tell user they are "close"
      else:
          return "grey"

  def compare_pop(self, guess):
      """ Returns feedback telling info about population of guess vs. answer """
      if guess.get_pop() == self.secretcountry.get_pop():
          return "green"
      elif abs(guess.get_pop() - self.secretcountry.get_pop()) <= 10000000:
          return "yellow"  ## if guess population is within 10 mil. of answer, tell user they are "close"
      else:
          return "grey"
