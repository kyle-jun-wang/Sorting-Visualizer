import pygame
import random
import button



pygame.init()
window = pygame.display.set_mode((1200, 600))
window.fill((255,255,255))
pygame.display.set_caption("Sorting Algorithm Visualizer")


teal = (0,255,255)
green = (0, 128, 0)
red = (128, 0, 0)

#values = create_values()
#draw_values(window, values)

Selection_Sort_Button = button.Button(window, "Insertion Sort", 300, 525, 150, 50)
Bubble_Sort_Button = button.Button(window, "Bubble Sort", 450, 525, 150, 50)
Merge_Sort_Button = button.Button(window, "Merge Sort", 600, 525, 150, 50)
Quick_Sort_Button = button.Button(window, "Quick Sort", 750, 525, 150, 50)

load_values = button.Button(window, "PRESS THE SPACE BAR TO LOAD OR RESET VALUES", 0, 20, 700, 50)
start_sort = button.Button(window, "CLICK ON AN ALGORITHM AND PRESS THE ENTER KEY TO START", 600, 20, 700, 50)


def create_values():
    values = [[0, teal] for x in range(50)]
    for x in range(len(values)):
        # NOTE: The range is based on how coordinates are upside down here
        values[x][0] = random.randrange(100, 500)

    return values


# draws the values
def draw_values(win, values):
    pygame.draw.rect(win, (255, 255, 255), (0, 70, 1200, 450))
    for z in range(len(values)):
        pygame.draw.line(win, values[z][1], (100 + (z * 20), 500), (100 + (z * 20), values[z][0]), 10)

    pygame.display.update()




values = create_values()



def selectionsort(window, values):

    for x in range(len(values)):
        min_index = x
        values[min_index][1] = red

        pygame.event.pump()

        for y in range(x+1, len(values)):


            if values[min_index] > values[y]:

                values[y][1] = red

                values[min_index][1] = teal
                draw_values(window, values)
                min_index = y

        values[x], values[min_index] = values[min_index], values[x]

        values[x][1] = green

    draw_values(window, values)

    return values


def bubblesort(window, values):
    for x in range(len(values)):
        for y in range(len(values) - 1):
            pygame.event.pump()

            if values[y][0] > values[y+1][0]:
                values[y], values[y+1] = values[y+1], values[y]

                values[y+1][1] = red

                draw_values(window, values)

            values[y][1] = teal
            values[len(values)-1][1] = teal
            if x == len(values)-1:
                values[y][1] = green
                values[y+1][1] = green
                draw_values(window, values)

    return values






def mergesort(window, values, left, right):

    mid = (left + right) // 2

    if left < right:
        mergesort(window, values, left, mid)
        mergesort(window, values, mid + 1, right)

        merge(window, values, left, mid, mid+1, right)

def merge(window, values, a, b, c, d):

    l = a
    m = c

    temp = []
    pygame.event.pump()

    while l <= b and m <= d:
        values[l][1] = red
        values[m][1] = red
        draw_values(window, values)
        values[l][1] = teal
        values[m][1] = teal

        if values[l] < values[m]:
            temp.append(values[l])
            l += 1
        else:
            temp.append(values[m])
            m += 1

    while l <= b:
        values[l][1] = red
        draw_values(window, values)
        values[l][1] = teal

        temp.append(values[l])

        #draw_values(window, values)
        l += 1

    while m <= d:
        values[m][1] = red
        draw_values(window, values)
        values[m][1] = teal

        temp.append(values[m])

        m += 1

    y = 0
    for x in range(a, d + 1):
        pygame.event.pump()

        values[x] = temp[y]
        values[x][1] = red
        y+=1

        draw_values(window, values)

        # Consider changing the way the color updates so that it's only one side
        if d - a == len(values)-2:
            values[x][1] = green
            draw_values(window, values)
        else:
            values[x][1] = teal

    return values



org = values.copy()
z = 0
def quicksort(win, values, a, b):
    global z
    z += 1
    #print(z)
    if len(values) <= 1:
        return values

    smaller = []
    equal = []
    larger = []

    pivot = values[0][0]
    values[0][1] = red

    pygame.event.pump()

    p = 0
    for x in range(len(values)):
        if values[x][0] < pivot:
            smaller.append(values[x])
            p += 1
        elif values[x][0] > pivot:
            larger.append(values[x])
        else:
            equal.append(values[x])

    values = smaller + equal + larger

    count = 0
    pygame.event.pump()
    for y in range(a, b):
        org[y] = values[count]
        count += 1
        print(b-a)


    draw_values(win, org)
    values[p][1] = teal

    return quicksort(win, smaller, a, (a + len(smaller))) + equal + quicksort(win, larger, (b - len(larger)),  b)



while True:
    for e in pygame.event.get():
        # Resets the visualizer and randomizes the values again
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                values = create_values()

                window.fill((255,255,255))
                Selection_Sort_Button = button.Button(window, "Insertion Sort", 300, 525, 150, 50)
                Bubble_Sort_Button = button.Button(window, "Bubble Sort", 450, 525, 150, 50)
                Merge_Sort_Button = button.Button(window, "Merge Sort", 600, 525, 150, 50)
                Quick_Sort_Button = button.Button(window, "Quick Sort", 750, 525, 150, 50)

                load_values = button.Button(window, "PRESS THE SPACE BAR TO LOAD OR RESET VALUES", 0, 20, 700, 50)
                start_sort = button.Button(window, "CLICK ON AN ALGORITHM AND PRESS THE ENTER KEY TO START", 600, 20, 700, 50)

                draw_values(window, values)


            if e.key == pygame.K_RETURN:

                # IMPLEMENT SORTING

                if Selection_Sort_Button.call:
                    selectionsort(window, values)
                elif Bubble_Sort_Button.call:
                    bubblesort(window, values)
                elif Merge_Sort_Button.call:
                    mergesort(window, values, 0, len(values)-1)
                elif Quick_Sort_Button.call:
                    quicksort(window, values, 0, 50)
                    for p in range(len(org)):
                        org[p][1] = green
                    draw_values(window, org)
                #bubblesort(window, values)

                #mergesort(window, values, 0, len(values)-1)

                #pygame.time.delay(100)

                pygame.display.update()

        if e.type == pygame.QUIT:
            pygame.quit()


    Selection_Sort_Button.mouse_click()
    Bubble_Sort_Button.mouse_click()
    Merge_Sort_Button.mouse_click()
    Quick_Sort_Button.mouse_click()

    pygame.display.update()
