import tkinter as tk
import time
import math
class PaperRectangleApp:
    def __init__(self, master=None):
            self.master = master
            self.master.title("Origami")

            self.b_QUIT = tk.Label(self.master, text="Origami Deisgn")        
            self.b_QUIT.pack()
            self.fold = tk.Entry(self.master)
            self.fold.pack()
            self.width1 = tk.Label(master, text="Width1:")
            self.width1.pack()
            self.width1_entry = tk.Entry(master)
            self.width1_entry.pack()

            self.width2 = tk.Label(master, text="Width2:")
            self.width2.pack()
            self.width2_entry = tk.Entry(master)
            self.width2_entry.pack()

            self.height1 = tk.Label(master, text="Height1:")
            self.height1.pack()
            self.height1_entry = tk.Entry(master)
            self.height1_entry.pack()

            self.height2 = tk.Label(master, text="Height2:")
            self.height2.pack()
            self.height2_entry = tk.Entry(master)
            self.height2_entry.pack() 
            self.draw_button = tk.Button(master, text="Draw", command=self.check)
            self.draw_button.pack()
            self.my_variable = tk.IntVar()

        # Create canvas for drawing
            self.canvas = tk.Canvas(master, width=800, height=320, bg="white")
            self.canvas.pack()
            self.my_variable.set(0)
            self.increment_button = tk.Button(self.master, text="Increment Fold", command=self.increment_value)
            self.increment_button.pack()
            self.update_text()
            self.points = []
            self.lines = []
            self.drawing_mode = False

            self.draw_button = tk.Button(master, text="Draw Line", command=self.activate_draw_mode)
            self.draw_button.pack(side=tk.LEFT)

            self.delete_button = tk.Button(master, text="Delete Line", command=self.activate_delete_mode)
            self.delete_button.pack(side=tk.LEFT)

            self.canvas.bind("<Button-1>", self.draw_or_delete_line)
    def increment_value(self):
        # Increment the value of the variable
        self.my_variable.set(self.my_variable.get() + 1)
        # Update the canvas with the new value
        self.update_text()
    def update_text(self):
    # Get the current value from the variable
        value = self.my_variable.get()
        # Clear previous text
        self.canvas.delete("text_value")
        # Display the variable value on the canvas
        self.canvas.create_text(320, 50, text="No of Folds: {}".format(value), tags="text_value")

    def activate_draw_mode(self):
        self.drawing_mode = True
        print("Draw mode activated")

    def activate_delete_mode(self):
        self.drawing_mode = False
        print("Delete mode activated")

    def draw_or_delete_line(self, event):
        if self.drawing_mode:
            self.draw_line(event)
        else:
            self.delete_line(event)
    def draw_line(self, event):
        self.points.append((event.x, event.y))
        if len(self.points) == 2:
            x1, y1 = self.points[0]
            x2, y2 = self.points[1]
            line = self.canvas.create_line(x1, y1, x2, y2)
            self.lines.append(line)
            print("Line drawn from", (x1, y1), "to", (x2, y2))
            self.points = []

    def delete_line(self, event):
        for line in self.lines:
            coords = self.canvas.coords(line)
            x1, y1, x2, y2 = coords[0], coords[1], coords[2], coords[3]
            if (abs(x1 - event.x) < 5 and abs(y1 - event.y) < 5) or (abs(x2 - event.x) < 5 and abs(y2 - event.y) < 5):
                self.lines.remove(line)
                self.canvas.delete(line)
                print("Line deleted")
                break

   

   
    def check(self):
        foldt=self.fold.get()
        w1 = int(self.width1_entry.get())
        h1 = int(self.height1_entry.get())
        w2 = int(self.width2_entry.get())
        h2 = int(self.height2_entry.get())
        if foldt=="Valley":
          self.master.after(1000,self.valley_fold) 
          self.my_variable.set(self.my_variable.get() + 1)
          self.master.after(1000,self.update_text)
        if foldt=="Mountain":
          self.master.after(1000,self.mountain_fold) 
          self.my_variable.set(self.my_variable.get() + 1)
          self.master.after(1000,self.update_text)
        if foldt=="Squash":
          self.master.after(1000,self.squash_fold) 
          self.my_variable.set(self.my_variable.get() + 4)
          self.master.after(1000,self.update_text)
        if foldt=="Square":
          self.master.after(1000,self.square_fold) 
          self.my_variable.set(self.my_variable.get() + 2)
          self.master.after(1000,self.update_text)
        if foldt=="Pleat":
          self.master.after(1000,self.pleat_fold) 
          self.my_variable.set(self.my_variable.get() + 2)
          self.master.after(1000,self.update_text)
        if foldt=="Crease":
          self.master.after(1000,self.crease_fold) 
          self.my_variable.set(self.my_variable.get() + 1)
          self.master.after(1000,self.update_text)

        if foldt=="Twist":
          self.master.after(1000,self.twist_fold)  
          self.my_variable.set(self.my_variable.get() + 12)
          self.master.after(1000,self.update_text)
        if foldt=="Sink":
          self.master.after(1000,self.sink_fold)  
          self.my_variable.set(self.my_variable.get() + 7)
          self.master.after(1000,self.update_text)
        if foldt=="Turtle":
            self.master.after(100,self.turtle)
        if foldt=="Boat":
            self.master.after(100,self.boat_fold)

    def final_square(self,l1,l2,l3,l4,l5,l6,w1,w2,h1,h2):
        self.canvas.delete(l1)
        self.canvas.delete(l2)
        self.canvas.delete(l3)
        self.canvas.delete(l4)
        self.canvas.delete(l5)
        self.canvas.delete(l6)
        l7=self.canvas.create_line((w1+w2)/2,(h2+h1)/2,(w1+w2)/2,h2, width=2)
        l8=self.canvas.create_line((w1+w2)/2,h2,w1,h2, width=2)
        l9=self.canvas.create_line(w1,(h1+h2)/2,w1,h2, width=2)
        l10=self.canvas.create_line(w1,(h1+h2)/2,(w1+w2)/2,(h2+h1)/2, width=2)
        
    def square_fold(self):
        w1 = int(self.width1_entry.get())
        h1 = int(self.height1_entry.get())
        w2 = int(self.width2_entry.get())
        h2 = int(self.height2_entry.get())
        l1=self.canvas.create_line(w1,h1,w2,h1, width=2)
        l2=self.canvas.create_line(w2,h1,w2,h2, width=2)
        l3=self.canvas.create_line(w1,h2,w2,h2, width=2)
        l4=self.canvas.create_line(w1,h2,w1,h1, width=2)
        l5=self.canvas.create_line((w1+w2)/2,h1,(w1+w2)/2,h2, dash=(2,2))
        l6=self.canvas.create_line(w1,(h1+h2)/2,w2,(h1+h2)/2, dash=(2,2))
        self.master.after(3000,self.final_square,l1,l2,l3,l4,l5,l6,w1,w2,h1,h2)  
    def final_boat(self,l1,l2,l3,l4,l5,l6,w1,w2,h1,h2):
        self.canvas.delete(l1)
        self.canvas.delete(l2)
        self.canvas.delete(l3)
        self.canvas.delete(l4)
        self.canvas.delete(l5)
        self.canvas.delete(l6)
        l7=self.canvas.create_line((w1+w2)/2,(h2+h1)/2,(w1+w2)/2,h2, width=2)
        l8=self.canvas.create_line((w1+w2)/2,h2,w1,h2, width=2)
        l9=self.canvas.create_line(w1,(h1+h2)/2,w1,h2, width=2)
        l10=self.canvas.create_line(w1,(h1+h2)/2,(w1+w2)/2,(h2+h1)/2, width=2)
        self.master.after(3000,self.fold_square,w1,w2,h1,h2,l8,l9,l7,l10)
    def fold_square(self,w1,w2,h1,h2,l8,l9,l7,l10):
        d1=self.canvas.create_line(w1,(h2+h1)/2,(w1+w2)/2,h2, width=2,dash=(2,2))
        self.master.after(3000,self.fold_square2,w1,w2,h1,h2,l8,l9,d1,l7,l10)
    def fold_square2(self,w1,w2,h1,h2,l8,l9,d1,l7,l10):
        self.canvas.delete(l8)
        self.canvas.delete(l9)
        self.canvas.delete(d1)
        p1=self.canvas.create_line(w1,(h2+h1)/2,(w1+w2)/2,h2, width=2)
        self.my_variable.set(self.my_variable.get() + 2)
        self.master.after(1000,self.update_text)
        self.master.after(3000,self.fold_square3,w1,w2,h1,h2,l7,l10,p1)
    def fold_square3(self,w1,w2,h1,h2,l7,l10,p1):
        self.canvas.delete(l10)
        self.canvas.delete(l7)
        self.canvas.delete(p1)
        p2=self.canvas.create_line((w1+w2)/2,(h2+h1)/2,(w1+w2)/2,h1, width=2)
        self.canvas.create_line((3*w1+w2)/4,(h2+3*h1)/4,(w1+w2)/2,h1, width=2)
        p3=self.canvas.create_line((3*w1+w2)/4,(h2+3*h1)/4,(w1+w2)/2,(h1+h2)/2, width=2)
        p4=self.canvas.create_line((3*w2+w1)/4,(h2+3*h1)/4,(w1+w2)/2,(h1+h2)/2, width=2)
        self.canvas.create_line((3*w2+w1)/4,(h2+3*h1)/4,(w1+w2)/2,h1, width=2)
        self.my_variable.set(self.my_variable.get() + 1)
        self.master.after(1000,self.update_text)
        self.master.after(3000,self.fold_square4,w1,w2,h1,h2,p2,p3,p4)
    def fold_square4(self,w1,w2,h1,h2,p2,p3,p4):
        self.canvas.delete(p2)
        self.canvas.delete(p3)
        self.canvas.delete(p4)
        self.canvas.create_line((3*w1+w2)/4,(h2+3*h1)/4,(3*w2+w1)/4,(h2+3*h1)/4, width=2)
        self.canvas.create_line((3*w1+w2)/4,(h2+3*h1)/4,(w2+w1)/4,h1+0.1*h1, width=2)
        self.canvas.create_line(3*(w1+w2)/4,h1+0.1*h1,(3*w2+w1)/4,(h2+3*h1)/4, width=2)
        self.canvas.create_line(3*(w1+w2)/4,h1+0.1*h1,(w2+w1)/4,h1+0.1*h1,  width=2)
        self.my_variable.set(self.my_variable.get() + 1)
        self.master.after(1000,self.update_text)
    def boat_fold(self):
        w1 = int(self.width1_entry.get())
        h1 = int(self.height1_entry.get())
        w2 = int(self.width2_entry.get())
        h2 = int(self.height2_entry.get())
        l1=self.canvas.create_line(w1,h1,w2,h1, width=2)
        l2=self.canvas.create_line(w2,h1,w2,h2, width=2)
        l3=self.canvas.create_line(w1,h2,w2,h2, width=2)
        l4=self.canvas.create_line(w1,h2,w1,h1, width=2)
        l5=self.canvas.create_line((w1+w2)/2,h1,(w1+w2)/2,h2, dash=(2,2))
        l6=self.canvas.create_line(w1,(h1+h2)/2,w2,(h1+h2)/2, dash=(2,2))
        self.master.after(3000,self.final_boat,l1,l2,l3,l4,l5,l6,w1,w2,h1,h2)
    def final_crease(self,w1,w2,h1,h2):
        
        self.canvas.create_line((w1+w2)/2,h1,(w1+w2)/2,h2, dash=(2,2))
    def crease_fold(self):
        w1 = int(self.width1_entry.get())
        h1 = int(self.height1_entry.get())
        w2 = int(self.width2_entry.get())
        h2 = int(self.height2_entry.get())
        self.canvas.create_line(w1,h1,w2,h1, width=2)
        self.canvas.create_line(w2,h1,w2,h2, width=2)
        self.canvas.create_line(w1,h2,w2,h2, width=2)
        self.canvas.create_line(w1,h2,w1,h1, width=2)
        self.master.after(3000,self.final_crease,w1,w2,h1,h2)
    def final_valley(self,l2,l3,l4,w1,w2,h1,h2,l6,l7,l8):
        self.canvas.delete(l2)
        self.canvas.delete(l3)
        self.canvas.delete(l4)
        self.canvas.delete(l6)
        self.canvas.delete(l7)
        self.canvas.delete(l8)
        self.canvas.create_line(w1,(h1+h2)/2,w2,(h1+h2)/2, width=2)
        self.canvas.create_line(w1,h1,w1,(h1+h2)/2, width=2)
        self.canvas.create_line(w2,(h1+h2)/2,w2,h1, width=2)
        self.canvas.create_line(400+w1,(h1+h2)/2,400+w2,(h1+h2)/2, width=2)
        self.canvas.create_line(400+w1,h1,400+w1,(h1+h2)/2, width=2)
        self.canvas.create_line(400+w2,(h1+h2)/2,400+w2,h1, width=2)
        # self.master.after(2000, self.update_values)
    def valley_fold(self):
        # width = int(self.width_entry.get())
        # height = int(self.height_entry.get())
        #self.canvas.delete("all")
        w1 = int(self.width1_entry.get())
        h1 = int(self.height1_entry.get())
        w2 = int(self.width2_entry.get())
        h2 = int(self.height2_entry.get())
        self.canvas.create_line(w1,h1,w2,h1, width=2)
        l2=self.canvas.create_line(w2,h1,w2,h2, width=2)
        l3=self.canvas.create_line(w1,h2,w2,h2, width=2)
        l4=self.canvas.create_line(w1,h2,w1,h1, width=2)
        self.canvas.create_line(w1,(h2+h1)/2,w2,(h1+h2)/2, dash=(2,2))
        self.canvas.create_line(400+w1,h1,400+w2,h1, width=2)
        l6=self.canvas.create_line(400+w2,h1,400+w2,h2, width=2)
        l7=self.canvas.create_line(400+w1,h2,400+w2,h2, width=2)
        l8=self.canvas.create_line(400+w1,h2,400+w1,h1, width=2)
        self.canvas.create_line(400+w1,(h2+h1)/2,400+w2,(h1+h2)/2, dash=(2,2))

        # folds=0
        # surface_area=3
        # #surface_area=(self.width2-self.width1)*(self.height2-self.height1)
        # folds_label = tk.Label(self.master, text="Folds: " + str(folds))
        # folds_label.pack()
        # surface_area_label = tk.Label(self.master, text="Surface Area: " + str(surface_area))
        # surface_area_label.pack()        
        self.master.after(3000, self.final_valley,l2,l3,l4,w1,w2,h1,h2,l6,l7,l8)


    def final_mountain(self,l2,l1,l4,w1,w2,h1,h2,l6,l7,l9):
        self.canvas.delete(l2)
        self.canvas.delete(l1)
        self.canvas.delete(l4)
        self.canvas.delete(l7)
        self.canvas.delete(l6)
        self.canvas.delete(l9)
        self.canvas.create_line(w1,(h1+h2)/2,w2,(h1+h2)/2, width=2)
        self.canvas.create_line(w1,h2,w1,(h1+h2)/2, width=2)
        self.canvas.create_line(w2,(h1+h2)/2,w2,h2, width=2)
        self.canvas.create_line(400+w1,(h1+h2)/2,400+w2,(h1+h2)/2, width=2)
        self.canvas.create_line(400+w1,h2,400+w1,(h1+h2)/2, width=2)
        self.canvas.create_line(400+w2,(h1+h2)/2,400+w2,h2, width=2)
    def mountain_fold(self):        
        #self.canvas.delete("all")
        w1 = int(self.width1_entry.get())
        h1 = int(self.height1_entry.get())
        w2 = int(self.width2_entry.get())
        h2 = int(self.height2_entry.get())
        l1=self.canvas.create_line(w1,h1,w2,h1, width=2)
        l2=self.canvas.create_line(w2,h1,w2,h2, width=2)
        l3=self.canvas.create_line(w1,h2,w2,h2, width=2)
        l4=self.canvas.create_line(w1,h2,w1,h1, width=2)
        l5=self.canvas.create_line(w1,(h2+h1)/2,w2,(h1+h2)/2, dash=(2,2))
        l6=self.canvas.create_line(400+w1,h1,400+w2,h1, width=2)
        l7=self.canvas.create_line(400+w2,h1,400+w2,h2, width=2)
        l8=self.canvas.create_line(400+w1,h2,400+w2,h2, width=2)
        l9=self.canvas.create_line(400+w1,h2,400+w1,h1, width=2)
        l10=self.canvas.create_line(400+w1,(h2+h1)/2,400+w2,(h1+h2)/2, dash=(2,2))
        self.master.after(3000, self.final_mountain,l2,l1,l4,w1,w2,h1,h2,l6,l7,l9)
    
    def sink_final(self,l1,l2,l4,l5,l6,l7,l8,l9,w1,w2,h1,h2,l10,l11,l13,l14,l15,l16,l18,l19):
        self.canvas.delete(l1)
        self.canvas.delete(l2)
        self.canvas.delete(l4)
        self.canvas.delete(l5)
        self.canvas.delete(l6)
        self.canvas.delete(l7)
        self.canvas.delete(l8)
        self.canvas.delete(l9)
        self.canvas.delete(l10)
        self.canvas.delete(l11)
        self.canvas.delete(l13)
        self.canvas.delete(l14)
        self.canvas.delete(l15)
        self.canvas.delete(l16)
        self.canvas.delete(l18)
        self.canvas.delete(l19)
        self.canvas.create_line((3*w1+w2)/4,(3*h2+h1)/4,w1,h2,width=2)
        self.canvas.create_line((3*w1+w2)/4,(3*h2+h1)/4,(3*w2+w1)/4,(3*h2+h1)/4,width=2)
        self.canvas.create_line((3*w2+w1)/4,(3*h2+h1)/4,w2,h2,width=2)
        self.canvas.create_line(400+(3*w1+w2)/4,(3*h2+h1)/4,400+w1,h2,width=2)
        self.canvas.create_line(400+(3*w1+w2)/4,(3*h2+h1)/4,400+(3*w2+w1)/4,(3*h2+h1)/4,width=2)
        self.canvas.create_line(400+(3*w2+w1)/4,(3*h2+h1)/4,400+w2,h2,width=2)        
    def sink_fold(self):
        w1 = int(self.width1_entry.get())
        h1 = int(self.height1_entry.get())
        w2 = int(self.width2_entry.get())
        h2 = int(self.height2_entry.get())
        l1=self.canvas.create_line(w1,h1,w2,h1, width=2)
        l2=self.canvas.create_line(w2,h1,w2,h2, width=2)
        self.canvas.create_line(w1,h2,w2,h2, width=2)
        l4=self.canvas.create_line(w1,h2,w1,h1, width=2)
        l5=self.canvas.create_line(w1,h1,w2,h2,dash=(2,2))
        l6=self.canvas.create_line(w2,h1,w1,h2,dash=(2,2))
        l7=self.canvas.create_line((3*w1+w2)/4,(3*h1+h2)/4,(3*w2+w1)/4,(3*h1+h2)/4,dash=(2,2))
        self.canvas.create_line((3*w1+w2)/4,(3*h2+h1)/4,(3*w2+w1)/4,(3*h2+h1)/4,dash=(2,2))
        l8=self.canvas.create_line((3*w1+w2)/4,(3*h1+h2)/4,(3*w1+w2)/4,(3*h2+h1)/4,dash=(2,2))
        l9=self.canvas.create_line((3*w2+w1)/4,(3*h1+h2)/4,(3*w2+w1)/4,(3*h2+h1)/4,dash=(2,2))
        l10=self.canvas.create_line(400+w1,h1,400+w2,h1, width=2)
        l11=self.canvas.create_line(400+w2,h1,400+w2,h2, width=2)
        self.canvas.create_line(400+w1,h2,400+w2,h2, width=2)
        l13=self.canvas.create_line(400+w1,h2,400+w1,h1, width=2)
        l14=self.canvas.create_line(400+w1,h1,400+w2,h2,dash=(2,2))
        l15=self.canvas.create_line(400+w2,h1,400+w1,h2,dash=(2,2))
        l16=self.canvas.create_line(400+(3*w1+w2)/4,(3*h1+h2)/4,400+(3*w2+w1)/4,(3*h1+h2)/4,dash=(2,2))
        self.canvas.create_line(400+(3*w1+w2)/4,(3*h2+h1)/4,400+(3*w2+w1)/4,(3*h2+h1)/4,dash=(2,2))
        l18=self.canvas.create_line(400+(3*w1+w2)/4,(3*h1+h2)/4,400+(3*w1+w2)/4,(3*h2+h1)/4,dash=(2,2))
        l19=self.canvas.create_line(400+(3*w2+w1)/4,(3*h1+h2)/4,400+(3*w2+w1)/4,(3*h2+h1)/4,dash=(2,2))
        self.master.after(3000,self.sink_final,l1,l2,l4,l5,l6,l7,l8,l9,w1,w2,h1,h2,l10,l11,l13,l14,l15,l16,l18,l19)


    def pleat_final(self,l2,l1,l3,l5,l6,l8,l9,l10,l11,l12,l13,l14,w1,w2,h1,h2):
        self.canvas.delete(l1)
        self.canvas.delete(l2)
        self.canvas.delete(l3)
        self.canvas.delete(l6)
        self.canvas.delete(l5)
        self.canvas.delete(l13)
        self.canvas.delete(l8)
        self.canvas.delete(l9)
        self.canvas.delete(l10)
        self.canvas.delete(l11)
        self.canvas.delete(l12)
        self.canvas.delete(l14)
        self.canvas.create_line((3*w2+w1)/4,h1,(3*w2+w1)/4,h2,width=2)
        self.canvas.create_line(w1,h1,(3*w2+w1)/4,h1,width=2)
        self.canvas.create_line(w1,h2,(3*w2+w1)/4,h2,width=2)
        self.canvas.create_line(400+(3*w2+w1)/4,h1,400+(3*w2+w1)/4,h2,width=2)
        self.canvas.create_line(400+w1,h1,400+(3*w2+w1)/4,h1,width=2)
        self.canvas.create_line(400+w1,h2,400+(3*w2+w1)/4,h2,width=2)       
        self.canvas.create_text(2*w2,2*h1/3, text="Folds: 2", font=("Arial", 10), fill="black") 
        self.canvas.create_text(2*w2,h1, text="Surface Area:"+str(3*(w2-w1)*(h2-h1)/2), font=("Arial", 10), fill="black")      
    def pleat_fold(self):
        w1 = int(self.width1_entry.get())
        h1 = int(self.height1_entry.get())
        w2 = int(self.width2_entry.get())
        h2 = int(self.height2_entry.get())
        l1=self.canvas.create_line(w1,h1,w2,h1, width=2)
        l2=self.canvas.create_line(w2,h1,w2,h2, width=2)
        l3=self.canvas.create_line(w1,h2,w2,h2, width=2)
        self.canvas.create_line(w1,h2,w1,h1, width=2)
        l5=self.canvas.create_line((3*w1+w2)/4,h1,(3*w1+w2)/4,h2,dash=(2,2))
        l6=self.canvas.create_line((5*w1+3*w2)/8,h1,(5*w1+3*w2)/8,h2,dash=(2,2))
        l8=self.canvas.create_line((w1+w2)/2,h1,(w1+w2)/2,h2,dash=(2,2))
        l9=self.canvas.create_line(400+w1,h1,400+w2,h1, width=2)
        l10=self.canvas.create_line(400+w2,h1,400+w2,h2, width=2)
        l11=self.canvas.create_line(400+w1,h2,400+w2,h2, width=2)
        self.canvas.create_line(400+w1,h2,400+w1,h1, width=2)
        l12=self.canvas.create_line(400+(3*w1+w2)/4,h1,400+(3*w1+w2)/4,h2,dash=(2,2))
        l13=self.canvas.create_line(400+(5*w1+3*w2)/8,h1,400+(5*w1+3*w2)/8,h2,dash=(2,2))
        l14=self.canvas.create_line(400+(w1+w2)/2,h1,400+(w1+w2)/2,h2,dash=(2,2))
        self.master.after(3000,self.pleat_final,l2,l1,l3,l5,l6,l8,l9,l10,l11,l12,l13,l14,w1,w2,h1,h2)
    def final_twist(self,l1,l2,l3,l4,l9,l10,l11,l12,w1,w2,h1,h2):
        self.canvas.delete(l1)
        self.canvas.delete(l2)
        self.canvas.delete(l3)
        self.canvas.delete(l4)
        self.canvas.delete(l9)
        self.canvas.delete(l10)
        self.canvas.delete(l12)
        self.canvas.delete(l11)
        self.canvas.create_line((w1+w2)/2,(3*h1+h2)/4,(3*w1+w2)/4,(h1+h2)/2,width=2)
        self.canvas.create_line((w1+w2)/2,(3*h1+h2)/4,(3*w2+w1)/4,(h1+h2)/2,width=2)
        self.canvas.create_line((w1+w2)/2,(3*h2+h1)/4,(3*w1+w2)/4,(h1+h2)/2,width=2)
        self.canvas.create_line((w1+w2)/2,(3*h2+h1)/4,(3*w2+w1)/4,(h1+h2)/2,width=2)
        self.canvas.create_line((5*w1+3*w2)/8,(5*h1+3*h2)/8,(3*w1+5*w2)/8,(3*h1+5*h2)/8,dash=(2,2))
        self.canvas.create_line((3*w1+5*w2)/8,(5*h1+3*h2)/8,(3*w2+5*w1)/8,(3*h1+5*h2)/8,dash=(2,2))
        

    def twist_fold(self):
        w1 = int(self.width1_entry.get())
        h1 = int(self.height1_entry.get())
        w2 = int(self.width2_entry.get())
        h2 = int(self.height2_entry.get())
        l1=self.canvas.create_line(w1,h1,w2,h1, width=2)
        l2=self.canvas.create_line(w2,h1,w2,h2, width=2)
        l3=self.canvas.create_line(w1,h2,w2,h2, width=2)
        l4=self.canvas.create_line(w1,h2,w1,h1, width=2)
        l5=self.canvas.create_line((w1+w2)/2,(3*h1+h2)/4,(3*w1+w2)/4,(h1+h2)/2,dash=(2,2))
        l6=self.canvas.create_line((w1+w2)/2,(3*h1+h2)/4,(3*w2+w1)/4,(h1+h2)/2,dash=(2,2))
        l7=self.canvas.create_line((w1+w2)/2,(3*h2+h1)/4,(3*w1+w2)/4,(h1+h2)/2,dash=(2,2))
        l8=self.canvas.create_line((w1+w2)/2,(3*h2+h1)/4,(3*w2+w1)/4,(h1+h2)/2,dash=(2,2))
        l9=self.canvas.create_line((w1+w2)/2,(3*h1+h2)/4,(w1+w2)/2,h1,dash=(2,2))
        l10=self.canvas.create_line((w1+w2)/2,(3*h2+h1)/4,(w1+w2)/2,h2,dash=(2,2))
        l11=self.canvas.create_line(w1,(h1+h2)/2,(3*w1+w2)/4,(h1+h2)/2,dash=(2,2))
        l12=self.canvas.create_line(w2,(h1+h2)/2,(3*w2+w1)/4,(h1+h2)/2,dash=(2,2))
        self.canvas.after(3000,self.final_twist,l1,l2,l3,l4,l9,l10,l11,l12,w1,w2,h1,h2)

    def final_squash(self,l2,l3,l4,l5,l6,w1,w2,h1,h2):
        self.canvas.delete(l2)
        self.canvas.delete(l3)
        self.canvas.delete(l4)
        self.canvas.delete(l5)
        self.canvas.delete(l6)
        self.canvas.create_line(w1,h1,w2,h1,width=2)
        self.canvas.create_line(w1,h1,w1,(h1+h2)/2, width=2)
        self.canvas.create_line(w1,(h2+h1)/2,(w1+w2)/2,(h2+h1)/2,width=2)
        self.canvas.create_line(w1,h1,(w1+w2)/2,(h2+h1)/2,width=2)
        self.canvas.create_line(w2,h1,(w1+w2)/2,(h2+h1)/2,width=2)        
    def squash_fold(self):
        w1 = int(self.width1_entry.get())
        h1 = int(self.height1_entry.get())
        w2 = int(self.width2_entry.get())
        h2 = int(self.height2_entry.get())
        l1=self.canvas.create_line(w1,h1,w2,h1, width=2)
        l2=self.canvas.create_line(w2,h1,w2,h2, width=2)
        l3=self.canvas.create_line(w1,h2,w2,h2, width=2)
        l4=self.canvas.create_line(w1,h2,w1,h1, width=2)
        l5=self.canvas.create_line(w1,(h2+h1)/2,w2,(h1+h2)/2, dash=(2,2))
        l6=self.canvas.create_line((w1+w2)/2,h1,(w1+w2)/2,h2, dash=(2,2))
        self.master.after(8000,self.final_squash,l2,l3,l4,l5,l6,w1,w2,h1,h2)

    def turtle(self):
        # Get width and height from user input
        w1 = int(self.width1_entry.get())
        h1 = int(self.height1_entry.get())
        w2 = int(self.width2_entry.get())
        h2 = int(self.height2_entry.get())
        if (w2-w1)!=(h2-h1) :
            self.canvas.delete("all")
            self.canvas.create_text(300, 20, text="Given paper can't be folded into a Turtle efficiently", font=("Arial", 16), fill="black")
            return 
        # Clear canvas
        l1=self.canvas.create_line(w1,h1,w2,h1, width=2)
        l2=self.canvas.create_line(w2,h1,w2,h2, width=2)
        l3=self.canvas.create_line(w1,h2,w2,h2, width=2)
        self.lines.append(l3)
        l4=self.canvas.create_line(w1,h2,w1,h1, width=2)
        d1=self.canvas.create_line((w1+w2)/2,h2,(w1+w2)/2,h1, dash=(2,2))
        d2=self.canvas.create_line(w1,(h1+h2)/2,(w1+w2)/2,h1, dash=(2,2))
        d3=self.canvas.create_line(w2,(h1+h2)/2,(w1+w2)/2,h1, dash=(2,2))
        l8=self.canvas.create_line(400+w1,h1,400+w2,h1, width=2)
        l9=self.canvas.create_line(400+w2,h1,400+w2,h2, width=2)
        p1=self.canvas.create_line(400+w1,h2,400+w2,h2, width=2)
        self.lines.append(p1)
        l10=self.canvas.create_line(400+w1,h2,400+w1,h1, width=2)
        d4=self.canvas.create_line(400+(w1+w2)/2,h2,400+(w1+w2)/2,h1, dash=(2,2))
        d5=self.canvas.create_line(400+w1,(h1+h2)/2,400+(w1+w2)/2,h1, dash=(2,2))
        d6=self.canvas.create_line(400+w2,(h1+h2)/2,400+(w1+w2)/2,h1, dash=(2,2))
        self.master.after(3000, self.cp1,w1,w2,h1,h2,l1,l2,l4,l8,l9,l10,d1,d2,d3,d4,d5,d6)
    def cp1(self,w1,w2,h1,h2,l1,l2,l4,l8,l9,l10,d1,d2,d3,d4,d5,d6):
       self.canvas.delete(l1)
       self.canvas.delete(l2)
       self.canvas.delete(l4)
       self.canvas.delete(l8)
       self.canvas.delete(l9)
       self.canvas.delete(l10)
       self.canvas.delete(d1)
       self.canvas.delete(d2)
       self.canvas.delete(d4)
       self.canvas.delete(d3)
       self.canvas.delete(d5)
       self.canvas.delete(d6)
       l11=self.canvas.create_line(w1,(h1+h2)/2,(w1+w2)/2,h1, width=2)
       l12=self.canvas.create_line(w2,(h1+h2)/2,(w1+w2)/2,h1, width=2)
       l13=self.canvas.create_line(w1,(h1+h2)/2,w1,h2, width=2)
       l14=self.canvas.create_line(w2,(h1+h2)/2,w2,h2, width=2)
       l19=self.canvas.create_line(w1,(h1+h2)/2,(w1+w2)/2,(h1+h2)/2, width=2)
       l20=self.canvas.create_line(w2,(h1+h2)/2,(w1+w2)/2,(h1+h2)/2, width=2)
       l21=self.canvas.create_line((w1+w2)/2,(h1+h2)/2,(w1+w2)/2,h1, width=2)
       self.lines.append(l19)
       self.lines.append(l20)
       self.lines.append(l21)
       l15=self.canvas.create_line(400+w1,(h1+h2)/2,400+(w1+w2)/2,h1, width=2)
       l16=self.canvas.create_line(400+w2,(h1+h2)/2,400+(w1+w2)/2,h1, width=2)
       l17=self.canvas.create_line(400+w1,(h1+h2)/2,400+w1,h2, width=2)
       l18=self.canvas.create_line(400+w2,(h1+h2)/2,400+w2,h2, width=2)
       self.my_variable.set(self.my_variable.get() + 3)
       self.master.after(1000,self.update_text)
       #self.master.after(3000, self.cp2,l11,l12,l13,l14,l15,l16,l17,l18,w1,w2,h1,h2)
    def cp2(self,l11,l12,l13,l14,l15,l16,l17,l18,w1,w2,h1,h2):
        # self.lines.remove(l11)
        self.canvas.delete(l11) 
        # self.lines.remove(l12)
        self.canvas.delete(l12)
        # self.lines.remove(l13)
        self.canvas.delete(l13) 
        # self.lines.remove(l14)
        self.canvas.delete(l14)
        # self.lines.remove(l15) 
        self.canvas.delete(l15)
        # self.lines.remove(l16)
        self.canvas.delete(l16)
        # self.lines.remove(l17)
        self.canvas.delete(l17) 
        # self.lines.remove(l18)
        self.canvas.delete(l18)         
        l22=self.canvas.create_line(400+(w1+w2)/2,(h1+h2)*0.7,400+(w1+w2)/2,h1, width=2)
        self.lines.append(l22)
        
        # l23=self.canvas.create_line(400+(w1+w2)*0.2,h2,400+(w1+w2)/2,h1, width=2)
        # l24=self.canvas.create_line(400+(w1+w2)/2,(h1+h2)*0.7,400+(w1+w2)/2,h1, width=2)
        # l25=self.canvas.create_line(400+(w1+w2)*0.5,(h1+h2)*0.7,400+(w1+w2)/2,h1, width=2)
        # self.lines.append(l22)
        # self.lines.append(l23)
        # self.lines.append(l24)
        # self.lines.append(l25) 
    

def main():
    root = tk.Tk()
    app = PaperRectangleApp(root)  
    root.mainloop()

if __name__ == "__main__":
    main()
