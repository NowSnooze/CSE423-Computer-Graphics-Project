from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
W_Width, W_Height = 500,500
right_bus_x,right_bus_y = -200,-65
right_bus_box=[]
no_road_cross=1
black_hole =[]
pause_box =[-6,6,220,245]
cross_box = [220,250, 220,250]
restart=[-245, -210, 220, 245]
heart_box=[]
gray_heart=False
level = 1
r_car_x=100
r_car_y=-50
l_car_x=-100
l_car_y=-150
a1_x =0
a1_y=0
a2_x =0
a2_y=0
speed=3
cat_x, cat_y = 0, -250  # Cat Position Start at the middle bottom
m_x, m_y = 0, -250
step = 5
pause=False
h_x1 =240 #for upper half circle 1 (heart)
h_x2 =229 #for upper half circle 2 (heart)
h_y1=200
h_y2=200
lives = 3
arrow_f = True
cat=True
start=False#change it to False
l_car_box =[]
r_car_box=[]
char_box = []
arrow_down_box=[]
arrow_up_box=[]
arrow_down_flag=True
arrow_up_flag=True
game_over = False
#coin parameters
coins = []  # List to hold coin positions and directions
coin_speed = 2
coin_radius = 7
max_coins = 6
score=0
def mouseListener(button, state, x, y):
    if button == GLUT_LEFT_BUTTON:
        if (state == GLUT_DOWN):
            global cat,start,step,pause_box,cross_box,restart,game_over,pause,\
                right_bus_x,right_bus_y,right_bus_box,black_hole,\
               heart_box,gray_heart, r_car_x,r_car_y,l_car_y,\
                l_car_x,a1_x,a1_y,a2_x,a2_y,cat_x, cat_y,m_x, m_y,h_x1 ,h_x2,h_y1,h_y2,lives,arrow_f,\
                l_car_box,r_car_box ,char_box,arrow_down_box,arrow_up_box,arrow_down_flag,arrow_up_flag,\
                coins,coin_speed,coin_radius,max_coins,score
            c_x, c_y = mouse_convert_coordinate(x, y)
            if start==False and -130<=c_x<=-30 and 0<=c_y<=100:
                cat=True
                step =3
                print("Your character is cat")
            if start==False and 10<=c_x<=110 and 0<=c_y<=100:
                cat=False
                step=5
                print("Your character is mouse")
            if start == False and -25 <= c_x <= 25 and -155 <= c_y <= -110:
                start=True
                print("Starting the game")
            x_min = pause_box[0]
            x_max = pause_box[1]
            y_min = pause_box[2]
            y_max = pause_box[3]
            c_x, c_y = mouse_convert_coordinate(x, y)
            if x_min<=c_x<=x_max and y_min<=c_y<=y_max and game_over==False:
                if pause:
                    pause = False #will show pause button
                else:
                    pause = True #will show play button
            x_min = restart[0]
            x_max = restart[1]
            y_min = restart[2]
            y_max = restart[3]
            c_x, c_y = mouse_convert_coordinate(x, y)
            if x_min<=c_x<=x_max and y_min<=c_y<=y_max:
                #again initializing global variables
                game_over=False
                left_bus_x, left_bus_y = 0, 0
                right_bus_x, right_bus_y = -200, -65
                right_bus_box = []
                black_hole = []
                heart_box = []
                gray_heart = False
                r_car_x = 100
                r_car_y = -50
                l_car_x = -100
                l_car_y = -150
                a1_x = 0
                a1_y = 0
                a2_x = 0
                a2_y = 0
                cat_x, cat_y = 0, -250  # Cat Position Start at the middle bottom
                m_x, m_y = 0, -250
                h_x1 = 240  # for upper half circle 1 (heart)
                h_x2 = 229  # for upper half circle 2 (heart)
                h_y1 = 200
                h_y2 = 200
                lives = 3
                arrow_f = True
                l_car_box = []
                r_car_box = []
                char_box = []
                arrow_down_box = []
                arrow_up_box = []
                arrow_down_flag = True
                arrow_up_flag = True
                coins = []  # List to hold coin positions and directions
                coin_speed = 2
                coin_radius = 7
                max_coins = 6
                score = 0
                print("Starting Over")
            x_min = cross_box[0]
            x_max = cross_box[1]
            y_min = cross_box[2]
            y_max = cross_box[3]
            c_x, c_y = mouse_convert_coordinate(x, y)
            if x_min <= c_x <= x_max and y_min <= c_y <= y_max:
                print("Goodbye")
                print("Final Score:", score)
                glutLeaveMainLoop()
                # exit()
    glutPostRedisplay()
def generate_coin():
    if len(coins) < max_coins:  # Ensure we don't exceed the maximum number of coins
        side = random.choice(["left", "right"])
        lane_y = random.choice([-152.5, -57.5, 37.5, 132.5])
        if side == "left":
            x_pos = -250  # Start from the left side
            direction = 1  # Move right
        else:
            x_pos = 250  # Start from the right side
            direction = -1  # Move left

        coins.append({"x": x_pos, "y": lane_y, "direction": direction})
def draw_coin(x, y):
    glColor3f(1, 1, 0)  # Yellow color for coins
    glPointSize(3)
    draw_circle(coin_radius, x, y)


def update_coins():
    global coins
    # Create a new list to store updated coins
    updated_coins = []
    # Loop through each coin
    for coin in coins:
        # Update the coin's position
        coin["x"] = coin["x"] + (coin["direction"] * coin_speed)
        # Check if the coin is within bounds
        if coin["x"] >= -260 and coin["x"] <= 260:
            # Add the coin to the updated list if it's still on-screen
            updated_coins.append(coin)
    # Replace the global coins list with the updated list
    coins = updated_coins


def right_bus():
    global right_bus_x, right_bus_y, right_bus_box
    #scale = 0.4
    h= 0
    glColor3f(0, 1, 0.67)
    for i in range(2):
        right_bus_box.append([right_bus_x, right_bus_x + 150, right_bus_y + 50 + h, right_bus_y - 10 + h])

        draw_line(right_bus_x, right_bus_y + h, right_bus_x + 20, right_bus_y + h)  # 1-2
        draw_upper_half_circle(15, right_bus_x + 35, right_bus_y + h)  # 2-3
        draw_line(right_bus_x + 50, right_bus_y + h, right_bus_x + 90, right_bus_y + h)  # 3-4
        draw_upper_half_circle(15, right_bus_x + 105, right_bus_y + h)  # 4-5
        draw_line(right_bus_x + 120, right_bus_y + h, right_bus_x + 150, right_bus_y + h)  # 5-6
        draw_line(right_bus_x, right_bus_y + h, right_bus_x, right_bus_y + 20 + h)  # 1-7
        draw_line(right_bus_x, right_bus_y + 20 + h, right_bus_x + 5, right_bus_y + 50 + h)  # 7-8
        draw_line(right_bus_x + 5, right_bus_y + 50 + h, right_bus_x + 145, right_bus_y + 50 + h)  # 8-9
        draw_line(right_bus_x + 145, right_bus_y + 50 + h, right_bus_x + 150, right_bus_y + 35 + h)  # 9=10
        draw_line(right_bus_x + 150, right_bus_y + 35 + h, right_bus_x + 150, right_bus_y + h)  # 10-6
        draw_line(right_bus_x + 35, right_bus_y + 50 + h, right_bus_x + 35, right_bus_y + 15 + h)  # 11-12
        draw_line(right_bus_x + 35, right_bus_y + 20 + h, right_bus_x + 150, right_bus_y + 20 + h)  # 13-14
        draw_line(right_bus_x, right_bus_y + 13 + h, right_bus_x + 10, right_bus_y + 13 + h)  # 37-38
        draw_line(right_bus_x + 10, right_bus_y + 13 + h, right_bus_x + 10, right_bus_y + 7 + h)  # 38-39
        draw_line(right_bus_x, right_bus_y + 7 + h, right_bus_x + 10, right_bus_y + 7 + h)  # 40-39
        draw_line(right_bus_x + 12, right_bus_y + 43 + h, right_bus_x + 28, right_bus_y + 43 + h)  # 15-16
        draw_line(right_bus_x + 12, right_bus_y + 43 + h, right_bus_x + 7, right_bus_y + 20 + h)  # 15-17
        draw_line(right_bus_x + 7, right_bus_y + 20 + h, right_bus_x + 28, right_bus_y + 20 + h)  # 17-18
        draw_line(right_bus_x + 28, right_bus_y + 43 + h, right_bus_x + 28, right_bus_y + 20 + h)  # 16-18
        draw_circle(10, right_bus_x + 35, right_bus_y + h)
        draw_circle(10, right_bus_x + 105, right_bus_y + h)
        h =180
def mouse_convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y
    return a,b

def draw_points(x, y,n=2):
    glPointSize(n)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
def draw_road():
    # Draw road borders using GL_LINES
    glColor3f(0.2, 0.2, 0.2)
    draw_line(-250, -200, 250, -200,5)  # Bottom border
    draw_line(-250, -105, 250, -105,5)
    draw_line(-250, -10, 250, -10,5)
    draw_line(-250, 85, 250, 85,5)
    draw_line(-250, 180, 250, 180,5)    # Top border

    # Draw horizontal lanes using GL_LINES
    glColor3f(1, 1, 1)  # White color
      # Horizontal dashed lane centerline
    gap = 30
    for i in range(-250,250,70):
        draw_line(i,-152.5,i+gap,-152.5,10)
        draw_line(i, -57.5, i + gap, -57.5,10)
        draw_line(i, 37.5, i + gap, 37.5,10)
        draw_line(i, 132.5, i + gap, 132.5,10)

def draw_circle(r,cx,cy):
    d = 1 - r
    x = r
    y = 0
    while y <= x:
        for zone in range(8):
            new_x, new_y = convert_co_ordinates(x, y, zone)
            draw_points(new_x+cx,new_y+cy)
        if d <= 0:
            d = d + 2 * y + 3
        else:
            d = d + 2 * (y - x) + 5
            x -= 1
        y += 1
def draw_upper_half_circle(r, cx, cy,lower=False):
    d = 1 - r
    x = r
    y = 0

    while y <= x:
        for zone in range(8):
            new_x, new_y = convert_co_ordinates(x, y, zone)

            if lower==False:
                # Only draw points upper half
                if new_y + cy >= cy:
                    draw_points(new_x + cx, new_y + cy)
            else:
                if new_y + cy <= cy:
                    draw_points(new_x + cx, new_y + cy)

        if d <= 0:
            d = d + 2 * y + 3
        else:
            d = d + 2 * (y - x) + 5
            x -= 1
        y += 1

def left_car():
    global l_car_x, l_car_y,l_car_box
    scale = 0.37
    # # box checking
    # draw_line(l_car_box[0][0], l_car_box[0][2], l_car_box[0][1], l_car_box[0][2])
    # draw_line(l_car_box[0][1], l_car_box[0][2], l_car_box[0][1], l_car_box[0][3])
    # draw_line(l_car_box[0][1], l_car_box[0][3], l_car_box[0][0], l_car_box[0][3])
    # draw_line(l_car_box[0][0], l_car_box[0][3], l_car_box[0][0], l_car_box[0][2])
    # Mirrored Lines
    h=0
    for i in range(2):
        l_car_box.append([l_car_x - 290 * scale, l_car_x + 0 * scale, l_car_y - 55 * scale+h, l_car_y + 80 * scale+h])
        draw_line(l_car_x, l_car_y + h, l_car_x - 50 * scale, l_car_y - 17 * scale + h)  # Mirrored 1-2
        draw_line(l_car_x - 50 * scale, l_car_y - 17 * scale + h, l_car_x - 50 * scale,l_car_y - 40 * scale + h)  # Mirrored 2-4
        draw_line(l_car_x, l_car_y + h, l_car_x, l_car_y - 23 * scale + h)  # Mirrored 1-3
        draw_line(l_car_x, l_car_y - 23 * scale + h, l_car_x - 50 * scale, l_car_y - 40 * scale + h)  # Mirrored 3-4
        draw_line(l_car_x, l_car_y + h, l_car_x - 60 * scale, l_car_y + 35 * scale + h)  # Mirrored 1-5
        draw_line(l_car_x - 50 * scale, l_car_y - 17 * scale + h, l_car_x - 110 * scale,l_car_y + 25 * scale + h)  # Mirrored 2-6
        draw_line(l_car_x - 60 * scale, l_car_y + 35 * scale + h, l_car_x - 110 * scale,l_car_y + 25 * scale + h)  # Mirrored 5-6
        draw_line(l_car_x - 60 * scale, l_car_y + 35 * scale + h, l_car_x - 103 * scale,l_car_y + 80 * scale + h)  # Mirrored 5-7
        draw_line(l_car_x - 110 * scale, l_car_y + 25 * scale + h, l_car_x - 155 * scale,l_car_y + 73 * scale + h)  # Mirrored 6-8
        draw_line(l_car_x - 103 * scale, l_car_y + 80 * scale + h, l_car_x - 155 * scale,l_car_y + 73 * scale + h)  # Mirrored 7-8
        draw_line(l_car_x - 103 * scale, l_car_y + 80 * scale + h, l_car_x - 205 * scale,l_car_y + 80 * scale + h)  # Mirrored 7-9
        draw_line(l_car_x - 155 * scale, l_car_y + 73 * scale + h, l_car_x - 220 * scale,l_car_y + 72 * scale + h)  # Mirrored 8-10
        draw_line(l_car_x - 205 * scale, l_car_y + 80 * scale + h, l_car_x - 220 * scale, l_car_y + 72 * scale + h)  # Mirrored 9-10
        draw_line(l_car_x - 110 * scale, l_car_y + 25 * scale + h, l_car_x - 250 * scale,l_car_y + 25 * scale + h)  # Mirrored 6-11
        draw_line(l_car_x - 220 * scale, l_car_y + 72 * scale + h, l_car_x - 250 * scale, l_car_y + 25 * scale + h)  # Mirrored 10-11
        draw_line(l_car_x - 250 * scale, l_car_y + 25 * scale + h, l_car_x - 290 * scale, l_car_y - 5 * scale + h)  # Mirrored 11-12
        draw_line(l_car_x - 290 * scale, l_car_y - 5 * scale + h, l_car_x - 290 * scale,l_car_y - 25 * scale + h)  # Mirrored 12-13
        draw_line(l_car_x - 50 * scale, l_car_y - 40 * scale + h, l_car_x - 115 * scale, l_car_y - 38 * scale + h)  # Mirrored 4-17
        draw_upper_half_circle(10.5, l_car_x - 135 * scale, l_car_y - 38 * scale + h)  # Mirrored Circle
        draw_circle(7, l_car_x - 135 * scale, l_car_y - 40 * scale + h)  # Mirrored Circle
        draw_upper_half_circle(10.5, l_car_x - 228 * scale, l_car_y - 31 * scale + h)  # Mirrored Circle
        draw_circle(7, l_car_x - 228 * scale, l_car_y - 35 * scale + h)  # Mirrored Circle
        draw_line(l_car_x - 158 * scale, l_car_y - 40 * scale + h, l_car_x - 207 * scale, l_car_y - 37 * scale + h)  # Mirrored 16-15
        draw_line(l_car_x - 225 * scale, l_car_y - 40 * scale + h, l_car_x - 290 * scale,l_car_y - 25 * scale + h)  # Mirrored 14-13
        draw_line(l_car_x - 185 * scale, l_car_y + 73 * scale + h, l_car_x - 185 * scale,  l_car_y + 25 * scale + h)  # Mirrored 18-19
        h=190


def right_car():
    global r_car_x, r_car_y,r_car_box
    scale = 0.37 # to make the car smaller
    h = 0
    glColor3f(0.9, 0, 0)
    for i in range(2):
        r_car_box.append([r_car_x - 5 * scale, r_car_x + 290 * scale, r_car_y - 60 * scale+h, r_car_y + 80 * scale+h])
        draw_line(r_car_x, r_car_y + h, r_car_x + 50 * scale, r_car_y - 17 * scale + h)  # 1-2
        draw_line(r_car_x + 50 * scale, r_car_y - 17 * scale + h, r_car_x + 50 * scale, r_car_y - 40 * scale + h)  # 2-4
        draw_line(r_car_x, r_car_y + h, r_car_x, r_car_y - 23 * scale + h)  # 1-3
        draw_line(r_car_x, r_car_y - 23 * scale + h, r_car_x + 50 * scale, r_car_y - 40 * scale + h)  # 3-4
        draw_line(r_car_x, r_car_y + h, r_car_x + 60 * scale, r_car_y + 35 * scale + h)  # 1-5
        draw_line(r_car_x + 50 * scale, r_car_y - 17 * scale + h, r_car_x + 110 * scale, r_car_y + 25 * scale + h)  # 2-6
        draw_line(r_car_x + 60 * scale, r_car_y + 35 * scale + h, r_car_x + 110 * scale, r_car_y + 25 * scale + h)  # 5-6
        draw_line(r_car_x + 60 * scale, r_car_y + 35 * scale + h, r_car_x + 103 * scale, r_car_y + 80 * scale + h)  # 5-7
        draw_line(r_car_x + 110 * scale, r_car_y + 25 * scale + h, r_car_x + 155 * scale, r_car_y + 73 * scale + h)  # 6-8
        draw_line(r_car_x + 103 * scale, r_car_y + 80 * scale + h, r_car_x + 155 * scale,r_car_y + 73 * scale + h)  # 7-8
        draw_line(r_car_x + 103 * scale, r_car_y + 80 * scale + h, r_car_x + 205 * scale, r_car_y + 80 * scale + h)  # 7-9
        draw_line(r_car_x + 155 * scale, r_car_y + 73 * scale + h, r_car_x + 220 * scale, r_car_y + 72 * scale + h)  # 8-10
        draw_line(r_car_x + 205 * scale, r_car_y + 80 * scale + h, r_car_x + 220 * scale,r_car_y + 72 * scale + h)  # 9-10
        draw_line(r_car_x + 110 * scale, r_car_y + 25 * scale + h, r_car_x + 250 * scale, r_car_y + 25 * scale + h)  # 6-11
        draw_line(r_car_x + 220 * scale, r_car_y + 72 * scale + h, r_car_x + 250 * scale,r_car_y + 25 * scale + h)  # 10-11
        draw_line(r_car_x + 250 * scale, r_car_y + 25 * scale + h, r_car_x + 290 * scale, r_car_y - 5 * scale + h)  # 11-12
        draw_line(r_car_x + 290 * scale, r_car_y - 5 * scale + h, r_car_x + 290 * scale,r_car_y - 25 * scale + h)  # 12-13
        draw_line(r_car_x + 50 * scale, r_car_y - 40 * scale + h, r_car_x + 115 * scale, r_car_y - 38 * scale + h)  # 4-17
        draw_upper_half_circle(10.5, r_car_x + 135 * scale, r_car_y - 38 * scale + h)  # Circle
        draw_circle(7, r_car_x + 135 * scale, r_car_y - 40 * scale + h)  # Circle
        draw_upper_half_circle(10.5, r_car_x + 228 * scale, r_car_y - 31 * scale + h)  # Circle
        draw_circle(7, r_car_x + 228 * scale, r_car_y - 35 * scale + h)  # Circle
        draw_line(r_car_x + 158 * scale, r_car_y - 40 * scale + h, r_car_x + 207 * scale,r_car_y - 37 * scale + h)  # 16-15
        draw_line(r_car_x + 225 * scale, r_car_y - 40 * scale + h, r_car_x + 290 * scale,r_car_y - 25 * scale + h)  # 14-13
        draw_line(r_car_x + 185 * scale, r_car_y + 73 * scale + h, r_car_x + 185 * scale, r_car_y + 25 * scale + h)  # 18-19
        # # # box checking
        # print(r_car_box[0][2],r_car_box[0][3])
        # draw_line(r_car_box[0][0], r_car_box[0][2], r_car_box[0][1], r_car_box[0][2])
        # draw_line(r_car_box[0][1], r_car_box[0][2], r_car_box[0][1], r_car_box[0][3])
        # draw_line(r_car_box[0][1], r_car_box[0][3], r_car_box[0][0], r_car_box[0][3])
        # draw_line(r_car_box[0][0], r_car_box[0][3], r_car_box[0][0], r_car_box[0][2])
        h=180

def keyboard(key, x, y):
    global cat,pause
    if pause==False and game_over==False:
        if cat:
            global cat_x, cat_y
            if key == b'a' and cat_x>-250:
                cat_x -= step
            elif key == b'd' and cat_x<245:
                cat_x += step
            elif key == b'w' and cat_y<200:
                cat_y += step
            elif key == b's' and cat_y>-245:
                cat_y -= step
        else:
            global m_x, m_y
            if key == b'a' and m_x>-245:
                m_x -= step
            elif key == b'd' and m_x<245:
                m_x += step
            elif key == b'w' and m_y<200:
                m_y += step
            elif key == b's' and m_y>-245:
                m_y -= step
    glutPostRedisplay()
def draw_cat():
    global cat_x, cat_y,char_box
    char_box = [cat_x - 10, cat_x + 10, cat_y - 10, cat_y + 18]
    # #box checking
    # draw_line(char_box[0], char_box[2], char_box[1], char_box[2])
    # draw_line(char_box[1], char_box[2], char_box[1], char_box[3])
    # draw_line(char_box[1], char_box[3], char_box[0], char_box[3])
    # draw_line(char_box[0], char_box[3], char_box[0], char_box[2])
    glColor3f(0, 0, 0)
    draw_circle(8,cat_x, cat_y +14) # head draw
    #body draw korbe
    draw_line(cat_x - 6, cat_y - 10, cat_x + 6, cat_y - 10)
    draw_line(cat_x - 6, cat_y - 10, cat_x - 6, cat_y + 10)
    draw_line(cat_x + 6, cat_y - 10, cat_x + 6, cat_y + 10)
    # Left ear drawing
    draw_line(cat_x - 8, cat_y + 20, cat_x - 4, cat_y + 30) #1-2
    draw_line(cat_x - 4, cat_y + 30, cat_x, cat_y + 20) #2-3
    draw_line(cat_x - 8, cat_y + 20, cat_x, cat_y + 20) #1-3
    # Right ear drawing
    draw_line(cat_x, cat_y + 20, cat_x + 4, cat_y + 30)
    draw_line(cat_x + 4, cat_y + 30, cat_x + 8, cat_y + 20)
    draw_line(cat_x, cat_y + 20, cat_x + 8, cat_y + 20)
    # Tail part
    tail_points = [
        (cat_x, cat_y - 10),
        (cat_x + 2, cat_y - 15),
        (cat_x, cat_y - 20),
        (cat_x - 2, cat_y - 25),
    ]
    for i in range(len(tail_points) - 1):
        draw_line(tail_points[i][0], tail_points[i][1], tail_points[i + 1][0], tail_points[i + 1][1])


def draw_mouse():
    global m_x, m_y,char_box
    char_box = [m_x-10,m_x+10,m_y-16,m_y+8]
    # #box checking
    # draw_line(char_box[0], char_box[2], char_box[1], char_box[2])
    # draw_line(char_box[1], char_box[2], char_box[1], char_box[3])
    # draw_line(char_box[1], char_box[3], char_box[0], char_box[3])
    # draw_line(char_box[0], char_box[3], char_box[0], char_box[2])
    glColor3f(0.9, 0.7, 0.5)
    draw_circle(8,m_x, m_y-1) # head draw
    #body draw korbe
    draw_upper_half_circle(9,m_x, m_y -5,True) # head draw
    # Left ear drawing
    draw_line(m_x - 8, m_y + 9, m_x - 4, m_y + 17) #1-2
    draw_line(m_x - 4, m_y + 17, m_x, m_y + 9) #2-3
    draw_line(m_x - 8, m_y+ 9, m_x, m_y +9) #1-3
    # Right ear drawing
    draw_line(m_x, m_y + 9, m_x + 4, m_y + 17)
    draw_line(m_x + 4, m_y + 17,m_x + 8, m_y + 9)
    draw_line(m_x, m_y + 9, m_x + 8, m_y + 9)
    # Tail part
    tail_points = [
        (m_x, m_y - 15),
        (m_x + 2, m_y - 20),
        (m_x, m_y - 25),
        (m_x - 2, m_y - 30),
    ]
    for i in range(len(tail_points) - 1):
        draw_line(tail_points[i][0], tail_points[i][1], tail_points[i + 1][0], tail_points[i + 1][1])

def draw_line(x0, y0, x1, y1,n=2):
    zone = find_zone(x0, y0, x1, y1)
    x0, y0 = convert_co_ordinates(x0, y0, zone)
    x1, y1 = convert_co_ordinates(x1, y1, zone)
    dx = x1 - x0
    dy = y1 - y0
    d = 2 * dy - dx
    de = 2 * dy
    dne = 2 * (dy - dx)
    x, y = x0, y0
    new_x, new_y = convert_co_ordinates(x, y, zone, True)
    draw_points(new_x, new_y,n)
    while x < x1:
        if d <= 0:
            d += de
        else:
            d += dne
            y += 1
        x += 1
        new_x,new_y = convert_co_ordinates(x,y,zone,True)
        draw_points(new_x, new_y,n)


# Find the zone of the line
def find_zone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            return 0  # Zone 0
        elif dx <= 0 and dy >= 0:
            return 3  # Zone 3
        elif dx <= 0 and dy <= 0:
            return 4  # Zone 4
        elif dx >= 0 and dy <= 0:
            return 7  # Zone 7
    else:
        if dx >= 0 and dy >= 0:
            return 1  # Zone 1
        elif dx <= 0 and dy >= 0:
            return 2  # Zone 2
        elif dx <= 0 and dy <= 0:
            return 5  # Zone 5
        elif dx >= 0 and dy <= 0:
            return 6  # Zone 6

def convert_co_ordinates(x, y, zone, reverse=False):
    if zone == 0:
        return (x, y)
    elif zone == 1:
        return (y, x)
    elif zone == 2:
        if reverse:
            return (-y, x) #covert zone 0 to zone 2
        return (y, -x)
    elif zone == 3:
        return (-x, y)
    elif zone == 4:
        return (-x, -y)
    elif zone == 5:
        return (-y, -x)
    elif zone == 6:
        if reverse:
            return (y, -x) #covert zone 0 to zone 6
        return (-y, x)
    elif zone == 7:
        return (x, -y)

def starting():
    global start,cat_x, cat_y,m_x,m_y,level,no_road_cross,speed,cat,step,lives,heart_box,\
        gray_heart,arrow_down_box,arrow_up_box,arrow_down_flag,arrow_up_flag,arrow_f,right_bus_box
    if level==1:
        speed=3
        no_road_cross=1
        glColor3f(0.3, 0.0, 0.5)
        draw_circle(8, -10,200)
        draw_line(-10, 150, -10, 180,6)
    if level==2:
        speed=5
        no_road_cross = 2
        glColor3f(0.3, 0.0, 0.5)
        draw_circle(8, -30,200)
        draw_line(-30, 150, -30, 180,6)
        draw_circle(8, 10, 200)
        draw_line(10, 150, 10, 180, 6)
    if level==3:
        speed = 6
        no_road_cross = 3
        glColor3f(0.3, 0.0, 0.5)
        draw_circle(8, -40, 200)
        draw_line(-40, 150, -40, 180, 6)
        draw_circle(8, -15, 200)
        draw_line(-15, 150, -15, 180, 6)
        draw_circle(8, 10, 200)
        draw_line(10, 150, 10, 180, 6)
    if cat:
        step=3
    else:
        step=5
    lives = 3
    heart_box = []
    gray_heart = False
    arrow_down_box = []
    arrow_up_box = []
    arrow_down_flag = True
    arrow_up_flag = True
    arrow_f = True
    right_bus_box = []
    #cat_box(-130,-30,0,100)
    glColor3f(0.3, 0.0, 0.5)
    draw_line(-130, 100, -30, 100)
    draw_line(-130, 100, -130, 0)
    draw_line(-30, 100, -30, 0)
    draw_line(-130, 0, -30, 0)
    cat_x, cat_y = -80, 50
    draw_cat()
    cat_x, cat_y = 0, -250
    # box(10,110,0,100)
    glColor3f(0.3, 0.0, 0.5)
    draw_line(10, 100, 110, 100)
    draw_line(10, 100, 10, 0)
    draw_line(110, 100, 110, 0)
    draw_line(10, 0, 110, 0)
    m_x, m_y=60,50
    draw_mouse()
    m_x, m_y = 0, -250
    glColor3f(0.4, 0.7, 0.7)
    draw_line(-5, -140, -5, -125)
    draw_line(-5, -140, 5, -133)
    draw_line(-5, -125, 5, -133)
    #box(-25,25,-110,-155)
    glColor3f(0.3, 0.0, 0.5)
    draw_line(-25, -155, -25, -110)
    draw_line(-25, -155, 25, -155)
    draw_line(-25, -110, 25, -110)
    draw_line(25, -110, 25, -155)
def draw_heart():
        global gray_heart,lives
        x = 0
        glColor3f(0.8, 0, 0.5)
        if gray_heart:
            count=lives-1
        else:
            count=lives
        for i in range(count):
            draw_upper_half_circle(5,h_x1+x+11,h_y1) #1
            draw_upper_half_circle(5, h_x2+x+11, h_y2) #2
            draw_line(h_x1-5+x, 200, h_x1+5+x, 190) #1-3
            draw_line(h_x1+16+x, 200, h_x1+5+x, 190) #2-3
            x-=30
        if gray_heart:
            glColor3f(0.3, 0.3, 0.3)
            draw_upper_half_circle(5, h_x1 + x + 11, h_y1)  # 1
            draw_upper_half_circle(5, h_x2 + x + 11, h_y2)  # 2
            draw_line(h_x1 - 5 + x, 200, h_x1 + 5 + x, 190)  # 1-3
            draw_line(h_x1 + 16 + x, 200, h_x1 + 5 + x, 190)  # 2-3

def hole():
    global black_hole
    # Randomly generating x and y within the specified range
    x = random.uniform(-210, 210)
    y = random.uniform(-220, -150)
    black_hole.append([x,y]) #start
    x = random.uniform(-210, 210)
    y = random.uniform(50, 100)
    black_hole.append([x,y]) #end
def heart():
    global heart_box,char_box,lives
    if heart_box == []:
        x = random.uniform(-240, 240)
        y = random.uniform(-200, 170)
        heart_box.append(x)
        heart_box.append(y)
    else:
        #check if it char gets heart
        x_min_char = char_box[0]
        x_max_char = char_box[1]
        y_min_char = char_box[2]
        y_max_char = char_box[3]
        x=heart_box[0]
        y=heart_box[1]
        if (x-5 < x_max_char and x+16 > x_min_char and
                y-10 < y_max_char and y+5> y_min_char):
            heart_box=[0]
            lives+=1
        else:
            glColor3f(0.8, 0, 0.5)
            draw_upper_half_circle(5, x, y)  # 1
            draw_upper_half_circle(5, x + 11, y)  # 2
            draw_line(- 5 + x, y, 5 + x, y - 10)  # 1-3
            draw_line(16 + x, y, 5 + x, y - 10)  # 2-3

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor( 0.471,  0.471,  0.471, 0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    global arrow_f,a1_x,a1_y,a2_y,a2_x
    if start:
        glColor3f(1, 1, 0.4)
        #end_point_box=[-7,10,190,205]
        draw_line(-5, 205, -5, 190, 5)
        draw_line(-5, 205, 8, 205, 5)
        draw_line(-5, 198, 6, 198, 5)
        draw_line(-5, 190, 8, 190, 5)
        if arrow_f and (level==2 or level==3): # so that random number is being generated only one time
            def distance(x1, y1, x2, y2):
                return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            # Generate a1's coordinates
            a1_y = random.randint(-200, 170)
            a1_x = random.randint(-220, 220)

            # Generate a2's coordinates and ensure it doesn't overlap with a1
            while True:
                a2_y = random.randint(-200, 170)
                a2_x = random.randint(-220, 220)
                if distance(a1_x, a1_y, a2_x, a2_y) > 150:  # Replace 20 with your minimum distance
                    break
            arrow_f = False
        draw_road() #which ever we draw 1st is in the behind
        if level==2 or level==3:
            arrow(a1_x, a1_y, a2_x, a2_y)
        if cat:
            draw_cat()
        else:
            draw_mouse()
        right_car()
        left_car()
        if level==3:
            right_bus()
        if heart_box!=[0] and level!=1: #to stop drawing
            heart()
        for coin in coins:
            draw_coin(coin["x"], coin["y"])
        if level != 1:
            speed_up_down() #put after the arrow() function
        check_coin_collection()
        add_score()
        # arrow (box: -245, -220, 230, 245)
        glColor3f(0, 0, 1)
        draw_line(-240, 235, -225, 235,5)
        draw_line(-240, 235, -235, 230,5)
        draw_line(-240, 235, -235, 240,5)
        # cross (box: x=230-250, y=230-250)
        glColor3f(0, 1, 0)
        draw_line(235, 240, 245, 230,3)
        draw_line(235, 230, 245, 240,3)
        glColor3f(1, 0.5, 0)

        if pause == False:
            draw_line(-3, 240, -3, 228,3)
            draw_line(3, 240, 3, 228,3)
        else:
            draw_line(-5, 240, -5, 225)
            draw_line(-5, 240, 5, 233)
            draw_line(-5, 225, 5, 233)
        glColor3f(0, 0, 0)
        draw_line(-250, 219, 250, 219)
        glColor3f(1, 0, 0)
        draw_heart()
        if level == 3:
            if black_hole==[]:
                hole()
            elif black_hole==[0]: #to stop drawing
                pass
            else:
                x,y=black_hole[0]
                glColor3f(0, 0.1, 1)
                draw_circle(10, x,y)
                x,y=black_hole[1]
                draw_circle(10, x, y)
    else:
        starting()
    glutSwapBuffers()

# Initialize OpenGL
def init():
    glClearColor(0, 0, 0, 0)  # Clear the screen
    glMatrixMode(GL_PROJECTION)  # Load the projection matrix
    glLoadIdentity()  # Initialize the matrix
    gluPerspective(104, 1, 1, 1000.0)
    # Perspective parameters


# OpenGL viewport settings
def iterate():
    glViewport(0, 0, W_Width, W_Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, W_Width, 0.0, W_Height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
def check_coin_collection():
    global char_box, coin_radius, score
    char_left = char_box[0]
    char_right = char_box[1]
    char_bottom = char_box[2]
    char_top = char_box[3]

    for coin in coins:
        coin_left = coin['x'] - coin_radius
        coin_right = coin['x'] + coin_radius
        coin_bottom = coin['y'] - coin_radius
        coin_top = coin['y'] + coin_radius
        # AABB collision check
        if (char_left < coin_right and
                char_right > coin_left and
                char_top > coin_bottom and
                char_bottom < coin_top):
            coins.remove(coin)
            score += 10
            print(f"Coin Collected!! The Score is now {score}")

def add_score():
    global score, char_box,m_x, m_y,cat_x,cat_y,no_road_cross,level,start,lives
    char_bottom = char_box[2]
    if char_bottom >= 180:
        score += 5
        no_road_cross-=1
        m_x, m_y = 0, -250
        cat_x, cat_y = 0, -250
        print("5 points added!!")
        if level!=1: #as for level 1 we need to cross road only one time
            print(f"You only need to cross {no_road_cross} more times!")
        if no_road_cross==0 and level!=3:
            print(f"Congrats you completed level {level}!!")
            print(f"Total score for level {level}: {score}")
            score=0
            level+=1
            start=False
            lives = 3
        elif level==3 and no_road_cross==0:
            print(f"Congrats you cleared all the levels!!")
            print(f"Total score for level {level}: {score}")
            glutLeaveMainLoop()

def check_collision():
    global l_car_box, char_box,r_car_box

    # Extract character's bounding box
    x_min_char = char_box[0]
    x_max_char = char_box[1]
    y_min_char = char_box[2]
    y_max_char = char_box[3]

    # Check collision with each bounding box in the car
    for car in l_car_box:
        x_min_car = car[0]
        x_max_car = car[1]
        y_min_car = car[2]
        y_max_car = car[3]

    # Axis-Aligned Bounding Box (AABB) collision detection
        if (x_min_car < x_max_char and x_max_car > x_min_char and
                y_min_car < y_max_char and y_max_car > y_min_char):
                print("Collision detected with car!! You lost a live!!")
                return True  # Collision detected
    for car in r_car_box:
        x_min_car = car[0]
        x_max_car = car[1]
        y_min_car = car[2]
        y_max_car = car[3]

    # Axis-Aligned Bounding Box (AABB) collision detection
        if (x_min_car < x_max_char and x_max_car > x_min_char and
                y_min_car < y_max_char and y_max_car > y_min_char):
            print("Collision detected with car!! You lost a live!!")
            return True  # Collision detected
    for bus in right_bus_box:
        left = bus[0]
        right = bus[1]
        top = bus[2]
        bottom = bus[3]

        if (left < x_max_char and right > x_min_char and
                bottom < y_max_char and top > y_min_char):
            print("Oopsie!! You just lost a life T-T")
            return True  # Collision detected
    return False  # No collision detected

def arrow(x,y,x1,y1):
    global arrow_up_box,arrow_down_box,arrow_up_flag,arrow_down_flag
    #upward
    if arrow_up_flag:
        arrow_up_box = [x-9, x+9, y-5, y+23]
        glColor3f(1.0, 0.647, 0.0)
        draw_line(x, y, x, y+10, 5)
        draw_line(x-5, y+10, x+5, y+10, 5)
        draw_line(x-5, y+10, x+2, y+18, 5)
        draw_line(x+2, y+18, x+5, y+10, 5)
        # draw_line(arrow_up_box[0], arrow_up_box[2], arrow_up_box[1], arrow_up_box[2])
        # draw_line(arrow_up_box[1], arrow_up_box[2], arrow_up_box[1], arrow_up_box[3])
        # draw_line(arrow_up_box[1], arrow_up_box[3], arrow_up_box[0], arrow_up_box[3])
        # draw_line(arrow_up_box[0], arrow_up_box[3], arrow_up_box[0], arrow_up_box[2])
    if arrow_down_flag:
        # #downward
        arrow_down_box = [x1-9, x1+9, y1-23,y1+5]
        # draw_line(arrow_down_box[0], arrow_down_box[2], arrow_down_box[1], arrow_down_box[2])
        # draw_line(arrow_down_box[1], arrow_down_box[2], arrow_down_box[1], arrow_down_box[3])
        # draw_line(arrow_down_box[1], arrow_down_box[3], arrow_down_box[0], arrow_down_box[3])
        # draw_line(arrow_down_box[0], arrow_down_box[3], arrow_down_box[0], arrow_down_box[2])
        glColor3f(1.0, 0.75, 0.8)
        draw_line(x1, y1, x1, y1-10, 5) #line
        draw_line(x1-5, y1-10, x1+5, y1-10, 5)
        draw_line(x1-5, y1-10, x1-2, y1-18, 5)
        draw_line(x1+5, y1-10, x1+2, y1-18, 5)

def speed_up_down():
    global arrow_up_box,arrow_down_box,speed,char_box,arrow_up_flag,arrow_down_flag,step
    # Extract character's bounding box
    x_min_char = char_box[0]
    x_max_char = char_box[1]
    y_min_char = char_box[2]
    y_max_char = char_box[3]
    x_min_u = arrow_up_box[0]
    x_max_u = arrow_up_box[1]
    y_min_u = arrow_up_box[2]
    y_max_u = arrow_up_box[3]
    x_min_d = arrow_down_box[0]
    x_max_d = arrow_down_box[1]
    y_min_d = arrow_down_box[2]
    y_max_d = arrow_down_box[3]
    if arrow_up_flag:
        if (x_min_u < x_max_char and x_max_u > x_min_char and
                y_min_u < y_max_char and y_max_u > y_min_char):
            print("You earned Up Arrow, now the character will speed up.")
            step*=1.5
            arrow_up_flag=False
    if arrow_down_flag:
        if (x_min_d < x_max_char and x_max_d > x_min_char and
                y_min_d < y_max_char and y_max_d > y_min_char):
            print("You earned Down Arrow, now the car will slow down.")
            speed *= 0.5
            arrow_down_flag = False
def char_gets_black_hole():
    global black_hole ,char_box,cat,cat_x,cat_y,m_x,m_y
    x1,y1=black_hole[0]
    x2,y2=black_hole[1]
    x_min_char = char_box[0]
    x_max_char = char_box[1]
    y_min_char = char_box[2]
    y_max_char = char_box[3]
    if (x1-10 < x_max_char and x1+10 > x_min_char and
            y1-10 < y_max_char and y1+10 > y_min_char):
        print("Character will go through the black hole")
        if cat:
            cat_x=x2
            cat_y=y2
        else:
            m_x = x2
            m_y = y2
        black_hole=[0]


def animate():
    glutPostRedisplay()
    global r_car_x,r_car_y,speed,l_car_y,l_car_x,lives,game_over,cat_x,cat_y,m_x, m_y,l_car_box,cat,black_hole,speed,level,\
        right_bus_x,right_bus_y,right_bus_box,gray_heart,pause,game_over,char_box
    if pause == False and game_over == False and start:
        if r_car_x<-400:
            r_car_x=250
            for i in r_car_box:
                i[0]=370
                i[1]=i[0]-123
        else:
            for i in r_car_box:
                i[0]-=speed
                i[1]-=speed
            r_car_x-=speed
        if l_car_x>400:
            l_car_x=-250
            for i in l_car_box:
                i[0]=-370
                i[1]=i[0]+123
        else:
            for i in l_car_box:
                i[0]+=speed
                i[1]+=speed
            l_car_x+=speed
        if right_bus_x < -400:
            right_bus_x = 250
            for i in right_bus_box:
                i[0] = 370
                i[1] = i[0] - 123
        else:
            for i in right_bus_box:
                i[0] -= speed
                i[1] -= speed
            right_bus_x -= speed
        if char_box!=[]:
            if check_collision():
                if lives==0:
                    game_over = True
                    print("game over")
                    #glutLeaveMainLoop()
                else:
                    if cat:
                        if gray_heart:
                            gray_heart = False
                            lives -= 1
                        else:
                            gray_heart=True
                    else:
                        lives -= 1
                    cat_x, cat_y = 0, -250
                    m_x, m_y = 0, -250
        if black_hole!=[0] and black_hole!=[] and level==3:
            char_gets_black_hole()
        update_coins()
        if random.random() < 0.02:  # Randomly attempt to generate a new coin
            generate_coin()
    glutPostRedisplay()


# Main program
glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

# Create window
wind = glutCreateWindow(b"Project")
init()
glutIdleFunc(animate)
# Register callbacks
glutDisplayFunc(showScreen)
glutDisplayFunc(showScreen)
# Start the main loop
glutMouseFunc(mouseListener)
glutKeyboardFunc(keyboard)
glutMainLoop()

