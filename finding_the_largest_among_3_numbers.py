# Assignment#4: Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

#pseudocode
from tkinter import *
import tkinter as tk
import time
from tkinter import simpledialog
from tkinter import messagebox
from PIL import ImageTk, Image

def user_input_three_numbers():
    #ask user for input
    # first_number = float(input("Please input your 1st Number: "))
    # second_number = float(input("Please input your 2nd Number: "))
    # third_number = float(input("Please input your 3rd Number: "))
    
    first_number = simpledialog.askfloat("Your First Number","Please input your 1st Number: ")
    if first_number == None:
        messagebox.showerror("Error", "Please input a number ") 

    second_number = simpledialog.askfloat("Your Second Number","Please input your 2nd Number: ")
    if second_number == None:
        messagebox.showerror("Error", "Please input a number ")

    third_number = simpledialog.askfloat("Your Third Number","Please input your 3rd Number: ")
    if third_number == None:
        messagebox.showerror("Error", "Please input a number ")

    #check if the numbers are equal to each other
    if first_number == second_number == third_number:
        result_equal= (f"The numbers {first_number}, {second_number} and {third_number} are equal to each other.")
        messagebox.showinfo("Results",result_equal )

    #check for the largest number in the three numbers collected
    else:
        largest_number = max(first_number, second_number, third_number)
        result = (f"Among the numbers {first_number}, {second_number} and {third_number}, the largest is {largest_number}")
        messagebox.showinfo("Results",result )


main_window = tk.Tk()
main_window.title("Emu finds the largest number!!!")
# main_window.geometry("1280x720")
WIDTH = 932
HEIGTH = 697
# horizontal_velocity = 1
# vertical_velocity = 1
canvas = Canvas(main_window, width=WIDTH, height= HEIGTH)
canvas.pack()
main_window.resizable(False,False)

# bg_img = Image.open("images/emu_bg.png")
# resized = bg_img.resize((1280,720))
# new_bg_img = ImageTk.PhotoImage(resized)
# bg_img_label = Label(main_window, image = new_bg_img).place(relx=0/1280,rely=0/720)

bg_photo = PhotoImage(file="images/emu_bg2.png")
title_image = canvas.create_image(0, 0, image = bg_photo, anchor=NW)

photo_title = PhotoImage(file="images/main_title_1.png")
title_image = canvas.create_image(600, 200, image = photo_title)

photo_title2 = PhotoImage(file="images/main_title_2.png")
title_image2 = canvas.create_image(600, 260, image = photo_title2)

# photo_float = PhotoImage(file="images/Wonderhoy!.png")
# float_image = canvas.create_image(0, 0, image = photo_float, anchor=NW)

# while True:
#     coordinates = canvas.coords(float_image)
#     print(coordinates)
#     canvas.move(float_image, horizontal_velocity,0)
#     main_window.update()
#     time.sleep(0.01)

button_img = Image.open("images/button.png")
resized = button_img.resize((50,50))
new_bg_img = ImageTk.PhotoImage(resized)

start_btn = tk.Button(main_window, image=new_bg_img, command= user_input_three_numbers)
start_btn.pack()

main_window.mainloop()