from game import Game
from database import Database

class Executive:
  def __init__(self,file_name):
    self.filename = file_name
    self.country_info_list = []


  def run(self):
    """ Reads file and creates list of class instances for each country """
    with open(self.filename, 'r') as input_file:
      for line in input_file:
        categories = line.strip().split('\t')
        country_name = categories[0].upper()
        pop = categories[1]
        area = categories[2]
        hemisphere = categories[3]
        continent = categories[4]
        country_instance = Database(country_name, pop, area, hemisphere, continent)
        self.country_info_list.append(country_instance)

    self.game = Game(self.country_info_list)
    self.game.run()




