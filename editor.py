from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog
import os

#Root for main window
root = Tk(className = " Text Editor")
textArea = scrolledtext.ScrolledText(root, width=100, height=80)
root.iconbitmap('dofe.ico')

#
#Functions
#

def newFile():
    if len(textArea.get('1.0', END+'-1c')) > 0:
        if messagebox.askyesno("Save?", "Do you wish to save?"):
            saveFile()

        else:
            textArea.delete('1.0', END)
    root.title("Text Editor")


def openFile():
    textArea.delete('1.0', END)
    file = filedialog.askopenfile(parent=root, title='Select a text file', filetypes=(("Text file", "*.txt"), ("All files", "*.*")))

    root.title(os.path.basename(file.name) + " - Text Editor")


    if file != None:
        contents = file.read()
        textArea.insert('1.0', contents)
        file.close()


def saveFile():
    file = filedialog.asksaveasfile(mode='w', filetypes=(("Text file (*.txt)", "*.txt"), ("All files (*.*)", "*.*")))

    if file != None:
        #Slice off the last character from get, as an extra return (enter) is added
        data = textArea.get('1.0', END+'-1c')
        file.write(data)
        file.close()


def findInFile():
    findString = simpledialog.askstring("Find...", "Enter text")

    textData = textArea.get('1.0', END)

    occurances = textData.upper().count(findString.upper())

    if findString.upper() in textData.upper():
        label = messagebox.showinfo("Results", findString + " has multiple occurances, " + str(occurances))

    else:
        label = messagebox.showinfo("Results", "There were no findings")



def about():
    label = messagebox.showinfo("About", "This is a simple Python text editor")



def exitRoot():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()

#
#Menu options
#


menu = Menu(root)
root.config(menu = menu)
fileMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Find", command=findInFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitRoot)

helpMenu = Menu(menu)
menu.add_cascade(label= "About", command=about)

textArea.pack()


#Keeps window open
root.mainloop()
