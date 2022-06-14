# Arthur Lin Spring 2022
class Board:
    def __init__(self):
        self.board = {}
        self.empty()
    def empty(self):
        for col in 'abcdefgh':
            for row in '12345678':
                self.board[col+row] = ' '
    def set(self, pos, piece):   # pos is a square label (a1, a2, ..., h8)
        if pos in self.board.keys():
            self.board[pos] = piece
    def draw(self):
        print("   a   b   c   d   e   f   g   h   ")
        print(" +---+---+---+---+---+---+---+---+ ")
        for i in '87654321':
            print(f"{i}| {self.board['a' + i]} | {self.board['b' + i]} | {self.board['c' + i]} | {self.board['d' + i]} | {self.board['e' + i]} | {self.board['f' + i]} | {self.board['g' + i]} | {self.board['h' + i]} |{i}")
            print(" +---+---+---+---+---+---+---+---+ ")
        print("   a   b   c   d   e   f   g   h   ")

class Chess_Piece:
    def __init__(self, board, pos, color='white'):
        self.position = self.get_index(pos)
        self.color = color
        board.set(pos, self.get_name())
    def get_index(self, pos):
        return ('abcdefgh'.index(pos[0]), '12345678'.index(pos[1]))
    def get_name(self):
        pass
    def moves(self, board):
        pass

class King(Chess_Piece):
    def get_name(self):
        return "K"
    def moves(self, board):
        p1 = self.position[0]
        p2 = self.position[1]
        st1 = "abcdefgh"
        st2 = "12345678"
        try:
            if p1 != 0:
                board.set(st1[p1-1] + st2[p2+1],"X")            
                board.set(st1[p1-1] + st2[p2],"X")
                board.set(st1[p1-1] + st2[p2-1],"X")
            if p2 > 0:
                board.set(st1[p1] + st2[p2-1],"X")
                board.set(st1[p1+1] + st2[p2-1],"X")

            board.set(st1[p1] + st2[p2+1],"X")       
            board.set(st1[p1+1] + st2[p2],"X")          
            board.set(st1[p1+1] + st2[p2+1],"X")           
        except IndexError:
            pass

class Rook(Chess_Piece):
    def get_name(self):
        return "R"
    def moves(self, board):
        p1 = self.position[0]
        p2 = self.position[1]
        st1 = "abcdefgh"
        st2 = "12345678"
        for i in range(p1+1,8):
            board.set(st1[i]+st2[p2],"X")
        for i in range(p1-1,-1,-1):
            board.set(st1[i]+st2[p2],"X")
        for i in range(p2+1,8):
            board.set(st1[p1]+st2[i],"X")
        for i in range(p2-1,-1,-1):
            board.set(st1[p1]+st2[i],"X")        
            
class Bishop(Chess_Piece):
    def get_name(self):
        return "B"
    def moves(self, board):
        p1 = self.position[0]
        p2 = self.position[1]
        st1 = "abcdefgh"
        st2 = "12345678"
        try:
            for i in range(1,4):
                if p1+i < 8:
                    board.set(st1[p1+i] + st2[p2+i],"X")
                if p1-i > 0 and p2-i >= 0:   
                    board.set(st1[p1-i] + st2[p2-i],"X")
                if p1+i < 8 and p2-i >= 0:
                    board.set(st1[p1+i] + st2[p2-i],"X")
                if p1-i > 0 and p2+i < 8:
                    board.set(st1[p1-i] + st2[p2+i],"X")

            for i in range(4,8):
                if p1+i < 8:
                    board.set(st1[p1+i] + st2[p2+i],"X")
                if p1-i >= 0 and p2-i >= 0:   
                    board.set(st1[p1-i] + st2[p2-i],"X")
                if p1+i < 8 and p2-i >= 0:
                    board.set(st1[p1+i] + st2[p2-i],"X")
                if p1-i >= 0 and p2+i < 8:
                    board.set(st1[p1-i] + st2[p2+i],"X")
        except IndexError:
            pass        

class Knight(Chess_Piece):
    def get_name(self):
        return "N"
    def moves(self, board):
        p1 = self.position[0]
        p2 = self.position[1]
        st1 = "abcdefgh"
        st2 = "12345678"
        try:
            if p1 < 6 and p2 < 7:
                board.set(st1[p1+2] + st2[p2+1],"X")  
            if p1 < 7 and p2 < 6:          
                board.set(st1[p1+1] + st2[p2+2],"X")   #TR
        except IndexError:
            pass
        try:
            if p1 > 1 and p2 > 0:
                board.set(st1[p1-2] + st2[p2-1],"X") #BL
            if p1 > 0 and p2 > 1:
                board.set(st1[p1-1] + st2[p2-2],"X") 
        except IndexError:
            pass
        try:
            if p1 > 1 and p2 < 7:
                board.set(st1[p1-2] + st2[p2+1],"X") #TL
            if p1 > 0 and p2 < 6:
                board.set(st1[p1-1] + st2[p2+2],"X")
        except IndexError:
            pass
        try: 
            if p1 < 6 and p2 > 0:
                board.set(st1[p1+2] + st2[p2-1],"X")
            if p1 < 7 and p2 > 1:
                board.set(st1[p1+1] + st2[p2-2],"X") #BR
        except IndexError:
            pass

class Queen(Chess_Piece):
    def get_name(self):
        return "Q"
    def moves(self, board):
        p1 = self.position[0]
        p2 = self.position[1]
        st1 = "abcdefgh"
        st2 = "12345678"
        try:
            for i in range(1,4):
                if p1+i < 8:
                    board.set(st1[p1+i] + st2[p2+i],"X")
                if p1-i > 0 and p2-i >= 0:   
                    board.set(st1[p1-i] + st2[p2-i],"X")
                if p1+i < 8 and p2-i >= 0:
                    board.set(st1[p1+i] + st2[p2-i],"X")
                if p1-i > 0 and p2+i < 8:
                    board.set(st1[p1-i] + st2[p2+i],"X")

            for i in range(4,8):
                if p1+i < 8:
                    board.set(st1[p1+i] + st2[p2+i],"X")
                if p1-i >= 0 and p2-i >= 0:   
                    board.set(st1[p1-i] + st2[p2-i],"X")
                if p1+i < 8 and p2-i >= 0:
                    board.set(st1[p1+i] + st2[p2-i],"X")
                if p1-i >= 0 and p2+i < 8:
                    board.set(st1[p1-i] + st2[p2+i],"X")
        except IndexError:
            pass
        for i in range(p1+1,8):
            board.set(st1[i]+st2[p2],"X")
        for i in range(p1-1,-1,-1):
            board.set(st1[i]+st2[p2],"X")
        for i in range(p2+1,8):
            board.set(st1[p1]+st2[i],"X")
        for i in range(p2-1,-1,-1):
            board.set(st1[p1]+st2[i],"X")

class Pawn(Chess_Piece):    
    def get_name(self):
        return "P"
    def moves(self, board):
        p1 = self.position[0]
        p2 = self.position[1]
        st1 = "abcdefgh"
        st2 = "12345678"        
        if self.color == "white":
            if st2[p2] == "2":
                board.set(st1[p1] + st2[p2 + 1],"X")
                board.set(st1[p1] + st2[p2 + 2],"X")     
            elif st2[p2] != "8":
                board.set(st1[p1] + st2[p2 + 1],"X")                           
        if self.color == "black":
            if st2[p2] == "7":
                board.set(st1[p1] + st2[p2 - 1],"X")
                board.set(st1[p1] + st2[p2 - 2],"X")     
            elif st2[p2] != "1":
                board.set(st1[p1] + st2[p2 - 1],"X")       
    

b = Board()
b.draw()
while True:
    move = input("Enter a chess piece and its position or type X to exit: ").lower()
    if move == "x":
        print("Goodbye")
        break
    if move[0] == "k":
        k = King(b,move[1]+move[2])
        k.moves(b)
        b.draw()
        b.empty()
    elif move[0] == "r":
        r = Rook(b,move[1]+move[2])
        r.moves(b)
        b.draw()
        b.empty()
    elif move[0] == "b":
        bi = Bishop(b,move[1]+move[2])
        bi.moves(b)
        b.draw()
        b.empty()
    elif move[0] == "p":
        while True:
            color = input("black or white pawn?").lower()
            if color == "white" or color == "black":
                break
            else:
                print("Try again.")
        p = Pawn(b,move[1]+move[2],color)
        p.moves(b)
        b.draw()
        b.empty()
    elif move[0] == "n":
        n = Knight(b,move[1]+move[2])
        n.moves(b)
        b.draw()
        b.empty()
    elif move[0] == "q":
        q = Queen(b,move[1]+move[2])
        q.moves(b)
        b.draw()
        b.empty()
    else:
        print("Try again.")
