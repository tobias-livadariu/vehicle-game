#Tobias Livadariu
#ICS3UI-23
#Instructor: Ms. Mohammed
#2023-06-14
#This is my ICS3U culminating assignment. it is a game where the user plays as a blue vehicle and collects experience points to power up. When the user is eventually destroyed by the enemies, their final experience points total is displayed as their score for that game.

# Importing the pygame, sys, random and math modules.
import pygame, sys, random, math
# Importing the sin, cos, tan, asin, atan, acos, sqrt, and pow functions from the math module. Note that I didn't use all these functions, but I imported them all anyway, just in case I need one to solve a problem that may arise in the future.
from math import sin, cos, tan, asin, atan, acos, sqrt, pow

# Initializing the pygame module.
pygame.init()

# Defining the functions that will be used to draw the title screen for the game and also the game over screens when the user's health reaches zero
def draw_screens(screenDrawing):
  while True:
    # Drawing the necessary information for the title screen if that is what is currently being displayed to the user
    if screenDrawing == "titleScreen":
      screen.fill(MUTE_YELLOW)

      # Setting the values of the text to be blit'ed
      titleText1 = font.render("Tobias Livadariu's", True, BLACK)
      titleText2 = font.render("Vehicle Game!", True, BLACK)
      titleText3 = font.render("Welcome!", True, BLACK)
      playText = font.render("CLICK HERE TO PLAY GAME", True, BUTTON_TEXT_COLOUR)
      instructionText = font.render("INSTRUCTIONS", True, BUTTON_TEXT_COLOUR)

      # Bliting the text to the center of the screen
      # Note that I got the text always exactly centered by making its starting x-position equal to half of the text's width to the left of the center of the screen
      screen.blit(titleText1, [275 - titleText1.get_rect().width/2, 50])
      screen.blit(titleText2, [275 - titleText2.get_rect().width/2, 80])
      screen.blit(titleText3, [275 - titleText3.get_rect().width/2, 110])
      screen.blit(playText, [275 - playText.get_rect().width/2, 248])
      screen.blit(instructionText, [275 - instructionText.get_rect().width/2, 328])

      # Setting coordinates of the button to play again
      button1Width = 315
      button1Height = 30
      button1X = 275 - button1Width/2
      button1Y = 245
      pygame.draw.rect(screen, BLACK, [button1X, button1Y, button1Width, button1Height], 2)

      # Setting coordinates of the button to open the instructions menu
      button2Width = 185
      button2Height = 30
      button2X = 275 - button2Width/2
      button2Y = 325
      pygame.draw.rect(screen, BLACK, [button2X, button2Y, button2Width, button2Height], 2)

      # Checking if the user presses quit or any other button on the screen
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          mouseX, mouseY = pygame.mouse.get_pos()
          if (mouseX >= button1X and mouseX <= button1X + button1Width) and (mouseY >= button1Y and mouseY <= button1Y + button1Height):
            return "gameScreen"
          elif (mouseX >= button2X and mouseX <= button2X + button2Width) and (mouseY >= button2Y and mouseY <= button2Y + button2Height):
            return "instructionsScreen"

      # Flipping the changes made to the display to the screen
      pygame.display.flip()
      # Setting the maximum framerate of the game to 30 frames per second.
      clock.tick(30)
    elif screenDrawing == "gameOverScreen":
      screen.fill(MUTE_YELLOW)

      # Defining the text to be blit'ed to the game over screen
      gameOverText1 = font.render("Your Health Reached Zero!", True, BLACK)
      gameOverText2 = font.render("Game Over!", True, BLACK)
      gameOverText3 = font.render("Your final score was:", True, BLACK)
      gameOverText4 = font.render(f"{old_exp_collect} Points", True, BLACK)
      playAgainText = font.render("CLICK HERE TO PLAY AGAIN", True, BUTTON_TEXT_COLOUR)
      instructionText = font.render("INSTRUCTIONS", True, BUTTON_TEXT_COLOUR)

      # Bliting the text to the center of the screen
      # Note that I got the text always exactly centered by making its starting x-position equal to half of the text's width to the left of the center of the screen
      screen.blit(gameOverText1, [275 - gameOverText1.get_rect().width/2, 50])
      screen.blit(gameOverText2, [275 - gameOverText2.get_rect().width/2, 80])
      screen.blit(gameOverText3, [275 - gameOverText3.get_rect().width/2, 110])
      screen.blit(gameOverText4, [275 - gameOverText4.get_rect().width/2, 140])
      screen.blit(playAgainText, [275 - playAgainText.get_rect().width/2, 248])
      screen.blit(instructionText, [275 - instructionText.get_rect().width/2, 328])

      # Setting the values of the play again button
      button1X = 117.5
      button1Y = 245
      button1Width = 318
      button1Height = 29
      pygame.draw.rect(screen, BLACK, [button1X, button1Y, button1Width, button1Height], 2)

      # Setting the values of the instruction button
      button2X = 182.5
      button2Y = 325
      button2Width = 185
      button2Height = 30
      pygame.draw.rect(screen, BLACK, [button2X, button2Y, button2Width, button2Height], 2)

      # Checking if the user presses quit or any other button on the screen
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          mouseX, mouseY = pygame.mouse.get_pos()
          if (mouseX >= button1X and mouseX <= button1X + button1Width) and (mouseY >= button1Y and mouseY <= button1Y + button1Height):
            return "gameScreen"
          elif (mouseX >= button2X and mouseX <= button2X + button2Width) and (mouseY >= button2Y and mouseY <= button2Y + button2Height):
            return "instructionsScreen"
      # Flipping the changes made to the display to the screen
      pygame.display.flip()
      # Setting the maximum framerate of the game to 30 frames per second
      clock.tick(30)
    elif screenDrawing == "instructionsScreen":
      # Defining the text to be blit'ed to the instruction screen
      playAgainText = font.render("CLICK HERE TO START GAME", True, BUTTON_TEXT_COLOUR)
      instructionTitleText = boldFont.render("Game Instructions:", True, BLACK)
      instructionLine1 = font.render("1. The blue circle is your vehicle", True, BLACK)
      instructionLine2 = font.render("2. Press W to move up, A to move left", True, BLACK)
      instructionLine2_1 = font.render("S to move down, D to move left", True, BLACK)
      instructionLine3 = font.render("3. Press/hold left click to shoot projectiles", True, BLACK)
      instructionLine4 = font.render("4. Enemies will shoot back at you", True, BLACK)
      instructionLine5 = font.render("5. Your exp is your score; you gain score", True, BLACK)
      instructionLine5_1 = font.render("by collecting exp orbs or by distroying enemies", True, BLACK)
      instructionLine6 = font.render("6. Your vehicle becomes stronger at:", True, BLACK)
      instructionLine6_1 = font.render("250 exp", True, BLACK)
      instructionLine6_2 = font.render("500 exp", True, BLACK)
      instructionLine6_3 = font.render("750 exp", True, BLACK)
      instructionLine6_4 = font.render("1000 exp", True, BLACK)
      instructionLine7 = font.render("7. If your health reaches zero, game over", True, BLACK)
      goodLuckText = boldFont.render("Good Luck", True, BLACK)

      #set coordinates of the play again button
      button1X = 111
      button1Y = 456
      button1Width = 328
      button1Height = 31

      screen.fill(MUTE_YELLOW)

      # Bliting the text to the center of the screen
      # Note that I got the text always exactly centered by making its starting x-position equal to half of the text's width to the left of the center of the screen
      screen.blit(instructionTitleText, [275 - instructionTitleText.get_rect().width/2, 10])
      screen.blit(instructionLine1, [275 - instructionLine1.get_rect().width/2, 40])
      screen.blit(instructionLine2, [275 - instructionLine2.get_rect().width/2, 68])
      screen.blit(instructionLine2_1, [275 - instructionLine2_1.get_rect().width/2, 96])
      screen.blit(instructionLine3, [275 - instructionLine3.get_rect().width/2, 124])
      screen.blit(instructionLine4, [275 - instructionLine4.get_rect().width/2, 152])
      screen.blit(instructionLine5, [275 - instructionLine5.get_rect().width/2, 180])
      screen.blit(instructionLine5_1, [275 - instructionLine5_1.get_rect().width/2, 208])
      screen.blit(instructionLine6, [275 - instructionLine6.get_rect().width/2, 236])
      screen.blit(instructionLine6_1, [275 - instructionLine6_1.get_rect().width/2, 264])
      screen.blit(instructionLine6_2, [275 - instructionLine6_2.get_rect().width/2, 292])
      screen.blit(instructionLine6_3, [275 - instructionLine6_3.get_rect().width/2, 320])
      screen.blit(instructionLine6_4, [275 - instructionLine6_4.get_rect().width/2, 348])
      screen.blit(instructionLine7, [275 - instructionLine7.get_rect().width/2, 376])
      screen.blit(goodLuckText, [275 - goodLuckText.get_rect().width/2, 409])
      screen.blit(playAgainText, [275 - playAgainText.get_rect().width/2, 460])

      # Drawing liness across the screen to separate the different sections of the instructions
      pygame.draw.line(screen, BLACK, [0, 36], [550, 36], 3)
      pygame.draw.line(screen, BLACK, [0, 65], [550, 65], 1)
      pygame.draw.line(screen, BLACK, [0, 120], [550, 120], 1)
      pygame.draw.line(screen, BLACK, [0, 150], [550, 150], 1)
      pygame.draw.line(screen, BLACK, [0, 178], [550, 178], 1)
      pygame.draw.line(screen, BLACK, [0, 234], [550, 234], 1)
      pygame.draw.line(screen, BLACK, [0, 374], [550, 374], 1)
      pygame.draw.line(screen, BLACK, [0, 403], [550, 403], 3)

      # Drawing the border of the button
      pygame.draw.rect(screen, BLACK, [button1X, button1Y, button1Width, button1Height], 3)

      # Checking if the user presses quit or any other button on the screen
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          mouseX, mouseY = pygame.mouse.get_pos()
          if (mouseX >= button1X and mouseX <= button1X + button1Width) and (mouseY >= button1Y and mouseY <= button1Y + button1Height):
            return "gameScreen"
      # Flipping the changes made to the display to the screen
      pygame.display.flip()
      # Setting the maximum framerate of the game to 30 frames per second
      clock.tick(30)
    else:
      return "gameScreen"

# This function checks if enemies or exp have gotten too far away from the user, and it deletes them if they did
def render(valid_xy, num_enemy, num_exp, enemy_xy, exp_xy, enemies, enemy_size, enemy_current_HP, user_projectile, enemy_projectile):
  # If an enemy gets too far replace it with a new random one that is closer to the user
  for i in range(num_enemy):
    if enemy_xy[i][0] > valid_xy[0][1] or enemy_xy[i][0] < valid_xy[0][0] or enemy_xy[i][1] > valid_xy[1][1] or enemy_xy[i][1] < valid_xy[1][0]:
      enemy_xy, enemy_size, enemy_current_HP, enemies = replace_enemy(enemy_xy, enemy_size, i, enemy_current_HP, enemies)

  # If an exp orb gets too far replace it with a new random one that is closer to the user
  for i in range(num_exp):
    if exp_xy[i][0] > valid_xy[0][1] or exp_xy[i][0] < valid_xy[0][0] or exp_xy[i][1] > valid_xy[1][1] or exp_xy[i][1] < valid_xy[1][0]:
      exp_size[i] = (random.randint(2, 12))
      exp_xy[i] = ([random.randint(GENERATE_ENEMY_EXP[0][0], GENERATE_ENEMY_EXP[0][1] - exp_size[i]), random.randint(GENERATE_ENEMY_EXP[1][0], GENERATE_ENEMY_EXP[1][1] - exp_size[i])])

  # Returning the modified coordinates of the enemies and exp orbs after the orbs/enemies too far away have been removed and new enemies have been added
  return enemy_xy, exp_xy, enemy_size, enemy_current_HP, enemies

# Defining the function that checks if an exp orb is within the collection range of the user and collects the exp orb if it is
def collect_range(exp_xy, exp_size, exp_collect):
  for i in range(num_exp):
    x = USER_CENTER[0] - (exp_xy[i][0] + exp_size[i]/2)
    y = USER_CENTER[1] - (exp_xy[i][1] + exp_size[i]/2)
    hypotenuse = math.sqrt(x**2+y**2)
    # If exp in 100 radius bring exp towards user
    if hypotenuse < 100:
      exp_xy[i][0] += x/(hypotenuse*0.5)
      exp_xy[i][1] += y/(hypotenuse*0.5)
    # If exp in 25 radius create new orb
    if hypotenuse < 16:
      exp_collect += exp_size[i]
      exp_size[i] = random.randint(2, 12)
      exp_xy[i][0] = random.randint(GENERATE_ENEMY_EXP[0][0], GENERATE_ENEMY_EXP[0][1] - exp_size[i])
      exp_xy[i][1] = random.randint(GENERATE_ENEMY_EXP[1][0], GENERATE_ENEMY_EXP[1][1] - exp_size[i])

  return exp_collect

# Defining the function that is used to create new enemies when one is destroyed or out of the render range
def replace_enemy(xy, size, i, HP, enemies):
  size[i] = (random.randint(25, 75))
  xy[i] = ([random.randint(GENERATE_ENEMY_EXP[0][0], GENERATE_ENEMY_EXP[0][1]), random.randint(GENERATE_ENEMY_EXP[1][0], GENERATE_ENEMY_EXP[1][1])])
  enemies[i] = [int(xy[i][0]+(size[i]/2)), int(xy[i][1]+(size[i]/2)), 60]
  enemy_health[i] = (10 * size[i] - 150)
  HP[i] = (10 * size[i] - 150)
  return xy, size, HP, enemies

# Defining the function that will draw enemy turrets
def enemy(x_y, size, i, HP, exp_collect, enemies):
  pygame.draw.ellipse(screen, ENEMY_COLOUR, [x_y[i][0], x_y[i][1], size[i], size[i]])
  turret(enemies[i][0], enemies[i][1], size[i], ENEMY_COLOUR, USER_CENTER)
  if HP[i] <= 0:
    exp_collect += size[i]
    x_y, size, HP, enemies = replace_enemy(x_y, size, i, HP, enemies)
  return exp_collect, x_y, size, HP, enemies

# Defining the function that will draw experience orbs to the screen
def exp_orb(x_y, size, i):
  pygame.draw.ellipse(screen, EXP_COLOUR, [x_y[i][0], x_y[i][1], size[i], size[i]])

# Defining a function that can be used to find the angle in standard form of a 2D vector
def find_vector_angle(tailX, tailY, tipX, tipY):
  deltaX = tipX - tailX
  deltaY = tipY - tailY
  hypotenuse = sqrt(pow(deltaX, 2) + pow(deltaY, 2))
  # Calculating the angle of the vector on the screen in standard form
  theta = asin(deltaY/hypotenuse)
  if deltaX < 0:
    theta = PI - theta
  return theta

# Defining the function used to create a line showing the trajectory that a fired projectile will follow when the user clicks
def turret(centerX, centerY, size, colour, target):
  turret_angle = find_vector_angle(centerX, centerY, target[0], target[1])
  hypotenuse1 = 0.9 * size
  hypotenuse2 = 1.5 * size
  width =  1
  y = [centerY + hypotenuse1 * sin(turret_angle), centerY + hypotenuse2 * sin(turret_angle)]
  x = [centerX + hypotenuse1 * cos(turret_angle), centerX + hypotenuse2 * cos(turret_angle)]
  pygame.draw.line(screen, colour, [x[0], y[0]], [x[1], y[1]], width)


# Defining the function used to check if the user was hit with an enemy projectile each frame
def hit(char, proj, char_size, hp):
  for i in proj:
    x = char[0] - (i[0])
    y = char[1] - (i[1])
    h = math.sqrt(x**2+y**2)
    if h <= char_size/2:
      hp -= 30
      proj.remove(i)
  return hp


# Defining the function used to check if an enemy was hit with one of the user's projectiles each frame
def hit_enemy(char, proj, char_size, hp):
  for a in range(len(char)):
    for i in proj:
      x = char[a][0] - (i[0])
      y = char[a][1] - (i[1])
      h = math.sqrt(x**2+y**2)
      if h <= char_size[a]/2:
        hp[a] -= 30
        proj.remove(i)
  return hp, proj

# This function is used to determine if the user is pressing a movement key (w, a, s or d) and returning a movement list depending on which keys they are currently pressing. This vector is then used in future functions when actually moving the elements on the screen.
# It is important to note that this function contains the event-getting portion of the program. This was done because user movement is the most important event that must be accommodated.
def vector_finder(speed, vector):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    # Checking if the w,a,s or d keys are pressed and setting their respective vectors to the user's speed value if they are (the vector holds how much increment the coordinates of each item on screen by per frame, it is called "vector" because it holds a directional value).
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w:
        vector[1] = speed
      if event.key == pygame.K_s:
        vector[1] = -speed
      if event.key == pygame.K_a:
        vector[0] = speed
      if event.key == pygame.K_d:
        vector[0] = -speed
    # Checking if the w,a,s, or d keys are released and setting their respective vectors to zero if they are.
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_w:
          vector[1] = 0
      if event.key == pygame.K_s:
          vector[1] = 0
      if event.key == pygame.K_a:
          vector[0] = 0
      if event.key == pygame.K_d:
          vector[0] = 0
  return vector

# Defining the function that will be used to change the position of exp orbs if the user is moving
def exp_position_changer(vector):
  for i in range(num_exp):
    x_y_exp[i][0] += vector[0]
    x_y_exp[i][1] += vector[1]

# Defining the function that will be used to change the position of enemies if the user is moving
def enemy_position_changer(vector):
  for i in range(num_enemy):
    x_y_enemy[i][0] += vector[0]
    enemies[i][0] += vector[0]
    x_y_enemy[i][1] += vector[1]
    enemies[i][1] += vector[1]

# Defining the function that will be used to draw the user's projectiles when they fire
def user_projectile_drawer(vector):
  # Checking if the user presses the left mouse button and launching a projectile from their cannon if they did
  # Note that the projFired variable is returned to the main program, and it is used to regulate how fast the user can fire projectiles
  projFired = False
  if pygame.mouse.get_pressed()[0] == True:
    if fireCooldown >= user_fire_rate:
      mouseCoords = pygame.mouse.get_pos()
      firingAngle = find_vector_angle(275, 275, mouseCoords[0], mouseCoords[1])
      numProjectiles.append([275 - user_projectile_size, 275 - user_projectile_size, firingAngle])
      projFired = True

  # Deleting projectiles that have flown off screen
  for proj in numProjectiles:
    if (proj[0] < -user_projectile_size or proj[0] > 550) or (proj[1] < -user_projectile_size or proj[1] > 550):
      proj = None
    # Moving the projectiles that are still on screen depending on the user's current movement
    else:
      proj[0] += vector[0]
      proj[1] += vector[1]

      # Drawing each projectile
      pygame.draw.ellipse(screen, PROJECTILE_COLOUR, [proj[0]+user_projectile_size/2, proj[1]+user_projectile_size/2, user_projectile_size, user_projectile_size])
      # Moving each projectile a fixed amount determined by their fire angle
      # Note that each projectile's fire angle is kept in the third item in each sublist in the numProjectiles list
      proj[0] += user_projectile_speed * cos(proj[2])
      proj[1] += user_projectile_speed * sin(proj[2])

  # This section of code cleans up the projectiles that moved off-screen and were deleted from the numProjectiles list (note that a None placeholder was used when removing projectiles)
  while None in numProjectiles:
    del(numProjectiles[numProjectiles.index(None)])
  return projFired

# Defining the function that will be used to draw the enemy's projeciles when they fire
def enemy_projectile_drawer(vector, size):
  for enemy in enemies:
    enemyDistanceX = 275 - enemy[0]
    enemyDistanceY = 275 - enemy[1]
    enemyDistance = sqrt(pow(enemyDistanceX, 2) + pow(enemyDistanceY, 2))

    # If the enemy timer for firing is up and the enemy is ready to fire
    if enemy[2] > 59:
      # If the enemy is a certain distance away from the user, fire the projectile (note that this distance differs depending on the size of the enemy)
      if enemyDistance <= 760 + size[enemies.index(enemy)] / 2:
        enemyAngle = find_vector_angle(enemy[0], enemy[1], 275, 275)
        numEnemyProjectiles.append([enemy[0], enemy[1], enemyAngle])
        enemy[2] = 0
    else:
      # If the enemy didn't shoot, increment their timer that is used to determine if they are ready to fire
      enemy[2] += 1

  # Deleting enemy projectiles that have passed too far outside of the screen
  for enemyProj in numEnemyProjectiles:
    if enemyProj[0] < -enemyProjSize - 50 or enemyProj[0] > 600:
        enemyProj = None
    elif enemyProj[1] < -enemyProjSize - 50 or enemyProj[1] > 600:
      enemyProj = None

    # Moving the enemy projectiles that are within the boundaries to be drawn
    else:
      enemyProj[0] += vector[0]
      enemyProj[1] += vector[1]
      pygame.draw.ellipse(screen, ENEMY_PROJECTILE_COLOUR, [enemyProj[0]-enemyProjSize/2, enemyProj[1]-enemyProjSize/2, enemyProjSize, enemyProjSize])
      enemyProj[0] += enemyProjSpeed * cos(enemyProj[2])
      enemyProj[1] += enemyProjSpeed * sin(enemyProj[2])

    # This section of code cleans up the projectiles that moved off-screen and were deleted from the numEnemyProjectiles list (note that a None placeholder was used when removing projectiles)
    while None in numProjectiles:
      del(numProjectiles[numProjectiles.index(None)])

# Defining the function that will allow the vehicle to move. It does this by moving every element on the screen in the opposite direction to the key that the user presses (eg. moving all items down if the user presses "w"), making it appear like the vehicle is moving, while still keeping it in the center of the screen.
def movement(vector):
  enemy_position_changer(vector)
  exp_position_changer(vector)
  # Calling the user_projectile_drawer function to draw projectiles on the screen if the user is holding their left mouse button with the fire rate of their vehicle
  fired = user_projectile_drawer(vector)
  enemy_projectile_drawer(vector, enemy_size)
  return fired

# Defining the function that will draw the vehicle in the center of the screen
def vehicle(size):
    pygame.draw.ellipse(screen, VEHICLE_COLOUR, [(SIZE[0] - size) / 2, (SIZE[1] - size) / 2, size, size])
    turret(USER_CENTER[0], USER_CENTER[1], size, VEHICLE_COLOUR, pygame.mouse.get_pos())

#display the amount of health that the user has
def health_display(xy, max_HP, current_HP, size):
  pygame.draw.rect(screen, RED, [xy[0], xy[1]-15, size, 10])
  pygame.draw.rect(screen , GREEN, [xy[0], xy[1]-15, size*(current_HP/max_HP),10])

# Defining the function that will be used to upgrade the user's stats based on the amount of exp that they have collected
def stat_increaser():
  if exp_collect > 999:
    return 7, 9, 20
  if exp_collect > 749:
    return 6, 9, 30
  elif exp_collect > 499:
    return 5, 8, 40
  elif exp_collect > 249:
    return 4, 6, 50
  else:
    return 4, 6, 60

# Defining the font that will be used when blit'ing text to the screen on the title screen and the game over screen
font = pygame.font.SysFont('Times new roman', 20, False, False)
boldFont = pygame.font.SysFont('Times new roman', 20, True, False)

# Initializing constants to hold the RGB values of colors that are used in the pygame.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
MUTE_YELLOW = (242, 240, 235)
VEHICLE_COLOUR = (0, 128, 255)
ENEMY_COLOUR = (255, 128, 64)
EXP_COLOUR = (49, 209, 2)
PROJECTILE_COLOUR = (51, 153, 255)
ENEMY_PROJECTILE_COLOUR = (255, 36, 0)
BUTTON_TEXT_COLOUR = (66, 179, 100)

# Initializing the constant that holds the value of pi.
PI = math.pi

# Initializing the constant tuple that will hold the dimensions of the window that the graphics of the pygame are displayed in.
SIZE = (550, 550)
USER_CENTER = (SIZE[0]/2, SIZE[1]/2)
GENERATE_ENEMY_EXP = [(-1000, 1550), (-1000, 1550)]

# Initializing the clock variable from pygame.
clock = pygame.time.Clock()

# If elements on screen not in this range (xmin, xmax, ymin, ymax) remove the element and create a new one.
object_range = [[-1000, 1550], [-1000, 1550]]

# Initializing a variable to hold the total amount of exp that the user has collected
exp_collect = 0

# Initializing the size of the vehicle.
vehicle_size = 25

# Defining a list that holds the user projectiles currently on the screen
numProjectiles = []

# Defining a list that holds the enemy projectiles currently on the screen
numEnemyProjectiles = []

# Defining the speed of enemy projectiles
enemyProjSpeed = 6

# Defining the size of enemy projectiles
enemyProjSize = 5

# Defining the variable that dictates which screen the user is seeing
screenUserSees = "titleScreen"

# Drawing 4 - 8 enemies in a 2550 x 2550 box around the user, setting the enemies health based on their size, and find the enemies' centers
num_enemy = random.randint(4, 8)
x_y_enemy = []
enemy_size = []
enemy_health = []
enemies = []
enemy_current_HP = []
for i in range(num_enemy):
  enemy_size.append(random.randint(25, 75))
  x_y_enemy.append([random.randint(GENERATE_ENEMY_EXP[0][0], GENERATE_ENEMY_EXP[0][1]), random.randint(GENERATE_ENEMY_EXP[1][0], GENERATE_ENEMY_EXP[1][1])])
  enemies.append([int(x_y_enemy[i][0]+enemy_size[i]/2), int(x_y_enemy[i][1]+enemy_size[i]/2), 60])
  enemy_health.append(10 * enemy_size[i] - 150)
  enemy_current_HP.append(10 * enemy_size[i] - 150)


# The section of code below initializes all of the user's stats
# Initializing the user's health
user_max_HP = 300
user_current_HP = 300
# Initializing the user's speed
user_speed = 4
# Initializing the user's projectile size 
user_projectile_size = 5
# Initializing the user's projectile speed
user_projectile_speed = 6
# Initializing the user's fire rate
user_fire_rate = 60

# Defining the variable that will be used when determining the cooldown between projectile launches while the user is holding down their mouse.
fireCooldown = user_fire_rate

# Randomly drawing 60 - 120 exp orbs in a 2550 x 2550 box around the user
num_exp = random.randint(60, 120)
x_y_exp = []
exp_size = []
for i in range(num_exp):
  exp_size.append(random.randint(2, 12))
  x_y_exp.append([random.randint(GENERATE_ENEMY_EXP[0][0], GENERATE_ENEMY_EXP[0][1] - exp_size[i]), random.randint(GENERATE_ENEMY_EXP[1][0], GENERATE_ENEMY_EXP[1][1] - exp_size[i])])

# Initializing the movement vector values that will be changed when the user presses a movement key (w, a, s, or d)
movementVectors = [0, 0]

# Initializing the screen where graphics will be displayed with the dimensions stored in the SIZE constant
screen = pygame.display.set_mode(SIZE)

# Setting the screen name to "Vehicle Game - Tobias Livadariu"
pygame.display.set_caption("Vehicle Game - Tobias Livadariu")

# The main loop of the program where images are drawn.
while True:
  # Drawing the specific screen that the user should be seeing
  screenUserSees = draw_screens(screenUserSees)

  # Drawing the game screen if that is what the user should currently be looking at
  if screenUserSees == "gameScreen":
    # Setting the screen color to MUTEYELLOW.
    screen.fill(MUTE_YELLOW)

    # Calling the vector_finder function with the speed of the vehicle and a list holding the keys among "w", "a", "s", and "d" that are currently pressed
    movementVectors = vector_finder(user_speed, movementVectors)

    # Reassigning the user's stats based on the amount of exp that they have earned
    user_speed, user_projectile_speed, user_fire_rate = stat_increaser()

    # Incrementing the variable that determines if a projectile is able to be fired or not
    if fireCooldown < user_fire_rate:
      fireCooldown += 1

    # Calling the movement function
    userFired = movement(movementVectors)

    # If a projectile was fired, reset the userFireDelay variable to 0
    if userFired == True:
      fireCooldown = 0

    # Checking if the user was hit by an enemy projectile and adjusting their HP if they were
    user_current_HP = hit(USER_CENTER, numEnemyProjectiles, vehicle_size, user_current_HP)

    # If the user's HP reaches zero, this block of code will be run that sets the screen they are seeing to the game over screen
    # This block of code also resets the user's stats and score to their default values and clears out the lists that hold exp orb coordinates, enemy coordinates, and projectile coordinates
    if user_current_HP == 0:
      # Storing the user's exp earned in the current game in a variable so that it can be displayed before the exp_collect variable is reset to 0 in preparation for the next round
      old_exp_collect = exp_collect

      screenUserSees = "gameOverScreen"

      # Defining the function that holds the user's score
      exp_collect = 0

      # Defining a list that holds the user projectiles currently on the screen
      numProjectiles = []

      # Defining a list that holds the enemy projectiles currently on the screen
      numEnemyProjectiles = []

      # Drawing 4 - 8 enemies in a 2550 x 2550 box around the user set their health based on their size and find the center of the enemies
      num_enemy = random.randint(4, 8)
      x_y_enemy = []
      enemy_size = []
      enemy_health = []
      enemies = []
      enemy_current_HP = []
      for i in range(num_enemy):
        enemy_size.append(random.randint(25, 75))
        x_y_enemy.append([random.randint(GENERATE_ENEMY_EXP[0][0], GENERATE_ENEMY_EXP[0][1]), random.randint(GENERATE_ENEMY_EXP[1][0], GENERATE_ENEMY_EXP[1][1])])
        enemies.append([int(x_y_enemy[i][0]+enemy_size[i]/2), int(x_y_enemy[i][1]+enemy_size[i]/2), 60])
        enemy_health.append(10 * enemy_size[i] - 150)
        enemy_current_HP.append(10 * enemy_size[i] - 150)

      # The section of code below initializes all of the user's stats
      # Initializing the user's heath
      user_max_HP = 300
      user_current_HP = 300
      # Initializing the user's speed
      user_speed = 4
      # Initializing the user's projectile size 
      user_projectile_size = 5
      # Initializing the user's projectile speed
      user_projectile_speed = 6
      # Initializing the user's fire rate
      user_fire_rate = 60

      # Defining the variable that will be used when determining the cooldown between projectile launches while the user is holding down their mouse.
      fireCooldown = user_fire_rate

      # Randomly drawing 60 - 120 exp orbs in a 2550 x 2550 box around the user
      num_exp = random.randint(60, 120)
      x_y_exp = []
      exp_size = []
      for i in range(num_exp):
        exp_size.append(random.randint(2, 12))
        x_y_exp.append([random.randint(GENERATE_ENEMY_EXP[0][0], GENERATE_ENEMY_EXP[0][1] - exp_size[i]), random.randint(GENERATE_ENEMY_EXP[1][0], GENERATE_ENEMY_EXP[1][1] - exp_size[i])])

      # Initializing the movement vector values that will be changed when the user presses a movement key (w, a, s, or d)
      movementVectors = [0, 0]

    # Checking if an enemy was hit by one of the user's projectiles
    enemy_current_HP, numProjectiles = hit_enemy(enemies, numProjectiles, enemy_size, enemy_current_HP)

    # Drawing the main part of the user's vehicle player character to the screen
    vehicle(vehicle_size)

    # Drawing the enemies to the screen
    for enemy_num in range(len(x_y_enemy)):
        exp_collect, x_y_enemy, enemy_size, enemy_current_HP, enemies = enemy(x_y_enemy, enemy_size, enemy_num, enemy_current_HP, exp_collect, enemies)

    # Drawing the exp orbs to the screen
    for exp_num in range(len(x_y_exp)):
        exp_orb(x_y_exp, exp_size, exp_num)

    # Replacing any enemies or exp orbs that got too far away from the user
    x_y_enemy, x_y_exp, enemy_size, enemy_current_HP, enemies = render(object_range, enemy_num, exp_num, x_y_enemy, x_y_exp, enemies, enemy_size, enemy_current_HP, numProjectiles, numEnemyProjectiles)

    # Checking if each exp orb is less than 100 pixels away from the user. If an orb is close enough, it pulls the exp orb closer, and if it touches the user the orb will be replaced with a new orb and the user's total exp will increase (the bigger the exp orb, the more exp it will give)
    exp_collect = collect_range(x_y_exp, exp_size, exp_collect)

    # Using the health_display function to display the user's health bar
    health_display([(SIZE[0] - vehicle_size) / 2, (SIZE[1] - vehicle_size) / 2], user_max_HP, user_current_HP, vehicle_size)

    # Using the health_display function to display the enemies' health bars
    for i in range(num_enemy):
      health_display(x_y_enemy[i], enemy_health[i], enemy_current_HP[i], enemy_size[i])

    # Blit'ing the total exp collected onto the screen
    text = font.render("Total Exp: " + str(exp_collect), True, BLACK)
    screen.blit(text, [5, 0])

    # Flipping the changes made to the display to the screen
    pygame.display.flip()
    # Setting the maximum framerate of the game to 30 frames per second.
    clock.tick(30)