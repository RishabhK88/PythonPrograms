import pygame
import random

x = pygame.init()

# Colours
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating Window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("SnakesWithRishabh")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, colour, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, colour, [
            x, y, snake_size, snake_size])

# Game Loop


def gameloop():

    # Game Specific Variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    score = 0
    init_velocity = 5
    fps = 50
    snake_size = 20

    f = open("Highscore.txt", "r")
    highscore = f.read()
    f.close()

    while not exit_game:

        if game_over is True:
            gameWindow.fill(white)
            text_screen("Game over! Press Enter Continue",
                        red, 130, 200)
            f = open("Highscore.txt", "w")
            f.write(str(highscore))
            f.close()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x+velocity_x
            snake_y = snake_y+velocity_y

            if abs(snake_x-food_x) < 6 and abs(snake_y-food_y) < 6:
                score += 10
                food_x = random.randint(0, screen_width)
                food_y = random.randint(0, screen_height)
                snk_length += 5
                if score > int(highscore):
                    highscore = score

            gameWindow.fill(white)
            text_screen("Score: " + str(score) + "  Highscore: " +
                        str(highscore),  red, 5, 5)
            pygame.draw.rect(gameWindow, red, [
                food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


gameloop()
