VER = "ALPHA ALPHA ALPHA BUGGY OR UNDER DEV"


AUTHOR = "QNthuman"

from tkinter import *





class newframe:
    def __init__(self, title="",framesize="200x200",buttons=[],button_command=[],labels=[]) -> None:
        self.title = title
        self.framesize = framesize
        self.buttons = list(buttons)
        self.button_command = list(button_command)
        self.labels = labels

    def add_button(self,button_name,button_command):
        self.buttons.append(button_name)
        self.button_command.append(button_command)

    def delete_button(self,button_name):
        button_index = int(self.buttons.index(button_name))
        self.button_command.pop(button_index)
        self.buttons.remove(button_name)

    def add_label(self,label_name):
        self.labels.append(label_name)

    def delete_label(self,label_name):
        self.labels.remove(label_name)

 

    def initialise(self):
        root = Tk()
        root.title(self.title)
        root.geometry(self.framesize)
        frame = Frame(root)
        frame.pack()
        if self.buttons != None:
            for button  in self.buttons:
                button_name = button
                button_index= self.buttons.index(button_name)
                final_command = self.button_command[button_index]
                button = Button(frame,text=button_name,command=final_command)
                button.pack()

        if self.labels != None:
             for label  in self.labels:
                label = Label(frame,text=button_name)
                label.pack()


        root.mainloop()


        


    

if __name__ == "__main__":  
 

    def hello():
        print("hello")
     
    QuickAccess = newframe("QuickAccess","400x400",buttons=["hello","hello1","hello2","hello3"],button_command=[hello,hello,hello,hello])
    QuickAccess.add_button("lol",quit)
    QuickAccess.delete_button("lol")
    QuickAccess.add_button("quit",quit)
    QuickAccess.add_label("lol")
    QuickAccess.initialise()

