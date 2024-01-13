from tkinter import *
import tkinter.filedialog as fdialog

filename = None

def newFile(event=None):
    """
    Create a new file, resetting the text widget content.
    """
    text.delete(0.0, END)

def openFile(event=None):
    """
    Open a file dialog to select and read the content of a file into the text widget.
    """
    file_path = fdialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete(0.0, END)
            text.insert(0.0, content)

def saveFile(event=None):
    """
    Save the content of the text widget to the current file.
    """
    global filename
    if filename:
        with open(filename, 'w') as file:
            content = text.get(0.0, END)
            file.write(content)

def saveAs(event=None):
    """
    Save the content of the text widget to a new file.
    """
    file_path = fdialog.asksaveasfilename()
    if file_path:
        with open(file_path, 'w') as file:
            content = text.get(0.0, END)
            file.write(content)

# Themes
def themeDark():
    text.config(bg="#1A1A1A", fg="#CCCCCC")

def themeNord():
    text.config(bg="#2E3440", fg="#E5E9F0")

def themeOcean():
    text.config(bg="#0F1C2B", fg="#AEDFF2")

def themeBlack():
    text.config(bg="black", fg="white")

def themeWhite():
    text.config(bg="white", fg="black")

# Initialize the Tkinter root window
root = Tk()
root.title("Jonah's Text Editor")


# Get screen dimensions
sheight = root.winfo_screenheight()
swidth = root.winfo_screenwidth()

# Set minimum window size
root.minsize(width=400, height=350)

# Create a Text widget for editing text
text = Text(root, width=300, height=500)
text.pack()

# Default Dark mode theme
text.config(bg="#1A1A1A", fg="#CCCCCC")

# Create a menu bar
menubar = Menu(root)
filemenu = Menu(menubar)
thememenu = Menu(menubar)

# File menu items
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Open File", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)

# Theme Menu Items
thememenu.add_command(label="Dark", command=themeDark)
thememenu.add_command(label="Nord", command=themeNord)
thememenu.add_command(label="Ocean", command=themeOcean)
thememenu.add_command(label="Black", command=themeBlack)
thememenu.add_command(label="Light", command=themeWhite)

# Add the file menu to the menu bar
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Themes", menu=thememenu)

# Set the menu bar in the root window
root.config(menu=menubar)

# Keybindings
root.bind("<Control-n>", newFile)  # Ctrl+N for new file
root.bind("<Control-o>", openFile)  # Ctrl+O for open file
root.bind("<Control-s>", saveFile)  # Ctrl+S for save file
root.bind("<Control-Shift-S>", saveAs)  # Ctrl+Shift+S for save as
root.bind("<Control-Q>", root.quit) # Ctrl+Q to quit

# Start the Tkinter event loop
root.mainloop()
