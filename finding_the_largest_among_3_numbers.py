# Assignment#4: Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

#pseudocode
from tkinter import *
import tkinter as tk
import pygame.mixer
from tkinter import simpledialog
from tkinter import messagebox
from PIL import ImageTk, Image

#music
def emu_welcome_bgm():
    pygame.mixer.init()
    pygame.mixer.music.load("music/emu_welcome_bgm.wav")
    pygame.mixer.music.play(-1)

def user_input_three_numbers(event):
    # #ask user for input    
    def emu_conversation(event):
        #ask user to enter first number
        first_entry = simpledialog.askfloat("Your First Number","Please input your 1st Number: ")
        # ask user to enter second number
        second_entry = simpledialog.askfloat("Your Second Number","Please input your 2nd Number: ")        
        # ask user to enter third number
        third_entry = simpledialog.askfloat("Your Third Number","Please input your 3rd Number: ")

        #check for the largest number in the three numbers collected
        if first_entry == None or second_entry == None or third_entry == None:
            messagebox.showerror("Error", "Please input a number! Emu is not happy: " + f"\n" + f"                                                           ╱|、" + f"\n" + f"                                                         (˚ˎ 。7 " + f"\n" + f"                                                          |、˜〵" + f"\n" + f"                                                          じしˍ,)ノ")
            user_window.destroy()

        else:
            largest_number = max(first_entry, second_entry, third_entry)
            result = (f"Among the numbers {first_entry}, {second_entry} and {third_entry}, the largest is {largest_number}")
            messagebox.showinfo("Results",result )
            user_window.destroy()
    
    def back_to_main(event):
        user_window.destroy()

    #secondary_display
    user_window = tk.Toplevel(main_window)
    user_window.title("Emu finds the largest number!!!")
    WIDTH = 1150
    HEIGTH = 690
    canvas = Canvas(user_window, width=WIDTH, height= HEIGTH)
    canvas.pack()
    user_window.resizable(False,False)

    #user window elements
    user_bg_img = Image.open("user_window_elements/classroom_bg.png")
    resized_user = user_bg_img.resize((1150,690))
    new_user_bg_img = ImageTk.PhotoImage(resized_user)
    user_display = canvas.create_image(0, 0, image=new_user_bg_img, anchor=tk.NW)

    girl_model = Image.open("user_window_elements/emu_2d_model.png")
    resized_girl_model = girl_model.resize((389,670))
    new_girl_model = ImageTk.PhotoImage(resized_girl_model)
    girl_model_display = canvas.create_image(400, 25, image=new_girl_model, anchor=tk.NW)

    textbox_img = Image.open("user_window_elements/textbox.png")
    resized_textbox = textbox_img.resize((1000,200))
    new_textbox_img = ImageTk.PhotoImage(resized_textbox)
    textbox_display = canvas.create_image(100, 450, image=new_textbox_img, anchor=tk.NW)

    namebox_img = Image.open("user_window_elements/namebox.png")
    resized_namebox = namebox_img.resize((450,80))
    new_namebox_img = ImageTk.PhotoImage(resized_namebox)
    namebox_display = canvas.create_image(150, 420, image=new_namebox_img, anchor=tk.NW)

    model_name = Image.open("user_window_elements/emu_name.png")
    resized_model_name = model_name.resize((350,50))
    new_model_name = ImageTk.PhotoImage(resized_model_name)
    model_name_display = canvas.create_image(200, 435, image=new_model_name, anchor=tk.NW)

    conversation_text = Image.open("user_window_elements/conversation_text.png")
    resized_conversation_text = conversation_text.resize((450,50))
    new_conversation_text = ImageTk.PhotoImage(resized_conversation_text)
    conversation_text_display = canvas.create_image(150, 515, image=new_conversation_text, anchor=tk.NW)

    conversation_text_2 = Image.open("user_window_elements/conversation_text_2.png")
    resized_conversation_text_2 = conversation_text_2.resize((450,50))
    new_conversation_text_2 = ImageTk.PhotoImage(resized_conversation_text_2)
    conversation_text_2_display = canvas.create_image(610, 515, image=new_conversation_text_2, anchor=tk.NW)

    #cursor events of the buttons
    def enter():
        canvas.config(cursor="hand2")

    def leave():
        canvas.config(cursor="")

    #user window buttons
    submit_button = Image.open("user_window_buttons/submit_button.png")
    resized_submit_button = submit_button.resize((150,50))
    new_submit_button = ImageTk.PhotoImage(resized_submit_button)
    submit_button_display = canvas.create_image(700, 575, image=new_submit_button, anchor=tk.NW, tag = tagname)
    canvas.tag_bind(submit_button_display, "<Button-1>", emu_conversation)
    
    back_button = Image.open("user_window_buttons/back_button.png")
    resized_back_button = back_button.resize((150,50))
    new_back_button = ImageTk.PhotoImage(resized_back_button)
    back_button_display = canvas.create_image(350, 575, image=new_back_button, anchor=tk.NW, tag = tagname)
    canvas.tag_bind(back_button_display, "<Button-1>", back_to_main)

    canvas.tag_bind(tagname, "<Enter>", lambda event: enter())
    canvas.tag_bind(tagname, "<Leave>", lambda event: leave())

    user_window.mainloop()

def exit_window(event):
    main_window.destroy()

#primary_display
main_window = tk.Tk()
main_window.title("Emu finds the largest number!!!")
WIDTH = 1150
HEIGTH = 690
canvas = Canvas(main_window, width=WIDTH, height= HEIGTH)
canvas.pack()
main_window.resizable(False,False)

#main window elements
bg_img = Image.open("main_window_elements/emu_bg_final.png")
resized = bg_img.resize((1150,690))
new_bg_img = ImageTk.PhotoImage(resized)
bg_img_canvas = canvas.create_image(0, 0, image= new_bg_img, anchor=tk.NW)

text_blur = Image.open("main_window_elements/text_blur.png")
resized_text_blur = text_blur.resize((540,200))
new_text_blur = ImageTk.PhotoImage(resized_text_blur)
new_text_blur_display = canvas.create_image(300, 230, image = new_text_blur)

photo_title = Image.open("main_window_elements/main_title_1.png")
resized_title = photo_title.resize((400,50))
new_photo_title = ImageTk.PhotoImage(resized_title)
title_display = canvas.create_image(300, 200, image = new_photo_title)

photo_title_2 = Image.open("main_window_elements/main_title_2.png")
resized_title_2 = photo_title_2.resize((540,50))
new_photo_title_2 = ImageTk.PhotoImage(resized_title_2)
title_display_2 = canvas.create_image(300, 250, image = new_photo_title_2)

#cursor event of the buttons
def enter():
    canvas.config(cursor="hand2")

def leave():
    canvas.config(cursor="")

#main window buttons
tagname = "event"
start_button = Image.open("main_window_buttons/start_button.png")
resized_start_button = start_button.resize((230,75))
new_start_button = ImageTk.PhotoImage(resized_start_button)
start = canvas.create_image(300, 400, image= new_start_button, tag = tagname)
canvas.tag_bind(start, "<Button-1>", user_input_three_numbers)

exit_button = Image.open("main_window_buttons/exit_button.png")
resized_exit_button = exit_button.resize((170,60))
new_exit_button = ImageTk.PhotoImage(resized_exit_button)
exit = canvas.create_image(300, 500, image= new_exit_button, tag = tagname)
canvas.tag_bind(exit, "<Button-1>", exit_window)
canvas.tag_bind(tagname, "<Enter>", lambda event: enter())
canvas.tag_bind(tagname, "<Leave>", lambda event: leave())

emu_welcome_bgm()

main_window.mainloop()