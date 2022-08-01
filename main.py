from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

letters = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' ,
           's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' ,
           'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
numbers = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
symbols = ['!' , '#' , '$' , '%' , '&' , '(' , ')' , '*' , '+']

nr_letters = randint(8 , 10)
nr_symbols = randint(2 , 4)
nr_numbers = randint(2 , 4)


def generate_password():
    password_list = [choice(letters) for _ in range(nr_letters)] + \
                    [choice(symbols) for _ in range(nr_symbols)] + \
                    [choice(numbers) for _ in range(nr_numbers)]
    shuffle(password_list)
    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    third_entry.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = first_entry.get()
    mail = second_entry.get()
    password_details = third_entry.get()

    if len(website) == 0 or len(password_details) == 0 or len(mail) == 0:
        messagebox.showinfo(title="Oops" , message="Please do not leave any fields empty!")
    else:

        is_ok = messagebox.askokcancel(title=website ,
                                       message=f"These are the details entered: \n Email: {mail} \n Password: {password_details} \n Is it ok to save?")
        if is_ok:
            with open("data.txt" , "a") as file:
                file.write(f"{website} | {mail} | {password_details} \n")
                print(file)
                first_entry.delete(0 , END)
                second_entry.delete(0 , END)
                third_entry.delete(0 , END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50 , pady=50)

canvas = Canvas(width=200 , height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100 , 100 , image=lock_img)
canvas.grid(row=0 , column=1)

# labels
first_label = Label(text="Website:")
first_label.grid(row=1 , column=0)

second_label = Label(text="Email/Username:")
second_label.grid(row=2 , column=0)

third_label = Label(text="Password:")
third_label.grid(row=3 , column=0)

# entries
first_entry = Entry(width=35)
first_entry.grid(row=1 , column=1 , columnspan=2 , sticky="EW")
first_entry.focus()  # focus the cursor on that particular entry

second_entry = Entry(width=35)
second_entry.grid(row=2 , column=1 , columnspan=2 , sticky="EW")
second_entry.insert(0 , "johndoe@gmail.com")

third_entry = Entry(width=21)
third_entry.grid(row=3 , column=1 , sticky="EW")

# buttons

password_button = Button(text="Generate Password" , command=generate_password)
password_button.grid(row=3 , column=2 , sticky="EW")
#
add_button = Button(text="Add" , width=35 , command=save)
add_button.grid(row=4 , column=1 , columnspan=2 , sticky="EW")

window.mainloop()
