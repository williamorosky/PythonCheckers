from Tkinter import *

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
        for x in range(0,8,2):
            for y in range(0,8,2):
                whiteSquares1 = canvas.create_rectangle(40+(x*50), 30+(y*50), 90+(x*50), 80+(y*50), outline="white", fill="white", tags="white")
                graySquares1 = canvas.create_rectangle(40+(x*50), 30+((y+1)*50), 90+(x*50), 80+((y+1)*50), outline="white", fill="gray", tags="gray")

        for x in range(1,9,2):
            for y in range(1,9,2):
                whiteSquares2 = canvas.create_rectangle(40+(x*50), 30+(y*50), 90+(x*50), 80+(y*50), outline="white", fill="white", tags="white")        
                graySquares2 = canvas.create_rectangle(40+(x*50), 30+((y-1)*50), 90+(x*50), 80+((y-1)*50), outline="white", fill="gray", tags="gray")        
        canvas.pack(fill=BOTH, expand=1)

    def setupGamePieces(self, canvas):
        self.pack(fill=BOTH, expand=1)

        #BLACK PIECES
        for x in range(0,8,2):
            for y in range(0,8,2):
                if y<2:
                    re1 = canvas.create_oval(50+(x*50), 40+((y+1)*50), 80+(x*50), 70+((y+1)*50), outline="black", fill="black", tags="black")

        for x in range(1,9,2):
            for y in range(1,9,2):
                if y<4:
                    re2 = canvas.create_oval(50+(x*50), 40+((y-1)*50), 80+(x*50), 70+((y-1)*50), outline="black", fill="black", tags="black")        
        
        #RED PIECES
        for x in range(0,8,2):
            for y in range(0,8,2):
                if y>3:
                    re1 = canvas.create_oval(50+(x*50), 40+((y+1)*50), 80+(x*50), 70+((y+1)*50), outline="red", fill="red", tags="red")

        for x in range(1,9,2):
            for y in range(1,9,2):
                if y>5:
                    re2 = canvas.create_oval(50+(x*50), 40+((y-1)*50), 80+(x*50), 70+((y-1)*50), outline="red", fill="red", tags="red")        


        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    root.minsize(width=500, height=500)
    root.maxsize(width=500, height=500)
    root.resizable(width=False, height=False)
    checkerboard = CheckerBoard(root)
    root.mainloop()

if __name__ == '__main__':
    main()