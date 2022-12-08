
# importing the necessary libraries
import string
import tkinter as tk
import customtkinter as ctk
from tkinter import *
from tkinter import ttk
import numpy as np

# setting the correct and incorrect counters
counter = 0
correct_counter = 0
# initialising a blank list to store guesses
all_guesses = []



def clear_widgets(frame):
    'this function destroys all the widgets on the specified frame'
    # select all frame widgets and delete them
    for widget in frame.winfo_children():
        widget.destroy()



def load_main():
    ''' This function loads the main screen'''
    # sets some global variables so they can be used in other functions
    global userinput
    global input1
    global word
    global wordlist
    global underscores
    #gets the inputted word
    word = input1.get()
    # turns it into a list
    wordlist = list(word)
    # starts  a list of underscores for each letter with spaces in betwen
    underscores = ' '.join(['_' for i in range(len(word))])
    
    #clears all other frames
    clear_widgets(wordinput)
    clear_widgets(main)
    clear_widgets(third)
    clear_widgets(gameover)
    #raises the main frame
    main.tkraise()
    
    
    
    # adds a label 
    tk.Label(main, text="Guess A Letter",bg=background,
        fg="blue",
        font=("Rockwell", 20)
        ).place(rely=0.4,relx=0.8,anchor=CENTER)
    
    # user entry box for letter entry
    userinput = ctk.CTkEntry(
    main)
    userinput.place(rely=0.3,relx=0.8, anchor=CENTER)
    
    # guess button which runs guess function
    ctk.CTkButton(
    main,
    text="GUESS",
        
        #bg="#28393a",
        font=("Rockwell",30),
        command=lambda: guess()
        ).place(rely=0.8,relx=0.8, anchor=CENTER)
    
    # label which fills out with the underscores list
    tk.Label(main, text=underscores,bg=background,
        fg="blue",
        font=("Rockwell", 20)
        ).place(rely=0.8,relx=0.3,anchor=CENTER)



def load_wordinput():
    '''This function loads the input screen'''
    global input1
    #clears other screens
    clear_widgets(main)
    clear_widgets(third)
    clear_widgets(win)
    clear_widgets(gameover)
    # raises the wordinput frame
    wordinput.tkraise()
    #adds label
    tk.Label(wordinput, text="Player 1: Input a Word",bg=background,
        fg="blue",
        font=("Rockwell", 20)
        ).place(rely=0.3,relx=0.5,anchor=CENTER)
    # adds input box for word
    input1 = ctk.CTkEntry(wordinput)
    input1.place(rely=0.4,relx=0.5, anchor=CENTER)
    # button that loads main screen
    ctk.CTkButton(
    wordinput,
    text="INPUT",
        
        #bg="#28393a",
        font=("Rockwell",30),
        command=lambda: load_main()
        ).place(rely=0.8,relx=0.5, anchor=CENTER)

def load_third():
    ''' This function loads the third screen'''
    global userinput
    global counter
    clear_widgets(wordinput)
    clear_widgets(main)
    clear_widgets(third)
    third.tkraise()
    
    
    
    # adds a label 
    tk.Label(third, text="Guess A Letter",bg=background,
        fg="blue",
        font=("Rockwell", 20)
        ).place(rely=0.4,relx=0.8,anchor=CENTER)
    
    # user entry box
    userinput = ctk.CTkEntry(
    third)
    userinput.place(rely=0.3,relx=0.8, anchor=CENTER)
    
    # guess button which runs guess function
    ctk.CTkButton(
    third,
    text="GUESS",
        
        #bg="#28393a",
        font=("Rockwell",30),
        command=lambda: guess()
        ).place(rely=0.8,relx=0.8, anchor=CENTER)
    
    # label which shows remaining underscores but with filled letters if there are any
    tk.Label(third, text=underscores,bg=background,
        fg="blue",
        font=("Rockwell", 30)
        ).place(rely=0.8,relx=0.35,anchor=CENTER)
    
    # label which displays all previous guesses
    tk.Label(third, text=' '.join(all_guesses),bg=background,
        fg="blue",
        font=("Rockwell", 20)
        ).place(rely=0.2,relx=0.3,anchor=CENTER)
    
    #this checks how many wrong guesses there are and decides which hangman image to load
    if 0 < counter < 8:
        img = PhotoImage(file=f"./hangmanpythonimages/Picture{counter}.gif")
        img = img.subsample(2)
        logo = tk.Label(third, image=img,bg=background)
        logo.image = img
        logo.place(relx=0.35,rely=0.5,anchor=CENTER)
    elif counter == 8:
        img = PhotoImage(file=f"./hangmanpythonimages/Picture{counter}.gif")
        img = img.subsample(2)
        logo = tk.Label(third, image=img,bg=background)
        logo.image = img
        logo.place(relx=0.35,rely=0.5,anchor=CENTER)
        load_gameover()
    # checks the correct counter and decides if they have won    
    if (correct_counter >= len(set(word)) - 1) and (guessed_letter in wordlist):
        load_win()


def guess():
    '''This function runs when a guess is made'''
    # global variables
    global underscores
    global counter
    global correct_counter
    global guessed_letter
    global all_guesses
    # gets the user inputted letter
    guessed_letter = userinput.get()
    # clears the entry box
    clear_text()
    # checks if the letter is in the word
    if guessed_letter in wordlist:
        #converts the wordlist to an array
        vals = np.array(wordlist)
        # finds where guessed letter is in the list
        where = np.where(vals == guessed_letter)[0]
        where = [where[i] for i in range(len(where))]
        # splits the underscores and replaces with the guessed letter
        for j in where:
            usplit = underscores.split(' ')
            usplit[j] = guessed_letter
            underscores = ' '.join(usplit)
        #loads third screen and increases correct counter
        load_third()
        correct_counter +=1
    else:
        #if not correct then increases incorrect counter
        counter +=1
        # appends to the guesses list
        all_guesses.append(guessed_letter)
        #loads third screen
        load_third()
        


def load_win():
    #clears widgets frim other screens
    clear_widgets(wordinput)
    clear_widgets(main)
    clear_widgets(third)
    # raises win screen
    win.tkraise()
    # tells them they got it
    tk.Label(third, text='You Got It',bg=background,
    fg="blue",
    font=("Rockwell", 40)
    ).place(rely=0.2,relx=0.5,anchor=CENTER)
    
    # asks to play again. runs play_again() function
    ctk.CTkButton(
    win,
    text="PLAY AGAIN?",
        
        #bg="#28393a",
        font=("Rockwell",40),
        command=lambda: play_again()
        ).pack(padx=20,pady=20)
    
    # gives option to quit
    ctk.CTkButton(
    win,
    text="EXIT",
        
        #bg="#28393a",
        font=("Rockwell",40),
        command=window.destroy
        ).pack(padx=20,pady=20)



def load_gameover():
    global word
    #clears widgets from selected screens
    clear_widgets(wordinput)
    clear_widgets(main)
    gameover.tkraise()
    
    # adds label telling what the word was
    tk.Label(gameover, text=f'Game Over. The Word Was {word}',bg=background,
    fg="red",
    font=("Rockwell", 30)
    ).pack(padx=20,pady=20)
    
    # play again button running play_again() function
    ctk.CTkButton(
    gameover,
    text="PLAY AGAIN?",
        
        #bg="#28393a",
        font=("Rockwell",40),
        command=lambda: play_again()
        ).pack(padx=20,pady=20)
    
    # gives option to quit
    ctk.CTkButton(
    gameover,
    text="EXIT",
        
        #bg="#28393a",
        font=("Rockwell",40),
        command=window.destroy
        ).pack(padx=20,pady=20)



def clear_text():
    '''this function deletes user input'''
    userinput.delete(0, END)




def play_again():
    '''This function runs if the user'''
    global counter
    global correct_counter
    global all_guesses
    #resets the correct counter
    correct_counter = 0
    #resets incorrect counter
    counter = 0
    #resets the list of guesses
    all_guesses = []
    #loads the input screen
    load_wordinput()

    
# this initialises the UI settings
background='#FAF9F6'
ctk.set_appearance_mode('Light')
ctk.set_default_color_theme('dark-blue')

# this initialises tkinter
window = ctk.CTk()
window.title("Hangman")
window.geometry("1200x500+10+10")

#this defines the 4 frames
main = tk.Frame(window, width=1800, height=1000, bg=background)
wordinput = tk.Frame(window, width=1800, height=1000, bg=background)
third = tk.Frame(window, width=1800, height=1000, bg=background)
win = tk.Frame(window, width=1800, height=1000, bg=background)
gameover = tk.Frame(window, width=1800, height=1000, bg=background)


# place frame widgets in window
for frame in (main, wordinput,third,win,gameover):
    frame.place(rely=0.5,relx=0.5, anchor = CENTER)
# load the main frame
load_wordinput()

#runs the window
window.mainloop()
