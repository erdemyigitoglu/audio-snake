class game():
	def	__init__(self):
		self.height = int(input("how high should game board be?\n"))
		self.width = int(input("how vide should game board be?\n"))
		self.board_matrix = [["*"]*self.width]*self.height
	def render(self):
		for i in self.board_matrix:
			for j in i:
				if (i == other.position[0]) and (j == other.position[1]:
					print("v", end =" ") 
				else:
					print(j, end = " ")
			print() 
class snake():
	def __init__(self):
		self.position = (game.with//2, game.height//2)
		self.direction = (1, 0)
	def step(self):
	self.direction = (int(input("x axis")), int(input("y axis"))
		self.position += self.direction)
snake = game()
snake.render(), )
