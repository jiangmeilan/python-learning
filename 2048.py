# -*- coding -*- UTF-8
#2048
import random
class Matrix:
    def __init__(self, width = 4, height = 4):
        self.width = width
        self.height = height
        self.status = [[0] * width for i in range(height)]

    def prepare(self, k):
        location = random.sample(range(self.width * self.height), k)
        for loc in location:
            row = loc / self.width
            col = loc % self.width
            self.status[row][col] = 2

    def next(self):
        available = []
        for r in range(self.height):
            for c in range(self.width):
                if self.status[r][c] == 0:
                    available.append((r, c))
        loc = random.sample(available, 1)[0]
        self.status[loc[0]][loc[1]] = 2
 
class Action:
    def __init__(self):
        pass
    def move(self, event, matrix):
        if event == 259:
            self.move_up(matrix)
        elif event == 258:
            self.move_down(matrix)
        elif event == 260:
            self.move_left(matrix)
        elif event == 261:
            self.move_right(matrix)

    def move_left(self, matrix):
        status = matrix.status
        for line in status:
            items = filter(lambda x: x != 0, line)
            for i in range(len(line)):
                line[i] = items[i] if i < len(items) else 0
            for i in range(1,len(line)):
                if line[i] == line[i - 1]:
                    line[i - 1] += line[i]
                    line[i] = 0
                    break

            items = filter(lambda x: x != 0, line)
            for i in range(len(line)):
                line[i] = items[i] if i < len(items) else 0

    def move_right(self, matrix): 
        status = matrix.status
        for line in status:
            items = filter(lambda x: x != 0, line)
            for i in range(1, len(line) + 1):
                line[-i] = items[-i] if i < len(items) + 1 else 0
            for i in range(len(line) -1):
                if line[i] == line[i + 1]:
                    line[i + 1] += line[i]
                    line[i] = 0
                    break
            items = filter(lambda x:x != 0, line)
            for i in range(1, len(line) + 1):
                line[-i] = items[-i] if i < len(items) + 1 else 0

    def move_up(self, matrix):
        status = matrix.status
        for c in range(matrix.width):
            items = []
            for r in range(matrix.height):
                if status[r][c] != 0:
                    items.append(status[r][c])
            for r in range(matrix.height):
                status[r][c] = items[r] if r < len(items) else 0
            for r in range(1, matrix.height):
                if status[r][c] == status[r - 1][c]:
                    status[r -1][c] += status[r][c]
                    status[r][c] = 0
                    break
            items = []
            for r in range(matrix.height):
                if status[r][c] != 0:
                    items.append(status[r][c])
            for r in range(matrix.height):
                status[r][c] = items[r] if r < len(items) else 0

    def move_down(self, matrix):
        status = matrix.status
        for c in range(matrix.width):
            items = []
            for r in range(matrix.height):
                if status[r][c] != 0:
                    items.append(status[r][c])
            for r in range(1, matrix.height + 1):
                status[-r][c] = items[-r] if r < len(items) + 1 else 0
            for r in range(matrix.height - 1):
                if status[r][c] == status[r + 1][c]:
                    status[r + 1][c] += status[r][c]
                    status[r][c] = 0
                    break
            items = []
            for r in range(matrix.height):
                if status[r][c] != 0:
                    items.append(status[r][c])
            for r in range(1, matrix.height + 1):
                status[-r][c] = items[-r] if r < len(items) + 1 else 0

if __name__ == '__main__':
    import curses
    class Render:
        def __init__(self):
            pass

        def show(self, screen, matrix):
            screen.clear()
            status = matrix.status
            for line in status:
                screen.addstr(' '.join('%4d' % x for x in line))
                screen.addstr('\n')

    def main(stdscr):
        curses.use_default_colors()
        
        matrix = Matrix()
        action = Action()
        render = Render()
        matrix.prepare(2)
        render.show(stdscr, matrix)

        while True:
            key = stdscr.getch()
            if key == ord('q'):break
            action.move(key, matrix)
            matrix.next()
            render.show(stdscr, matrix)
    curses.wrapper(main)


