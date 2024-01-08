# Assignment#4: Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

#pseudocode
import tkinter as tk 
from tkinter import simpledialog
from tkinter import messagebox
from PIL import ImageTk, Image

    # def user_input_three_numbers():
        
    #     simpledialog(first_number)
    #     simpledialog(second_number)
    #     simpledialog(third_number)

    #     # biggest = largest_number

    #     messagebox.showinfo("Result", equal_numbers)

def user_input_three_numbers():
    #ask user for input
    first_number = float(input("Please input your 1st Number: "))
    second_number = float(input("Please input your 2nd Number: "))
    third_number = float(input("Please input your 3rd Number: "))

    #check if the numbers are equal to each other
    if first_number == second_number == third_number:
        print(f"The numbers {first_number}, {second_number} and {third_number} are equal to each other.")

    #check for the largest number in the three numbers collected
    else:
        largest_number = max(first_number, second_number, third_number)
        print(f"Among the numbers {first_number}, {second_number} and {third_number}, the largest is {largest_number}")

root = tk.Tk()
root.geometry("1280x720")
root.title("Emu finds the largest number!!!")
root.resizable(False,False)

bg_img = Image.open("images/emu_bg.png")
resized = bg_img.resize((1280,720))
new_bg_img = ImageTk.PhotoImage(resized)
tk.Label(root, image = new_bg_img).place(relx=0/1280,rely=0/720)

title_img = tk.PhotoImage(file="images/main_title.png")
title_img_label = tk.Label(root, image=title_img).place(relx= 0/500, rely= 0/500)

root.mainloop()
