import pygame
# batman = 122, ironman = 182
pygame.init()

display_width, display_height = 1000, 600
iron_width, bat_width = 187, 153
steps = 0
# load background
bg = pygame.image.load('street2.jpg')
bg = pygame.transform.scale(bg, (display_width, display_height))
# environment
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Ironbatman')
clock = pygame.time.Clock()
# load ironman images
iron_left = pygame.image.load('ironman-still-small.png')
iron_right = pygame.image.load('ironman-still-mirrored.png')

iron_moving = pygame.image.load('ironman-moving-small.png')
iron_moving_flipped = pygame.transform.flip(iron_moving, True, False) 

iron_attack = pygame.image.load('ironman-attack-small.png')
iron_attack_flipped = pygame.image.load('ironman-attack-mirrored.png')
iron_defence = pygame.image.load('ironman-defence-small.png')
iron_defence_flipped = pygame.transform.flip(iron_defence, True, False)

iron_jump = pygame.image.load('ironman-jump-sharp.png')
iron_jump_flipped = pygame.transform.flip(iron_jump, True, False)
# load batman images
bat_left = pygame.image.load('batman-lean-small.png')
bat_right = pygame.transform.flip(bat_left, True, False)

bat_attack = pygame.image.load('batman-lean-attack.png')
bat_attack_flipped = pygame.transform.flip(bat_attack, True, False)
bat_defence = pygame.image.load('batman-lean-defence.png')
bat_defence_flipped = pygame.transform.flip(bat_defence, True , False)
#bat_left = pygame.transform.scale(bat_left, (118, 306))

# ironman function
def drawIron(x, y, move, side):
	if move == 'stand':
		if side == 'left':	gameDisplay.blit(iron_left, (x, y))
		elif side == 'right':	gameDisplay.blit(iron_right, (x, y))	

##	elif move == 'walk' and y == 280:
##		if side == 'left':
##			if x % 4 == 0:
#				gameDisplay.blit(iron_left, (x, y))
#			elif x % 4 != 0:
#				gameDisplay.blit(iron_moving, (x, y))
#
#		elif side == 'right':
#			if x % 4 == 0:
#				gameDisplay.blit(iron_right, (x, y))
#			elif x % 4 != 0:
#				gameDisplay.blit(iron_moving_flipped, (x, y))	

	elif move == 'walk': #and y != 280:
		if side == 'left': gameDisplay.blit(iron_left, (x, y))	
		elif side == 'right': gameDisplay.blit(iron_right, (x, y))		

	elif move == 'jump':
		if side == 'left':	gameDisplay.blit(iron_jump, (x, y))
		elif side == 'right':	gameDisplay.blit(iron_jump_flipped, (x, y)) 

	elif move == 'attack':
		if side == 'left': gameDisplay.blit(iron_attack, (x, y))
		elif side == 'right': gameDisplay.blit(iron_attack_flipped, (x, y))	

	elif move == 'defend':
		if side == 'left': gameDisplay.blit(iron_defence, (x, y))
		elif side == 'right': gameDisplay.blit(iron_defence_flipped, (x, y))	
# batman function
def drawBat(x, y, move, side):
	if move == 'stand':
		if side == 'left': gameDisplay.blit(bat_left, (x, y))
		elif side == 'right': gameDisplay.blit(bat_right, (x, y))

	elif move == 'attack':
		if side == 'left': gameDisplay.blit(bat_attack, (x, y))
		elif side == 'right': gameDisplay.blit(bat_attack_flipped, (x, y))

	elif move == 'defend':
		if side == 'left': gameDisplay.blit(bat_defence, (x, y))
		elif side == 'right': gameDisplay.blit(bat_defence_flipped, (x, y))	

score = 0
iron_x, iron_y = 100, 280 # 280 (50: difference), (270: second difference)
bat_x, bat_y = 300, 270 
x_change, y_change = 0, 0
crashed = False
iron_move, iron_side = 'stand', 'left'
bat_move, bat_side = 'stand', 'right'
# mainloop
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -5
				iron_move, iron_side = 'walk', 'right'
			if event.key == pygame.K_RIGHT:
				x_change = 5
				iron_move, iron_side = 'walk', 'left'
			if event.key == pygame.K_UP:
				y_change, iron_move = -5, 'jump' 				
			if event.key == pygame.K_a:
				iron_move = 'attack'
			if event.key == pygame.K_d:
				iron_move = 'defend'		

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change, iron_move = 0, 'stand'
			if event.key == pygame.K_UP:
				y_change, iron_move =  5, 'stand'
			if event.key == pygame.K_a:
				iron_move = 'stand'
			if event.key == pygame.K_d:
				iron_move = 'stand'		
		
	iron_x += x_change
	iron_y += y_change

	if iron_x > 1000: iron_x = 1000
	elif iron_x < 0: iron_x = 0
	
	if iron_y > 280: iron_y = 280 	
	#elif y < 0: y = 0	

	gameDisplay.blit(bg, (0,0))

	drawBat(bat_x, bat_y, bat_move, bat_side)
	drawIron(iron_x, iron_y, iron_move, iron_side)

	if (iron_move == 'attack' and bat_move != 'defend'):
		if (bat_x - iron_x < 160 and bat_x - iron_x > 95) and (bat_y - iron_y < 50):
			print('yay')
			

	# 70, 10	
	#print(iron_y, bat_y)	

	pygame.display.update()
	clock.tick(60)		

pygame.quit()
quit()