import pygame
import math
from random import randint
from sklearn.cluster import KMeans

def calculate_distance(p1,p2):
    dimension = len(p1)
    distance = 0
    for i in range(dimension):
        distance += (p1[i] - p2[i])*(p1[i] - p2[i])
    return math.sqrt(distance)

pygame.init()
screen = pygame.display.set_mode((1200,700))
title = pygame.display.set_caption("Data Clustering Simulation")
running = True
clock = pygame.time.Clock()

#Color
BLACK = (0,0,0)
WHITE = (255, 255, 255)
NAVY = (4, 4, 48)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (147, 153, 35)
PURPLE = (255,0,255)
SKY = (0,255,255)
ORANGE = (255,125,25)
GRAPE = (100,25,125)
GRASS = (55,155,65)
COLORS = [RED,GREEN,BLUE,YELLOW,PURPLE,SKY,ORANGE,GRAPE,GRASS]

#Text
font = pygame.font.SysFont('sans', 30)
font_small = pygame.font.SysFont('sans', 20)
font_big = pygame.font.SysFont('sans', 45)
text_plus = font.render('+', True, WHITE)
text_minus = font.render('-', True, WHITE)
text_run = font.render("Run", True, WHITE)
text_random = font.render("Random", True, WHITE)
text_algorithm = font.render("Algorithm", True, WHITE)
text_reset = font.render("Reset", True, WHITE)

K = 0
error = 0
points = []
clusters = []
labels = []

while running:
    clock.tick(60)
    screen.fill(BLACK)

    # INTERFACE
    # Draw panel
    pygame.draw.rect(screen, BLUE, (50, 50, 1100, 500))
    pygame.draw.rect(screen, NAVY, (55, 55, 1090, 490))
    # K button +
    pygame.draw.rect(screen, BLUE, (450, 630, 50, 50))
    pygame.draw.rect(screen, NAVY, (455, 635, 40, 40))
    screen.blit(text_plus, (466, 638))
    # K button -
    pygame.draw.rect(screen, BLUE, (700, 630, 50, 50))
    pygame.draw.rect(screen, NAVY, (705, 635, 40, 40))
    screen.blit(text_minus, (720, 638))
    # K value
    text_k = font_big.render("K = " + str(K), True, WHITE)
    screen.blit(text_k, (550, 630))
    # Run button
    pygame.draw.rect(screen, BLUE, (50, 630, 150, 50))
    pygame.draw.rect(screen, NAVY, (55, 635, 140, 40))
    screen.blit(text_run, (98, 638))
    # Random button
    pygame.draw.rect(screen, BLUE, (250, 630, 150, 50))
    pygame.draw.rect(screen, NAVY, (255, 635, 140, 40))
    screen.blit(text_random, (265, 638))
    # Algorithm button
    pygame.draw.rect(screen, BLUE, (1000, 630, 150, 50))
    pygame.draw.rect(screen, NAVY, (1005, 635, 140, 40))
    screen.blit(text_algorithm, (1010, 638))
    # Reset button
    pygame.draw.rect(screen, BLUE, (800, 630, 150, 50))
    pygame.draw.rect(screen, NAVY, (805, 635, 140, 40))
    screen.blit(text_reset, (830, 638))

    # Draw mouse position when mouse is in panel
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if 50 < mouse_x < 1150 and 50 < mouse_y < 550:
        text_mouse = font_small.render("(" + str(mouse_x - 50) + "," + str(mouse_y - 50) + ")", True, WHITE)
        screen.blit(text_mouse, (mouse_x + 10, mouse_y))

    # INTERACTION
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Create point on panel
            if 50 < mouse_x < 1150 and 50 < mouse_y < 550:
                labels = []
                point = [mouse_x - 50, mouse_y - 50]
                points.append(point)
                # Change K button +
            if 450 < mouse_x < 500 and 630 < mouse_y < 680:
                if K < 8:
                    K = K + 1
                print("Press K +")
            # Change K button -
            if 700 < mouse_x < 750 and 630 < mouse_y < 680:
                if K > 0:
                    K -= 1
                print("Press K -")
                # Random button
            if 250 < mouse_x < 400 and 630 < mouse_y < 780:
                labels = []
                clusters = []
                for i in range(K):
                    random_point = [randint(0, 1100), randint(0, 500)]
                    clusters.append(random_point)
                print("random pressed")
            # Run button
            if 50 < mouse_x < 200 and 630 < mouse_y < 780:
                labels = []

                if clusters == []:
                    continue

                # Assign points to closet clusters
                for p in points:
                    distances_to_cluster = []
                    for c in clusters:
                        dis = calculate_distance(p, c)
                        distances_to_cluster.append(dis)

                    min_distance = min(distances_to_cluster)
                    label = distances_to_cluster.index(min_distance)
                    labels.append(label)

                # Update clusters
                for i in range(K):
                    sum_x = 0
                    sum_y = 0
                    count = 0
                    for j in range(len(points)):
                        if labels[j] == i:
                            sum_x += points[j][0]
                            sum_y += points[j][1]
                            count += 1

                    if count != 0:
                        new_cluster_x = sum_x / count
                        new_cluster_y = sum_y / count
                        clusters[i] = [new_cluster_x, new_cluster_y]

                print("run pressed")
            # Reset button
            if 800 < mouse_x < 950 and 630 < mouse_y < 780:
                K = 0
                error = 0
                points = []
                clusters = []
                labels = []
                print("reset button pressed")
            # Algorithm
            if 1000 < mouse_x < 1150 and 630 < mouse_y < 780:
                try:
                    kmeans = KMeans(n_clusters=K).fit(points)
                    labels = kmeans.predict(points)
                    clusters = kmeans.cluster_centers_
                except:
                    print("error")
                print("Algorithm button pressed")

    # DRAW
    # Draw cluster
    for i in range(len(clusters)):
        pygame.draw.circle(screen, COLORS[i], (int(clusters[i][0]) + 50, int(clusters[i][1]) + 50), 10)
    # Draw point
    for i in range(len(points)):
        pygame.draw.circle(screen, WHITE, (points[i][0] + 50, points[i][1] + 50), 6)
        if labels == []:
            pygame.draw.circle(screen, BLACK, (points[i][0] + 50, points[i][1] + 50), 5)
        else:
            pygame.draw.circle(screen, COLORS[labels[i]], (points[i][0] + 50, points[i][1] + 50), 5)
    # Calculate and draw error
    error = 0
    if clusters != [] and labels != []:
        for i in range(len(points)):
            error += calculate_distance(points[i], clusters[labels[i]])

    text_error = font_big.render("Error = " + str(int(error)), True, WHITE)
    screen.blit(text_error, (518, 565))

    pygame.display.flip()
pygame.quit()

