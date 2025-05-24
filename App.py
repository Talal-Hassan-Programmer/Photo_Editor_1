# Photo Editor

#Imports
from tkinter import Tk, Menu, Canvas
import Func  # Assuming Func.py contains the necessary functions for image handling


# Main App
#------------------------------------------------------------------------------------------------------------------------------------------------------------->

App = Tk()


#App configs
#------------------------------------------------------------------------------------------------------------------------------------------------------------->
App.title("Photo Editor") 
App.geometry("800x600")
App.config(bg="white")
App.resizable(False, False)


#Canvas For Image Display
#------------------------------------------------------------------------------------------------------------------------------------------------------------->

canvas = Canvas(App, width=700, height=500)  # Adjust size as needed
canvas.pack()





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
FileMenu.add_command(label="Open", command=lambda: Func.open_image(canvas))  # Assuming Func.py has a function to open images
FileMenu.add_command(label="Save", command=lambda: Func.save_image(canvas.pil_image))  # Assuming Func.py has a function to save images
FileMenu.add_command(label="Exit", command=App.quit)



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

#Commands for Enhance Menu
EnhanceMenu.add_command(label="Brightness",)
EnhanceMenu.add_command(label="Contrast",)
EnhanceMenu.add_command(label="Sharpness", command=lambda: Func.create_sharpness_slider(App, canvas))  # Assuming Func.py has a function to create a sharpness slider for adjsting sharpness




#1 - Enhance - Color Menu   ---------------------------------------------------------------------------> 
ColorMenu = Menu(EnhanceMenu, tearoff=0)
EnhanceMenu.add_cascade(label="Color", menu=ColorMenu)

#commands for Color Menu
ColorMenu.add_command(label="Hue",)
ColorMenu.add_command(label="Saturation",)
ColorMenu.add_command(label="Vibrance",)
ColorMenu.add_command(label="Temperature",)
ColorMenu.add_command(label="Color Balance",)
ColorMenu.add_command(label="Tint",)
ColorMenu.add_command(label="Gamma",)







#Running the app
#------------------------------------------------------------------------------------------------------------------------------------------------------------->

if __name__ == "__main__":
    App.mainloop()
