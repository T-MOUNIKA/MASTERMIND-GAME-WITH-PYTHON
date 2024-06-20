from tkinter import *
import random
import tkinter.messagebox
def checkcode():
   global ans, col1, col2, col3, col4, n, correct
   count = 0
   count = (col1.get() == ans[0]) + (col2.get() == ans[1]) + (col3.get() == ans[2]) + (
           col4.get() == ans[3])
   chances = n.get()
   print(col1.get(), ',', col2.get(), ",", col3.get(), ",", col4.get())
   print(count)
   if chances > 0:
       if count == 0:
           correct.set(0)
       elif count == 1:
           correct.set(1)
       elif count == 2:
           correct.set(2)
       elif count == 3:
           correct.set(3)
       elif count == 4:
           n = 0
           tkinter.messagebox.showinfo("ProjectMounika", "Congratulations, your guess is correct!")
           return
       chances -= 1
       n.set(chances)
   else:
       chances -= 1
       print(n.get())
       if (chances <= 0):
           list = ['red', 'blue', 'green', 'yellow']
           ans = list[ans[0] - 1] + "," + list[ans[1] - 1] + "," + list[ans[2] - 1] + "," + list[ans[3] - 1]
           tkinter.messagebox.showinfo("ProjectMounika","The correct ans is " + ans + ".Better luck for the next time!")
           return
       n.set(chances)
   return 0
def game():
   global ans, col1, col2, col3, col4, n, correct
   root = Tk()
   root.title("ProjectMounika")
   root.geometry('800x650')
   root.config(bg='#f5deb3')
   ans = []
   for i in range(0, 4):
       ans.append(random.randint(1, 4))
   print(ans)
   n = IntVar(root)
   n.set(10)
   correct = IntVar(root)
   correct.set(0)
   col1 = IntVar(root)
   col2 = IntVar(root)
   col3 = IntVar(root)
   col4 = IntVar(root)
   # Getting the input of word from the user
   frame = Frame(root)
   frame.pack(pady=20)
   Label(frame, text='Please make your choice', font=('Arial', 15,'bold'), relief="ridge").pack()
   frame1 = Frame(root, bg='#f5deb3')
   frame1.pack(pady=20)
   red1 = Radiobutton(frame1, text="Red", value=1, bg='white', fg='red', variable=col1, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   blue1 = Radiobutton(frame1, text="Blue", value=2, bg='white', fg='blue', variable=col1, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   green1 = Radiobutton(frame1, text="Green", value=3, bg='white', fg='green', variable=col1, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   yellow1 = Radiobutton(frame1, text="Yellow", value=4, bg='white', fg='yellow', variable=col1, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   frame2 = Frame(root, bg='#f5deb3')
   frame2.pack(pady=20)
   red2 = Radiobutton(frame2, text="Red", value=1, bg='white', fg='red', variable=col2, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   blue2 = Radiobutton(frame2, text="Blue", value=2, bg='white', fg='blue', variable=col2, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   green2 = Radiobutton(frame2, text="Green", value=3, bg='white', fg='green', variable=col2, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   yellow2 = Radiobutton(frame2, text="Yellow", value=4, bg='white', fg='yellow', variable=col2, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   frame3 = Frame(root, bg='#f5deb3')
   frame3.pack(pady=20)
   red3 = Radiobutton(frame3, text="Red", value=1, bg='white', fg='red', variable=col3, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   blue3 = Radiobutton(frame3, text="Blue", value=2, bg='white', fg='blue', variable=col3, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   green3 = Radiobutton(frame3, text="Green", value=3, bg='white', fg='green', variable=col3, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   yellow3 = Radiobutton(frame3, text="Yellow", value=4, bg='white', fg='yellow', variable=col3, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   frame4 = Frame(root, bg='#f5deb3')
   frame4.pack(pady=20)
   red4 = Radiobutton(frame4, text="Red", value=1, bg='white', fg='red', variable=col4, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   blue4 = Radiobutton(frame4, text="Blue", value=2, bg='white', fg='blue', variable=col4, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   green4 = Radiobutton(frame4, text="Green", value=3, bg='white', fg='green', variable=col4, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   yellow4 = Radiobutton(frame4, text="Yellow", value=4, bg='white', fg='yellow', variable=col4, font=('Arial', 12), relief="groove").pack(side="left",padx=10)
   frame5 = Frame(root, bg='#f5deb3')
   frame5.pack(pady=20)
   Label(frame5, text='No of chances left', bg='#f5deb3',font=('Arial', 15,'bold'), relief="ridge").pack()
   Label(frame5, textvariable=n, bg='#f5deb3', font=('Arial', 15,'normal'), anchor="e",relief="ridge").pack()
   frame6 = Frame(root, bg='#f5deb3')
   frame6.pack(pady=20)
   Label(frame6, text='No of correct choices', bg='#f5deb3',font=('Arial', 15,'bold'), relief="ridge").pack()
   # Button to do the spell check
   Label(frame6, textvariable=correct, bg='#f5deb3',font=('Arial', 15,'bold'), relief="ridge").pack(pady=20)
   Button(frame6, text="Check", bg='#f5deb3', command=checkcode, font=('Arial', 15,'bold'), relief="ridge").pack(pady=20)
   # Runs the window till it is closed by the user
   root.mainloop()
# Creating the window
window = Tk()
window.title("ProjectMounika")
window.geometry('300x200')
window.config(bg='#eabeb4')
ans = []
# Creating the variables to get the word and set the correct word
n = IntVar(window)
correct = IntVar(window)
n.set(10)
correct.set(0)
col1 = IntVar(window)
col2 = IntVar(window)
col3 = IntVar(window)
col4 = IntVar(window)
Label(window, text="Mastermind Game", font=('Arial', 15,'bold'), relief="ridge").place(x=70, y=50)
Button(window, text="Start Game", bg='#eabeb4', font=('Arial', 12),command=game).place(x=100, y=100)
window.mainloop()
