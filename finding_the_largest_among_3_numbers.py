# Assignment#4: Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

#pseudocode
import tkinter as tk 
from tkinter import simpledialog
from tkinter import messagebox
from PIL import ImageTk, Image

#ask user for input
first_number = float(input("Please input your 1st Number: "))
second_number = float(input("Please input your 2nd Number: "))
third_number = float(input("Please input your 3rd Number: "))

#check for the larger number in the three numbers collected
if first_number > second_number:
    if first_number > third_number:
        largest_number = first_number
    else:
        if second_number > third_number:
            largest_number = second_number

if second_number > first_number:
    if second_number > third_number:
        largest_number = second_number
    else:
        if third_number > first_number:
            largest_number = third_number

if third_number > second_number:
    if third_number > first_number:
        largest_number = third_number
    else:
        if first_number > second_number:
            largest_number = third_number

if first_number == second_number:
    if first_number > third_number or second_number > third_number:
        largest_number = first_number or second_number
    else:
        largest_number = third_number

if second_number == third_number:
    if second_number > first_number or third_number > first_number:
        largest_number = third_number or second_number
    else:
        largest_number = first_number

if first_number == third_number:
    if first_number > second_number or third_number > second_number:
        largest_number = first_number or third_number
    else:
        largest_number = second_number

#check if the numbers are equal to each other
if first_number == second_number and first_number == third_number and second_number == third_number:
    equal_numbers = print(f"The numbers {first_number}, {second_number} and {third_number} are equal to each other.")
    exit()

#print the largest number among the 3
print(f"Among the numbers {first_number}, {second_number} and {third_number}, the largest is {largest_number}")

def user_input_three_numbers():
    simpledialog(first_number)
    simpledialog(second_number)
    simpledialog(third_number)

    biggest = largest_number

    notice = messagebox.showinfo("Result", equal_numbers)

root = tk.Tk()
root.geometry("1280x720")
root.title("wala pa title wahahaha")
root.config(bg= "#FDF5DF")

root.mainloop()