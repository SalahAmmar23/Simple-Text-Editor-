from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Al madrasa Porject - Text Editor")
root.iconbitmap("")
root.geometry("1200x660")

#create new file function
def new_file():
    my_text.delete("1.0", END)
    root.title("New File - Text Editor")
    
#create a new function for opening a file
def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfile(initialdir="", title="Open File", filetypes=(("Text Files", "*.txt"),("Python Files","*.py"),("All Files","*.*")))
    
    if text_file is not None:
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()

#create a new function for save as file
def save_as_file():
    text_file = filedialog.asksaveasfile(defaultextension=".txt", initialdir="c:/gui/", title="Save File", filetypes=(("Text Files", "*.txt"),("Python Files","*.py"),("All Files","*.*")))
    if text_file:
        text_file.write(my_text.get("1.0", END))
        text_file.close()
        
#create main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

#crete Scroll bar 
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)


#create text bot
my_text =  Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

#configure scrollbar
text_scroll.config(command=my_text.yview)

#create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add file menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator
file_menu.add_command(label="Exit", command=root.quit)

#Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")



root.mainloop()
