from Tkinter import *

gameBoardMatrix =  [[ 0, 1, 0, 1, 0, 1, 0, 1],
                    [ 1, 0, 1, 0, 1, 0, 1, 0],
                    [ 0, 1, 0, 1, 0, 1, 0, 1],
                    [ 1, 0, 1, 0, 1, 0, 1, 0],
                    [ 0, 1, 0, 1, 0, 1, 0, 1],
                    [ 1, 0, 1, 0, 1, 0, 1, 0],
                    [ 0, 1, 0, 1, 0, 1, 0, 1],
                    [ 1, 0, 1, 0, 1, 0, 1, 0]]

gameBoardIdMatrix = [[ 0, 1, 0, 1, 0, 1, 0, 1],
                    [ 1, 0, 1, 0, 1, 0, 1, 0],
                    [ 0, 1, 0, 1, 0, 1, 0, 1],
                    [ 1, 0, 1, 0, 1, 0, 1, 0],
                    [ 0, 1, 0, 1, 0, 1, 0, 1],
                    [ 1, 0, 1, 0, 1, 0, 1, 0],
                    [ 0, 1, 0, 1, 0, 1, 0, 1],
                    [ 1, 0, 1, 0, 1, 0, 1, 0]]

gamePieceMatrix =  [[ 0, 1, 0, 1, 0, 1, 0, 1],
                    [ 1, 0, 1, 0, 1, 0, 1, 0],
                    [ 0, 1, 0, 1, 0, 1, 0, 1],
                    [ 0, 0, 0, 0, 0, 0, 0, 0],
                    [ 0, 0, 0, 0, 0, 0, 0, 0],
                    [ 2, 0, 2, 0, 2, 0, 2, 0],
                    [ 0, 2, 0, 2, 0, 2, 0, 2],
                    [ 2, 0, 2, 0, 2, 0, 2, 0]]

gameIdMatrix =     [[ 0, 1, 0, 1, 0, 1, 0, 1],
                    [ 1, 0, 1, 0, 1, 0, 1, 0],
                    [ 0, 1, 0, 1, 0, 1, 0, 1],
                    [ 0, 0, 0, 0, 0, 0, 0, 0],
                    [ 0, 0, 0, 0, 0, 0, 0, 0],
                    [ 2, 0, 2, 0, 2, 0, 2, 0],
                    [ 0, 2, 0, 2, 0, 2, 0, 2],
                    [ 2, 0, 2, 0, 2, 0, 2, 0]]
isRedTurn = bool(1)

class CheckerBoard(Frame):

    def __init__(self, parent):

        Frame.__init__(self,parent)

        self.parent = parent
        self.setupGame()

    def setupGame(self):
        self.parent.title("Python Checkers")
        canvas = Canvas(self,bg="CadetBlue1")
        self.setupBoard(canvas)
        self.setupGamePieces(canvas)

    def setupBoard(self, canvas):
        self.pack(fill=BOTH, expand=1)
        for (y,row) in enumerate(gameBoardMatrix):
            for (x,value) in enumerate(row):
                if value == 1:
                    graySquare = canvas.create_rectangle(40+(x*50), 30+((y)*50), 90+(x*50), 80+((y)*50), outline="gray", fill="gray", tags="gray")
                    gameBoardIdMatrix[y][x] = graySquare
                elif value == 0:
                    whiteSquare = canvas.create_rectangle(40+(x*50), 30+((y)*50), 90+(x*50), 80+((y)*50), outline="white", fill="white", tags="white")
                    gameBoardIdMatrix[y][x] = whiteSquare

        canvas.pack(fill=BOTH, expand=1)

    def setupGamePieces(self, canvas):
        self.pack(fill=BOTH, expand=1)
        for (y,row) in enumerate(gamePieceMatrix):
            for (x,value) in enumerate(row):
                if value == 1:
                    blackChecker = canvas.create_oval(50+(x*50), 40+((y)*50), 80+(x*50), 70+((y)*50), outline="black", fill="black", tags="black")
                    gameIdMatrix[y][x] = blackChecker
                    canvas.tag_bind(blackChecker, "<ButtonPress-1>", lambda event, canvas=canvas:self.clickPiece(event, canvas)) 
                elif value == 2:
                    redChecker = canvas.create_oval(50+(x*50), 40+((y)*50), 80+(x*50), 70+((y)*50), outline="red", fill="red", tags="red")
                    gameIdMatrix[y][x] = redChecker
                    canvas.tag_bind(redChecker, "<ButtonPress-1>", lambda event, canvas=canvas:self.clickPiece(event, canvas)) 

    def clickPiece(self, event, canvas):
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        idValue = canvas.find_closest(x, y)[0]
        for (y,row) in enumerate(gameIdMatrix):
            for (x,value) in enumerate(row):
                if value == idValue:
                    self.showValidMoves(y, x, canvas)

    def showValidMoves(self, row, column, canvas):

        if not isRedTurn and gamePieceMatrix[row][column] == 1 :
            if gamePieceMatrix[row+1][column-1] == 0:
                print("Valid Left")                
                canvas.itemconfig((((row+1)*8)+column), outline="blue")
                canvas.tag_bind((((row+1)*8)+column), "<ButtonPress-1>", lambda event, row=row, column=column, canvas=canvas:self.executeMove(event, row, column, canvas))
            if gamePieceMatrix[row+1][column+1] == 0:
                print("Valid Right")
                canvas.itemconfig((((row+1)*8)+column+2), outline="blue")
                canvas.tag_bind((((row+1)*8)+column+2), "<ButtonPress-1>", lambda event, row=row, column=column, canvas=canvas:self.executeMove(event, row, column, canvas))
        elif isRedTurn and gamePieceMatrix[row][column] == 2 :
            if gamePieceMatrix[row-1][column-1] == 0:
                print("Valid Right")
                canvas.itemconfig((((row-1)*8)+column), outline="blue")
                canvas.tag_bind((((row-1)*8)+column), "<ButtonPress-1>", lambda event, row=row, column=column, canvas=canvas:self.executeMove(event, row, column, canvas))
            if gamePieceMatrix[row-1][column+1] == 0:
                print("Valid Left")
                canvas.itemconfig((((row-1)*8)+column+2), outline="blue")
                canvas.tag_bind((((row-1)*8)+column+2), "<ButtonPress-1>", lambda event, row=row, column=column, canvas=canvas:self.executeMove(event, row, column, canvas))

    def executeMove(self, event, row, column, canvas):
        print "Move"
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        newRow = 0
        newColumn = 0
        oldRow = row
        oldColumn = column
        newPosition = canvas.find_closest(x, y)[0]
        for (y,row) in enumerate(gameBoardMatrix):
            for (x,value) in enumerate(row):
                if value == newPosition:
                    newRow = y
                    newColumn = x

        gamePieceMatrix[newRow][newColumn] = gamePieceMatrix[oldRow][oldColumn]
        gamePieceMatrix[oldRow][oldColumn] = 0
        gameIdMatrix[newRow][newColumn] = gameIdMatrix[oldRow][oldColumn]
        gameIdMatrix[oldRow][oldColumn] = 0

        canvas.itemconfig((((oldRow+1)*8)+oldColumn+2), outline="gray")
        canvas.itemconfig((((oldRow+1)*8)+oldColumn), outline="gray")
        canvas.itemconfig((((oldRow-1)*8)+oldColumn+2), outline="gray")
        canvas.itemconfig((((oldRow-1)*8)+oldColumn), outline="gray")
        global isRedTurn
        isRedTurn = not isRedTurn
                        

def main():
    root = Tk()
    root.minsize(width=500, height=500)
    root.maxsize(width=500, height=500)
    root.resizable(width=False, height=False)
    checkerboard = CheckerBoard(root)
    root.mainloop()
    

if __name__ == '__main__':
    main()
