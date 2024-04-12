class Bacterium:
    def __init__(self, x, y, shape, is_resistant, is_gram_positive):
        self.x = x
        self.y = y
        self.shape = shape
        self.is_resistant = is_resistant
        self.is_gram_positive = is_gram_positive




# Create 3 instances
bacterium1 = Bacterium(50, 60, "coccus", True, True)
bacterium2 = Bacterium(50, 260, "bacillus", False, False)
bacterium3 = Bacterium(150, 200, "tetrad", True, True)
