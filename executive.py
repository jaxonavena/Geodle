from database import Database

class Executive:
    def __init__(self, file_name):
        self.country_info = []
        self.filename = file_name
        self.north_hemi = []
        self.south_hemi = []
        self.north_america = []
        self.south_america = []
        self.africa = []
        self.asia = []
        self.europe = []
        self.oceania = []
        self.country_names = []

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
                country_instance = Guesser(country_name, pop, area, hemisphere, continent)
                self.country_info.append(country_instance)


    def country_names(self):
        """ Creates a list of country names to choose from """
        for i in country_info:
            self.country_names.append(i.get_name())
        return country_names

    def get_country_info(self):
        return self.country_info

    def hemisphere(self):

        for i in self.country_info:
            if i.get_hemisphere() == 'N':
                self.north_hemi.append(i)
            elif i.get_hemisphere() == 'S':
                self.south_hemi.append(i)
            else:
                self.north_hemi.append(i)
                self.south_hemi.append(i)


    def continent(self):
        """ Creates """
        for i in self.country_info:
            if i.get_continent() == 'NA':
                self.north_america.append(i)
            elif i.get_continent() == 'SA':
                self.south_america.append(i)
            elif i.get_continent() == 'AF':
                self.africa.append(i)
            elif i.get_continent() == 'AS':
                self.asia.append(i)
            elif i.get_continent() == 'EU':
                self.europe.append(i)
            elif i.get_continent() == 'OC':
                self.oceania.append(i)

    def get_north_hemi(self):
        return self.north_hemi

    def get_south_hemi(self):
        return self.south_hemi

    def get_north_america(self):
        return self.north_america

    def get_south_america(self):
        return self.south_america

    def get_africa(self):
        return self.get_africa

    def get_asia(self):
        return self.asia

    def get_europe(self):
        return self.europe

    def get_oceania(self):
        return self.oceania