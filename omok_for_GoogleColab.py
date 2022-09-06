rows_keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
Board = [''.join(['┼' for j in range(19)]) for i in range(19)]
line_num = '    1 2 3 4 5 6 7 8 9 10111213141516171819'

Order = {True: '\n흑돌 차례입니다 : ', False: '\n백돌 차례입니다 : '}
Color = {True: '●', False: '○'}
Finmsg = {True: '\n흑돌 승리!', False: '\n백돌 승리!'}

Black = True

class SearchAround(list):
    
    def get_around(self, y, x):
        '''지정한 인덱스의 배열상 한 칸 주변에 있는 요소의 인덱스들을 반환'''
        
        l = len(self)
        col = [i for i in range(x-1, x+2) if i >= 0 and i < l]
        row = [i for i in range(y-1, y+2) if i >= 0 and i < l]
        return [[j, i] for j in row for i in col]
        
        
    def get_branch(self, y, x, n):
        '''주변 8방향으로 n길이 만큼 뻗어나갈 수 있으면 뻗어나가면서 만나는 요소를 뱡향별로 반환하는 함수'''
        
        l = len(self)
        temp = []
        for row, col in self.get_around(y, x):
            if col == x and row == y:
                continue
            else:
                _x = x + (col-x) * (n-1)
                _y = y + (row-y) * (n-1)
                if _x >= 0 and _x < l and _y >= 0 and _y < l:
                    temp.append([self[y+(row-y)*i][x+(col-x)*i] for i in range(n)])
        return temp
    
    def get_line(self, y, x):
        '''지정한 위치의 8방향 라인을 묶어서 리스트로 반환'''
        
        l = len(self)
        row_min = y - min(x, y)
        col_min = y - min((l-1)-x, y)
        
        yx_range = l - abs(y - x)
        xy_range = abs(y - x) + 1
        
        sub_row = x - (y - row_min)
        sub_col = x + (y - col_min)
        
        row = list(self[y])
        col = [i[x] for i in self]
        yx = [self[row_min+i][sub_row+i] for i in range(yx_range)]
        xy = [self[col_min+i][sub_col-i] for i in range(xy_range)]
        
        return [row, col, yx, xy]

def show_board():
    print()
    print(line_num)
    for i, w in enumerate(rows_keys):
        print(w, ':', Board[i])

show_board()


def refBoard(row, col, color):
    row = rows_keys.index(row)
    if col <= 0 or col > 19:
        raise
    col -= 1
    line = list(Board[row])
    
    if line[col] == '┼':
        line[col] = Color[color]
        Board[row] = ''.join(line)
        show_board()
        if check_win(row, col, color):
            print(Finmsg[color])
        else:
            global Black
            Black = not color
            main()
    else:
        print("이미 돌이 놓여져있습니다.")
        main()

def check_win(row, col, color):
    arr = SearchAround(Board)
    temp = arr.get_line(row, col)
    color = Color[color]*5
    for i in temp:
        if ''.join(i).find(color) >= 0 :
            return True
    
    return False


def main():
    try:
        global Black
        point = input(Order[Black])
        if point == '':
            return
        row, col = point[0], int(point[1:])
        refBoard(row, col, Black)
    except:
        print("잘못된 입력입니다.")
        main()
        

main()