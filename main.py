import pygame, random, numpy as np; pygame.init()


BAR_WIDTH = 15
SPACE = 10
TOTAL_SPACE = BAR_WIDTH + SPACE
font = pygame.font.SysFont("arial", 12)




def random_graph_heights(count: int, std_deviation: int, height: int) -> list:
    random_heights = []
    while True:
        random_height = np.random.normal(height, std_deviation, count)

        for i, val in enumerate(random_height):
            if val > 0:
                random_heights.append(int(round(val)))
                

        if len(random_heights) == count:
            return random_heights
        elif len(random_heights) > count:
            for i in range(len(random_heights) - count):
                random_heights.pop(i)
            return random_heights
        
    
def draw_board(random_graph_heights: list, display, display_width, display_height, current_bars: list, finished_bars: list) -> None:
    display.fill((255, 255, 255))


    # draw outline

    pygame.draw.rect(display, (0, 0, 0), ((display_width - len(random_graph_heights) * TOTAL_SPACE) // 2, 45, len(random_graph_heights) * TOTAL_SPACE, display_height - 145), 3)


    #draw bars

    for i, height in enumerate(random_graph_heights):
        if i in finished_bars:
            pygame.draw.rect(display, (0, 255, 0), ((display_width - len(random_graph_heights) * TOTAL_SPACE) // 2 + 5 + i * TOTAL_SPACE, display_height - 100 - height * 5, BAR_WIDTH, height * 5))

        elif i in current_bars:
            pygame.draw.rect(display, (255, 0, 0), ((display_width - len(random_graph_heights) * TOTAL_SPACE) // 2 + 5 + i * TOTAL_SPACE, display_height - 100 - height * 5, BAR_WIDTH, height * 5))
        else:
            pygame.draw.rect(display, (0, 0, 255), ((display_width - len(random_graph_heights) * TOTAL_SPACE) // 2 + 5 + i * TOTAL_SPACE, display_height - 100 - height * 5, BAR_WIDTH, height * 5))

        height_text = font.render(str(height), True, (0, 0, 0))
        display.blit(height_text, ((display_width - len(random_graph_heights) * TOTAL_SPACE) // 2 + i * TOTAL_SPACE + (15 - height_text.get_width() // 2), 45 + display_height - 145 + 10))
    pygame.display.update()
    


    

def bubble_sort(graph_point: list, display, display_width: int, display_height: int):
    graph = graph_point.copy()
    finished_bars = []
    count = 0
    switch = True
    while switch:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 quit()
        switch = False
        for i in range(len(graph) - 1):
            if graph[i] > graph[i + 1]:
                pre_graph = graph[i]
                graph[i] = graph[i + 1]
                graph[i + 1] = pre_graph
                draw_board(graph, display, display_width, display_height, [i + 1], finished_bars)
                pygame.time.delay(30)
                switch = True
        finished_bars.append(len(graph_point) - 1 - count)
        count += 1
    draw_board(graph, display, display_width, display_height, [], range(0, len(graph_point)))



def selection_sort(graph_point: list, display, display_width: int, display_height: int):
    graph = graph_point.copy()

    lowest_height = 100000000
    finished_bars = []
    #get the highest bar on the graph
    highest_height = -1
    for i, height in enumerate(graph_point):
        if highest_height < height:
            highest_height = height
            highest_index = i

    for run_count in range(len(graph_point)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit();
        
        for i in range(run_count, len(graph_point)):
            if graph[i] < lowest_height:
                lowest_height = graph[i]
                low_height_index = i
            draw_board(graph, display, display_width, display_height, [i, lowest_height], finished_bars)
            pygame.time.delay(30)
        

        graph.insert(run_count, lowest_height)
        graph.pop(low_height_index + 1)
        lowest_height = highest_height
        low_height_index = highest_index
        finished_bars.append(run_count)
    draw_board(graph, display, display_width, display_height, [], range(len(graph_point)))





def merge_sort(graph_point: list, display, display_width: int, display_height: int):

    pass        

        






if __name__ == "__main__":
    display_width, display_height = 1700, 1000
    display = pygame.display.set_mode((display_width, display_height))
    selection_sort(random_graph_heights(65, 30, 80), display, display_width, display_height)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True





