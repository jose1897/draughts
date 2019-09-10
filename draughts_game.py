import colorama
from colorama import Fore, Back, Style
import os

colorama.init()

class Player:
    
    def __init__(self,name,p_color,num):
        self.name = name
        self.p_color = p_color
        self.num = num
    
    def get_name_player(self):
        return self.name


class Piece:
    
    def __init__(self,player):
        self.player = player
    
    def get_piece_color(self):
        return self.player.p_color
    
    def get_player_num(self):
        return self.player.num




class Square:
    
    def __init__(self,color,piece = None):
        self.color = color
        self.piece = piece

    def assign_piece(self,piece):
        self.piece = piece

    def deallocate_piece(self):
        self.piece =  None
    
    def is_piece_inside(self):
        return self.piece != None

    def piece_color(self):
        return self.piece.get_piece_color()
    
    def get_piece_player_num(self):
        return self.piece.get_player_num()

    def get_piece(self):
        return self.piece


class Board:

    def __init__(self,size_m = 8):
        self.matrix = []
        self.size_m = size_m

    def generate_squares(self,player1,player2):
        i = True
        for y in range(0,self.size_m):
            aux = []
            for x in range(0,self.size_m):
                if y < (self.size_m/2) -1 or y >= (self.size_m/2) + 1:                        
                    if i:
                        aux.append(Square(Fore.WHITE))
                        i = False
                    else:
                        if y > self.size_m/2:
                            aux.append(Square(Fore.RED,Piece(player1)))
                        else:
                            aux.append(Square(Fore.RED,Piece(player2)))
                        i = True
                else:
                    if i:
                        aux.append(Square(Fore.WHITE))
                        i = False
                    else:
                        aux.append(Square(Fore.RED))   
                        i = True                    
            if i:
                i = False
            else:
                i = True
            self.matrix.append(aux)

    def draw_matrix(self):
        clear = lambda: os.system('cls')
        clear()
        draw_b = ''
        reset = Style.RESET_ALL
        con = 0
        for a in range(1,self.size_m+1):
            draw_b += str(a) + ' '
        draw_b += '\n'
        for row in self.matrix:
            for col in row:
                if col.is_piece_inside():
                    draw_b += col.piece_color() + '© ' + reset
                else:
                    draw_b += col.color + '■ '+ reset
            con += 1
            draw_b += '|'+str(con) +'\n'
        print(draw_b)

    def move_piece(self,from_x,from_y,to_x,to_y):

        if from_y == to_y or from_x == to_x or from_x <0 or from_x >= self.size_m or from_y <0 or from_y >= self.size_m or to_x <0 or to_x >= self.size_m or to_y <0 or to_y >= self.size_m:
            self.draw_matrix()
            print('Wrong coordinates')
            return
        if self.matrix[from_y][from_x].is_piece_inside():
            if self.matrix[to_y][to_x].is_piece_inside():
                self.draw_matrix()
                print('Wrong coordinates')
            else:
                self.matrix[to_y][to_x].assign_piece(self.matrix[from_y][from_x].piece)
                self.matrix[from_y][from_x].deallocate_piece()
                self.draw_matrix()
        else:
            self.draw_matrix()
            print('Wrong coordinates')

    def get_matrix(self):
        return self.matrix


player1 = Player('Jose',Fore.GREEN,1)
player2 = Player('Carlos',Fore.YELLOW,2)

board = Board(10)
board.generate_squares(player1,player2)
board.draw_matrix()
while True:
    print('Enter the coordinates (x, y) of the tab to move')
    from_x = int(input()) - 1
    from_y = int(input()) - 1
    print('Enter the coordinates (x, y) of where to move')
    to_x = int(input()) - 1
    to_y = int(input()) - 1
    board.move_piece(from_x,from_y,to_x,to_y)






# Set the color semi-permanentlys
# red = Fore.RED
# yellow = Fore.YELLOW
# cyan = Fore.CYAN
# reset = Style.RESET_ALL

# mensaje = red + "klk" + reset + yellow + " hola "+ reset
# print(mensaje)