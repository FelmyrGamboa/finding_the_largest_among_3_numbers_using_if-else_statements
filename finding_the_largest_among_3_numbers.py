# Assignment#4: Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

#pseudocode
from tkinter import *
import tkinter as tk
import time
from tkinter import simpledialog
from tkinter import messagebox
from PIL import ImageTk, Image

def user_input_three_numbers(event):
    # #ask user for input    
    def emu_conversation(event):
        #ask user to enter first number
        first_entry = simpledialog.askfloat("Your First Number","Please input your 1st Number: ")
        if first_entry == None:
            messagebox.showerror("Error", "Please input a number ")
            first_entry.quit()
        
        # ask user to enter second number
        second_entry = simpledialog.askfloat("Your Second Number","Please input your 2nd Number: ")
        if second_entry == None:
            messagebox.showerror("Error", "Please input a number")
            second_entry.quit()
        
        # ask user to enter third number
        third_entry = simpledialog.askfloat("Your Third Number","Please input your 3rd Number: ")
        if third_entry == None:
            messagebox.showerror("Error", "Please input a number ")
            third_entry.quit()
        
        #check for the largest number in the three numbers collected
        if first_entry == second_entry == third_entry:
            result_equal= (f"The numbers {first_entry}, {second_entry} and {third_entry} are equal to each other.")
            messagebox.showinfo("Results",result_equal )
            main_window.destroy()

        else:
            largest_number = max(first_entry, second_entry, third_entry)
            result = (f"Among the numbers {first_entry}, {second_entry} and {third_entry}, the largest is {largest_number}")
            messagebox.showinfo("Results",result )
            main_window.destroy()
    
    def back_to_main(event):
        user_window.destroy()

    user_window = tk.Toplevel(main_window)
    user_window.title("Emu finds the largest number!!!")
    WIDTH = 1150
    HEIGTH = 690
    canvas = Canvas(user_window, width=WIDTH, height= HEIGTH)
    canvas.pack()
    user_window.resizable(False,False)

    user_bg_img = Image.open("images/classroom_bg.png")
    resized_user = user_bg_img.resize((1150,690))
    new_user_bg_img = ImageTk.PhotoImage(resized_user)
    user_display = canvas.create_image(0, 0, image=new_user_bg_img, anchor=tk.NW)

    girl_model = Image.open("images/emu_2d_model.png")
    resized_girl_model = girl_model.resize((389,670))
    new_girl_model = ImageTk.PhotoImage(resized_girl_model)
    girl_model_display = canvas.create_image(400, 25, image=new_girl_model, anchor=tk.NW)

    textbox_img = Image.open("images/textbox.png")
    resized_textbox = textbox_img.resize((1000,200))
    new_textbox_img = ImageTk.PhotoImage(resized_textbox)
    textbox_display = canvas.create_image(100, 450, image=new_textbox_img, anchor=tk.NW)

    namebox_img = Image.open("images/namebox.png")
    resized_namebox = namebox_img.resize((450,80))
    new_namebox_img = ImageTk.PhotoImage(resized_namebox)
    namebox_display = canvas.create_image(150, 420, image=new_namebox_img, anchor=tk.NW)

    model_name = Image.open("images/emu_name.png")
    resized_model_name = model_name.resize((350,50))
    new_model_name = ImageTk.PhotoImage(resized_model_name)
    model_name_display = canvas.create_image(200, 435, image=new_model_name, anchor=tk.NW)

    conversation_text = Image.open("images/conversation_text.png")
    resized_conversation_text = conversation_text.resize((450,50))
    new_conversation_text = ImageTk.PhotoImage(resized_conversation_text)
    conversation_text_display = canvas.create_image(140, 515, image=new_conversation_text, anchor=tk.NW)

    conversation_text_2 = Image.open("images/conversation_text_2.png")
    resized_conversation_text_2 = conversation_text_2.resize((450,50))
    new_conversation_text_2 = ImageTk.PhotoImage(resized_conversation_text_2)
    conversation_text_2_display = canvas.create_image(610, 515, image=new_conversation_text_2, anchor=tk.NW)

    #cursor of the buttons
    def enter():
        canvas.config(cursor="hand2")

    def leave():
        canvas.config(cursor="")

    submit_button = Image.open("images/submit_button.png")
    resized_submit_button = submit_button.resize((150,50))
    new_submit_button = ImageTk.PhotoImage(resized_submit_button)
    submit_button_display = canvas.create_image(700, 575, image=new_submit_button, anchor=tk.NW, tag = tagname)
    canvas.tag_bind(submit_button_display, "<Button-1>", emu_conversation)
    
    back_button = Image.open("images/back_button.png")
    resized_back_button = back_button.resize((150,50))
    new_back_button = ImageTk.PhotoImage(resized_back_button)
    back_button_display = canvas.create_image(300, 575, image=new_back_button, anchor=tk.NW, tag = tagname)
    canvas.tag_bind(back_button_display, "<Button-1>", back_to_main)

    canvas.tag_bind(tagname, "<Enter>", lambda event: enter())
    canvas.tag_bind(tagname, "<Leave>", lambda event: leave())

    user_window.mainloop()

def exit_window(event):
    main_window.destroy()


main_window = tk.Tk()
main_window.title("Emu finds the largest number!!!")
WIDTH = 1150
HEIGTH = 690
canvas = Canvas(main_window, width=WIDTH, height= HEIGTH)
canvas.pack()
main_window.resizable(False,False)

bg_img = Image.open("images/emu_bg_final.png")
resized = bg_img.resize((1150,690))
new_bg_img = ImageTk.PhotoImage(resized)
bg_img_canvas = canvas.create_image(0, 0, image= new_bg_img, anchor=tk.NW)

text_blur = Image.open("images/text_blur.png")
resized_text_blur = text_blur.resize((540,200))
new_text_blur = ImageTk.PhotoImage(resized_text_blur)
new_text_blur_display = canvas.create_image(300, 230, image = new_text_blur)

photo_title = Image.open("images/main_title_1.png")
resized_title = photo_title.resize((400,50))
new_photo_title = ImageTk.PhotoImage(resized_title)
title_display = canvas.create_image(300, 200, image = new_photo_title)

photo_title_2 = Image.open("images/main_title_2.png")
resized_title_2 = photo_title_2.resize((540,50))
new_photo_title_2 = ImageTk.PhotoImage(resized_title_2)
title_display_2 = canvas.create_image(300, 250, image = new_photo_title_2)

#cursor event of the buttons
def enter():
    canvas.config(cursor="hand2")

def leave():
    canvas.config(cursor="")

tagname = "event"
start_button = Image.open("images/start_button.png")
resized_start_button = start_button.resize((230,75))
new_start_button = ImageTk.PhotoImage(resized_start_button)
start = canvas.create_image(300, 400, image= new_start_button, tag = tagname)
canvas.tag_bind(start, "<Button-1>", user_input_three_numbers)

exit_button = Image.open("images/exit_button.png")
resized_exit_button = exit_button.resize((170,60))
new_exit_button = ImageTk.PhotoImage(resized_exit_button)
exit = canvas.create_image(300, 500, image= new_exit_button, tag = tagname)
canvas.tag_bind(exit, "<Button-1>", exit_window)
canvas.tag_bind(tagname, "<Enter>", lambda event: enter())
canvas.tag_bind(tagname, "<Leave>", lambda event: leave())

main_window.mainloop()