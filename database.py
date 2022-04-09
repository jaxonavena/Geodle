class Database:
    def __init__(self, name, pop, area, hemisphere, continent):
        self.name = name
        self.pop = int(pop)
        self.area = int(area)
        self.hemisphere = hemisphere
        self.continent = continent

    def get_name(self):
        return self.name

    def get_pop(self):
        return self.pop

    def get_area(self):
        return self.area

    def get_hemisphere(self):
        return self.hemisphere

    def get_continent(self):
        return self.continent

