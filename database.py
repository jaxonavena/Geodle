class Database:
    def __init__(self, country, pop, area, hemisphere, continent):
        self.country = country
        self.pop = pop
        self.area = area
        self.hemisphere = hemisphere
        self.continent = continent

    def get_name(self):
        return self.country

    def get_pop(self):
        return self.pop

    def get_area(self):
        return self.area

    def get_hemisphere(self):
        return self.hemisphere

    def get_continent(self):
        return self.continent

