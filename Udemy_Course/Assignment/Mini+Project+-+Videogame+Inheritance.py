class Character:
    
		def __init__(self, x, y, img_file, speed, life_counter):
				self.x = x
				self.y = y
				self.img_file = img_file
				self.speed = speed
				self.life_counter = life_counter

class Enemy(Character):
    
		def __init__(self, x, y, img_file, speed, life_counter):
				Character.__init__(self, x, y, img_file, speed, life_counter)
				self.message = "I'm here to protect my master"

class Player(Character):
    
		def __init__(self, x, y, img_file, speed, life_counter):
				Character.__init__(self,x, y, img_file, speed, life_counter)
				self.speed = 56

class DifficultEnemy(Enemy):
    
		def __init__(self, x, y, img_file, speed, life_counter):
			Enemy.__init__(self, x, y, img_file, speed, life_counter)

class EasyEnemy(Enemy):
		def __init__(self, x, y, img_file, speed, life_counter):
			Enemy.__init__(self, x, y, img_file, speed, life_counter)
