import pygame
import random
pygame.init()
pygame.font.init()

# Define some colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (120, 120, 120)
LIGHT_GREY = (170, 170, 170)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 255)
GREEN = (0, 255, 0)

# Define the fonts used
INSTRUCTIONS_FONT = pygame.font.SysFont('comicsans', 20)
INFORMATION_FONT = pygame.font.SysFont('comicsans', 18)

# Define the dimensions of the window and the padding
APP_WIDTH, APP_HEIGHT = 1000, 600
X_PADDING, Y_PADDING = 100, 200

# Define the width and height of the buttons
BUTTON_WIDTH = 60
BUTTON_HEIGHT = 40

# This is a large number that is used in various instances throughout the program, such as when we want to draw redraw the window
# without redrawing drawing any rectangles red or blue, we pass in this large number
LARGE_NUMBER = 100000

# Define the window of pygame
WIN = pygame.display.set_mode((APP_WIDTH, APP_HEIGHT))
pygame.display.set_caption('Sorting Algorithms Visualisation')
FPS = 60 # the frame rate

# This declares the initial number of elements and the speed (delay) of the sorting
INITIAL_NUM_ELEMENTS = 10
STARTING_DELAY = 150

# the delay is set to the starting delay at first (not necessary but for coherence)
big_delay = STARTING_DELAY
num_elements = INITIAL_NUM_ELEMENTS

# The initial number of comparisons and swaps to display
comparisons = 0
swaps = 0

# Function that creates a new unsorted data set
def create_dataset(min:int, max:int, length:int) -> list:
    unsorted = random.sample(range(min, max), length) # produces a list of 10 random integers varying from 0 to 10
    return unsorted

# The beginning data set. The range of value in the elements is from 0 to the number of elements to avoid errors thrown by Python
unsorted = create_dataset(0, num_elements, num_elements)

# This is the button class, which helps creating the GUI buttons that can be used to vary the speed of the sorting
class Button():
    def __init__(self, color, x, y, width, height, text, delay):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.delay = delay # each button will change the speed of the sorting when clicked

    def draw_button(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 15)
            text = font.render(self.text, 1, BLACK)
            WIN.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, position):
        if position[0] > self.x and position[0] < self.x + self.width:
            if position[1] > self.y and position[1] < self.y + self.height:
                return True
        else:
            return False
    
    def apply_speed_change(self):
        if self.delay < 0:
            return (int)(STARTING_DELAY * self.delay)
        else:
            return (int)(STARTING_DELAY // self.delay)
        
x12_button = Button(LIGHT_GREY, x=20, y=10, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='1/2x', delay=0.5)
x2_button = Button(LIGHT_GREY, x=20, y=10+BUTTON_HEIGHT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='2x', delay=2)
x4_button = Button(LIGHT_GREY, x=20, y=10+2*BUTTON_HEIGHT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='4x', delay=4)
x8_button = Button(LIGHT_GREY, x=20, y=10+3*BUTTON_HEIGHT, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text='8x', delay=8)

buttons_list = [x12_button, x2_button, x4_button, x8_button]

# Bubble sort
def bubble_sort(data:list, num_elements:int, comparisons:int, swaps:int, big_delay:int):
    comparisons = 0
    swaps = 0
    size = len(data)
    for i in range(size-1):
        for j in range(size-i-1):
            comparisons += 1
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swaps += 1
                draw_window(data, j, j+1, num_elements, comparisons, swaps)
                pygame.time.delay(big_delay)
    
    draw_window(data, LARGE_NUMBER, LARGE_NUMBER, num_elements, comparisons, swaps)
    completed_sort(data)
    draw_window(data, LARGE_NUMBER, LARGE_NUMBER, num_elements, comparisons, swaps) # Makes sure that at the end of the sort the rectangles are redrawn with the right colors
    return data

# Selection sort
def selection_sort(data:list, num_elements:int, comparisons:int, swaps:int, big_delay:int):
    comparisons = 0
    swaps = 0
    for i in range(len(data)):
        smallest_num = i
        for j in range(i+1, len(data)):
            draw_window(data, j, i, num_elements, comparisons, swaps) # shows iterating through whole array to find smallestt number
            small_delay = big_delay // 5
            pygame.time.delay(small_delay)
            comparisons += 1
            if data[j] < data[smallest_num]: # once the smallest number has been found
                smallest_num = j # remember the index of the smallest number
        if smallest_num != i:
            draw_window(data, smallest_num, i, num_elements, comparisons, swaps) # shows the smallest number has been found
            delay = big_delay // 3
            pygame.time.delay(delay)
            swaps += 1
            data[i], data[smallest_num] = data[smallest_num], data[i]
            draw_window(data, i, smallest_num, num_elements, comparisons, swaps)
            pygame.time.delay(big_delay)
    
    draw_window(data, LARGE_NUMBER, LARGE_NUMBER, num_elements, comparisons, swaps)
    completed_sort(data)
    draw_window(data, LARGE_NUMBER, LARGE_NUMBER, num_elements, comparisons, swaps)
    return data

# Insertion sort
def insertion_sort(data:list, num_elements:int, comparisons:int, swaps:int, big_delay:int):
    comparisons = 0
    swaps = 0
    for i in range(1, len(data)):
        key = data[i] # the current element we are looking at
        j = i - 1 # this means we want to start the i loop from index 1 and select j to be the rectangle before
        comparisons += 1
        while j >= 0 and key < data[j]:
            swaps += 1
            data[j+1] = data[j]
            j -= 1
            draw_window(data, j+1, i, num_elements, comparisons, swaps)
            pygame.time.delay(big_delay)
        data[j + 1] = key
    
    draw_window(data, LARGE_NUMBER, LARGE_NUMBER, num_elements, comparisons, swaps)
    completed_sort(data)
    draw_window(data, LARGE_NUMBER, LARGE_NUMBER, num_elements, comparisons, swaps)
    return data

def completed_sort(data):
    bar_width = (APP_WIDTH - X_PADDING) / len(data)
    bar_height = [i / max(data) for i in data]
    for i in range(len(data)):
        rect = pygame.Rect((int) (bar_width * i + X_PADDING//2),
                           (int) (APP_HEIGHT - (bar_height[i] * (APP_HEIGHT - Y_PADDING))), (int) (bar_width), 1000)
        pygame.draw.rect(WIN, GREEN, rect)
        pygame.time.delay(25)
        pygame.display.update()
    pygame.time.delay(200)
    
def draw_window(data:list, red_rect:int, blue_rect:int, num_elements:int, comparisons:int, swaps:int, 
                x12_button=x12_button, x2_button=x2_button, x4_button=x4_button, x8_button=x8_button):
    
    WIN.fill(WHITE)
    
    x12_button.draw_button(WIN)
    x2_button.draw_button(WIN)
    x4_button.draw_button(WIN)
    x8_button.draw_button(WIN)
    
    instructions_text_1 = INSTRUCTIONS_FONT.render(
        "SPACE - Reset || B - Bubble Sort || I - Insertion Sort || S - Selection Sort", 1, BLACK
        )
    WIN.blit(instructions_text_1, instructions_text_1.get_rect(center = (APP_WIDTH//2, 30)))
    
    instructions_text_2 = INSTRUCTIONS_FONT.render(
        "UP ARROW - Increase Data || DOWN ARROW - Decrease Data", 1, BLACK
    )
    WIN.blit(instructions_text_2, instructions_text_2.get_rect(center = (APP_WIDTH//2, 60)))
        
    num_operations_text = INFORMATION_FONT.render(
        "Number of Elements: " + str(num_elements) + ", Comparisons: " + str(comparisons) + ", Swaps: " + str(swaps), 1, BLACK
        )
    WIN.blit(num_operations_text, num_operations_text.get_rect(center = (APP_WIDTH//2, 110)))
    
    bar_width = (APP_WIDTH - X_PADDING) / len(data)
    bar_height = [i / max(data) for i in data]
    for i in range(len(data)):
        rect = pygame.Rect((int) (bar_width * i + X_PADDING//2),
        (int) (APP_HEIGHT - (bar_height[i] * (APP_HEIGHT - Y_PADDING))), (int) (bar_width), 1000)
            
        if i == red_rect:
            pygame.draw.rect(WIN, RED, rect)
        elif i == blue_rect:
            pygame.draw.rect(WIN, BLUE, rect)
        elif i % 2:
            pygame.draw.rect(WIN, GREY, rect)
        else: 
            pygame.draw.rect(WIN, BLACK, rect)

    pygame.display.update() # updates the changes made to de display

def main(unsorted, big_delay, num_elements, comparisons, swaps):
    
    clock = pygame.time.Clock()
    
    run = True

    draw_window(unsorted, LARGE_NUMBER, LARGE_NUMBER, num_elements, comparisons, swaps)
    
    while run:
        clock.tick(FPS)
                
        for event in pygame.event.get():
            position = pygame.mouse.get_pos() # returns a tuple, (x, y) coordinates of current position of the mouse

            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons_list:
                    if button.isOver(position):
                        big_delay = button.apply_speed_change()
                        
            if event.type == pygame.MOUSEMOTION:
                    for button in buttons_list:
                        if button.isOver(position):
                            button.color = LIGHT_BLUE
                            button.draw_button(WIN) # called to update the color of the button
                            pygame.display.update() # called to update the display
                        else:
                            button.color = LIGHT_GREY
                            button.draw_button(WIN)
                            pygame.display.update()
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    unsorted = create_dataset(0, num_elements, num_elements)
                    comparisons = 0
                    swaps = 0
                    draw_window(unsorted, LARGE_NUMBER, LARGE_NUMBER, num_elements, comparisons, swaps)

                elif event.key == pygame.K_b:
                    bubble_sort(unsorted, num_elements, comparisons, swaps, big_delay)

                elif event.key == pygame.K_i: 
                    insertion_sort(unsorted, num_elements, comparisons, swaps, big_delay)

                elif event.key == pygame.K_s:
                    selection_sort(unsorted, num_elements, comparisons, swaps, big_delay)
                
                elif event.key == pygame.K_UP:
                    num_elements += INITIAL_NUM_ELEMENTS
                    unsorted = create_dataset(0, num_elements, num_elements)
                    comparisons = 0
                    swaps = 0
                    draw_window(unsorted, LARGE_NUMBER, LARGE_NUMBER, num_elements, comparisons, swaps)
                
                elif event.key == pygame.K_DOWN:
                    if (num_elements > INITIAL_NUM_ELEMENTS):
                        num_elements -= INITIAL_NUM_ELEMENTS
                        unsorted = create_dataset(0, num_elements, num_elements)
                        comparisons = 0
                        swaps = 0
                        draw_window(unsorted, LARGE_NUMBER, LARGE_NUMBER, num_elements, comparisons, swaps)

    pygame.quit()
    
if __name__ == '__main__':
    main(unsorted, big_delay, num_elements, comparisons, swaps)