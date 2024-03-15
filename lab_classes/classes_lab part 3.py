class Bird:
    def __init__(self, species, can_fly):
        self.species = species
        self.can_fly = can_fly


class Owl(Bird):
    def __init__(self, species, can_fly, nocturnal):
        Bird.__init__(self, species, can_fly)
        self.nocturnal = nocturnal


class Dodo(Bird):
    def __init__(self, species, can_fly, extinct_year):
        Bird.__init__(self, species, can_fly)
        self.extinct_year = extinct_year

owl = Owl("Owl", True, True)
dodo = Dodo("Dodo", False, 1662)



