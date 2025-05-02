# Photo Editor

#Imports
from tkinter import Tk, Menu


# Main App
#------------------------------------------------------------------------------------------------------------------------------------------------------------->

App = Tk()


#App configs
#------------------------------------------------------------------------------------------------------------------------------------------------------------->
App.title("Photo Editor") 
App.geometry("800x600")
App.config(bg="white")
App.resizable(False, False)



#Creating a menu bar
#------------------------------------------------------------------------------------------------------------------------------------------------------------->
MenuBar = App.menu = Menu(App)
App.config(menu=MenuBar)


# Creaeting submenu for app
#------------------------------------------------------------------------------------------------------------------------------------------------------------->


#1 - MenuBar - File Menu --------------------------------------------------------------------------->

FileMenu = Menu(MenuBar, tearoff=0)
MenuBar.add_cascade(label="File", menu=FileMenu)

#Commands for File Menu
FileMenu.add_command(label="Open",)
FileMenu.add_command(label="Export",)
FileMenu.add_command(label="Save",)



#2 - MenuBar - Edit Menu --------------------------------------------------------------------------->

EditMenu = Menu(MenuBar, tearoff=0)
MenuBar.add_cascade(label="Edit", menu=EditMenu)

#Commands for Edit Menu
EditMenu.add_command(label="Undo",)
EditMenu.add_command(label="Redo",)



#3 - MenuBar - Effect Menu   --------------------------------------------------------------------------->

EffectMenu = Menu(MenuBar, tearoff=0)
MenuBar.add_cascade(label="Effects", menu=EffectMenu)

#Commands for Effect Menu
EffectMenu.add_command(label="Grayscale",)
EffectMenu.add_command(label="Sepia",)
EffectMenu.add_command(label="Blur",)
EffectMenu.add_command(label="Sharpen",)



#4 - MenuBar - Enhance Menu   --------------------------------------------------------------------------->

EnhanceMenu = Menu(MenuBar, tearoff=0)
MenuBar.add_cascade(label="Enhance", menu=EnhanceMenu)

#Commands for Effect Menu






#Running the app
#------------------------------------------------------------------------------------------------------------------------------------------------------------->

if __name__ == "__main__":
    App.mainloop()
