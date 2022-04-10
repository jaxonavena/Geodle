import random
import math
import string

class Comparison:
  def __init__(self, country_info_list):
    self.country_info_list = country_info_list
    self.secretcountry = random.choice(country_info_list)
    print(self.secretcountry.get_name()) #Secret country name

  #comparisons
  def win(self, guess):
    if guess == self.secretcountry.get_name():
      return True

  def compare_all(self,guess):
    invalid = True
    comparison_list = []
    for country in self.country_info_list:
      if country.get_hemisphere() == "B":
        country.hemisphere = "BOTH"
      if guess == country.get_name():
        invalid = False
        guess = country #turn str to country class
        comparison_list.append(self.compare_letter(guess))
        comparison_list.append(self.compare_hemi(guess))
        comparison_list.append(self.compare_continent(guess))
        comparison_list.append(self.compare_area(guess))
        comparison_list.append(self.compare_pop(guess))
        comparison_list.append(self.pop_range(guess))
        comparison_list.append(self.area_range(guess))
        # comparison_list.append(self.letter_range(guess))
        return comparison_list
    if invalid:
      return "invalid"

  def bordering_continent(self,guess):
      """ Creates relationships for bordering continent """
      if guess.get_continent() == "NORTH-AMERICA":
          if self.secretcountry.get_continent() == "SOUTH-AMERICA":
              return True
      elif guess.get_continent() == "SOUTH-AMERICA":
          if self.secretcountry.get_continent() == "NORTH-AMERICA":
              return True
      elif guess.get_continent() == "OCEANIA":
          if self.secretcountry.get_continent() == "ASIA":
              return True
      elif guess.get_continent() == "ASIA":
          if self.secretcountry.get_continent() == "OCEANIA":
              return True
          elif self.secretcountry.get_continent() == "EUROPE":
              return True
          elif self.secretcountry.get_continent() == "AFRICA":
              return True
      elif guess.get_continent() == "EUROPE":
          if self.secretcountry.get_continent() == "AFRICA":
              return True
          elif self.secretcountry.get_continent() == "ASIA":
              return True
      elif guess.get_continent() == "AFRICA":
          if self.secretcountry.get_continent() == "EUROPE":
              return True
          elif self.secretcountry.get_continent() == "ASIA":
              return True
      return False

  def compare_letter(self, guess):
      """ Returns feedback telling the user if the first letter of the guess is near the first letter of the answer """
      guess_letter = guess.get_name()[0]
      secret_letter = self.secretcountry.get_name()[0]     ## Saves first letter

      alphabet = list(string.ascii_uppercase)   #creates a list of every letter
      letter_index = 0
      if guess_letter == secret_letter:
          return 'green'                   # if the guess and correct country start with the same letter
      elif guess_letter in alphabet:
          for letter in alphabet:
              if guess_letter == letter:
                  letter_index = alphabet.index(letter)        # stores index of the guess letter

          if letter_index < 5:
              for letter in alphabet[0:letter_index + 5:1]:
                  if secret_letter == letter:
                      return 'yellow'               #if guess and correct letter are one of first 5 letters in alphabet, return close
              return 'grey'
          elif letter_index > 20:
              for letter in alphabet[(letter_index - 5):25:1]:
                  if secret_letter == letter:       #if guess and correct letter are one of last 5 letters in alphabet, return close
                      return 'yellow'
              return 'grey'
          elif 5 <= letter_index <= 20:
              for letter in alphabet[(letter_index - 5):(letter_index + 5):1]:
                  if secret_letter == letter:     #if correct letter is within 5 indices of the guess letter
                      return 'yellow'
              return 'grey'



  def compare_continent(self, guess):
      """ Returns feedback lettin user know if country guess is in same, bordering, or wrong continent """
      if guess.get_continent() == self.secretcountry.get_continent():
          return 'green'
      elif self.bordering_continent(guess):
          return 'yellow'    ## if country is in a bordering continent, return yellow, meaning 'close'
      else:
          return 'grey'

  def compare_hemi(self,guess):
      """ Returns feedback telling user if guess in in same hemisphere or not """
      if guess.get_hemisphere() == self.secretcountry.get_hemisphere() or guess.get_hemisphere() == "BOTH":
          return "green"
      elif self.secretcountry.get_hemisphere() == "BOTH":
        return "yellow"
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

  def pop_range(self, guess):
      if guess.get_pop() < self.secretcountry.get_pop():
          return 'higher'
      elif guess.get_pop() > self.secretcountry.get_pop():
          return 'lower'

  def area_range(self, guess):
      if guess.get_area() < self.secretcountry.get_area():
          return 'higher'
      elif guess.get_area() > self.secretcountry.get_area():
          return 'lower'

  # def letter_range(self, guess):
  #     if guess.get_name()[0] > self.secretcountry.get_name()[0]:
  #         return 'higher'
  #     elif guess.get_name()[0] < self.secretcountry.get_name()[0]:
  #         return 'lower'
  #     else:
  #         return 'equal'