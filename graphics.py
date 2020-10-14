#This program creates a graphical user interface for 2-player Rock, Paper, Scissors
import random
import tkinter as tk
from tkmacosx import Button
import tkinter.font as tkFont
from instructions import rules_heading, welcome_message, how_to_win_1, how_to_win_2, how_to_win_3

#Configure root window and font styles
root = tk.Tk()
root.geometry("500x300")
root.title("Rock, Paper, Scissors!")
root.configure(bg="#21b6b6", borderwidth=2, relief="solid")
font_heading= tkFont.Font(family="Verdana", size=18, weight="bold")
font_sub_heading= tkFont.Font(family="Verdana", size=15, weight="bold")
font_result_heading= tkFont.Font(family="Verdana", size=12, slant="italic", weight="bold")
font_body= tkFont.Font(family="Verdana", size=10, weight="normal")

#Welcome Screen Messages
tk.Label(root, text= welcome_message, font=font_heading, bg="#21b6b6", fg="#000000").place(x = 60, y=10)
tk.Label(root, text= rules_heading, font=font_sub_heading, padx=10, pady=10, borderwidth=2, relief="groove", bg="#a6e1e1", fg="#000000").place(x=60, y=45)
tk.Label(root, text= how_to_win_1, font=font_body, bg="#21b6b6", fg="#000000").place(x=10, y=100)
tk.Label(root, text= how_to_win_2, font=font_body, bg="#21b6b6", fg="#000000").place(x=185, y=100)
tk.Label(root, text= how_to_win_3, font=font_body, bg="#21b6b6", fg="#000000").place(x=340, y=100)

#Set Global Variables to Hold User and Computer Choice
user_score = 0
computer_score = 0
user_choice = ''
computer_choice = ''

#Define what happens when you press rock, paper, scissors
def random_computer_choice():
    """Computer picks a random choice"""
    return random.choice([1,2,3]) 

def press_rock():
    """What happens when User presses rock button"""
    global user_choice
    global computer_choice
    user_choice = 1
    computer_choice =random_computer_choice()
    check_win(user_choice, computer_choice) 

def press_paper():
    """What happens when User presses paper button"""
    global user_choice
    global computer_choice
    user_choice = 2
    computer_choice =random_computer_choice()
    check_win(user_choice, computer_choice) 

def press_scissors():
    """What happens when User presses scissors button"""
    global user_choice
    global computer_choice
    user_choice = 3
    computer_choice =random_computer_choice()
    check_win(user_choice, computer_choice) 

#Check Win & Display Results
def check_win(user_choice, computer_choice):
    global user_score
    global computer_score
    if user_choice == computer_choice:
        result = "It's a tie"
        
    elif user_choice == computer_choice -1:
        result = "Computer wins!"
        computer_score += 1
        
    elif computer_choice == user_choice -1:
        result = "You Win!"
        user_score += 1
        
    elif user_choice == 1 and computer_choice == 3:
        result = "You Win!"
        user_score +=1
        
    elif computer_choice == 1 and user_choice == 3:
        result = "Computer Wins!"
        computer_score +=1
    
    text_area = tk.Text(master=root,height=2,width=20, borderwidth=2, relief="groove", bg="#a6e1e1", fg="#000000")
    text_area.place(x=318, y=252)
    answer = f" Your Score : {user_score} \n Computer Score : {computer_score} "
    text_area.insert(tk.END,answer)
    
    text_area_2 = tk.Text(master=root,height=1,width=20, font=font_result_heading, borderwidth=2, relief="groove", bg="#a6e1e1")
    text_area_2.place(x=15, y=258)
    score = f"   Result: {result} "
    text_area_2.insert(tk.END,score)

#Design Buttons on Main Screen
rock_button = Button(root, text= "Rock", font=font_sub_heading, padx= 25, pady= 30, bg= "#b62121", fg= "white", command= press_rock).place(x=10, y=150)
paper_button = Button(root, text= "Paper", font=font_sub_heading, padx= 25, pady= 30, bg= "#b6b621", command= press_paper).place(x=169, y=150)
scissors_button = Button(root, text= "Scissors", font=font_sub_heading, padx= 25, pady= 30, bg= "#157575", fg= "white", command= press_scissors).place(x=330, y=150)

#Continuous Loop for App
root.mainloop()