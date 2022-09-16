from tkinter import *
from PIL import Image, ImageTk
import random


def shake():
    """Generate result of shaking eight-ball."""
    options = [
        ("It is certain", "green"),
        ("It is decidedly so", "green"),
        ("Without a doubt", "green"),
        ("Yes, definitely", "green"),
        ("You may rely on it", "green"),
        ("As I see it, yes", "green"),
        ("Most likely", "green"),
        ("Outlook good", "green"),
        ("Yes", "green"),
        ("Signs point to yes", "green"),
        ("Reply hazy try again", "yellow"),
        ("Ask again later", "yellow"),
        ("Better not tell you now", "yellow"),
        ("Cannot predict now", "yellow"),
        ("Concentrate and ask again", "yellow"),
        ("Don't count on it", "red"),
        ("My reply is no", "red"),
        ("My sources say no", "red"),
        ("Outlook not so good", "red"),
        ("Very doubtful", "red")
    ]
    # Shuffle list to get random order.
    random.shuffle(options)
    # Display first result in shuffled list.
    result.config(text=options[0][0], fg=options[0][1])


root = Tk()
root.configure(bg="black")

# Display magic eight-ball image.
img = ImageTk.PhotoImage(Image.open("magic_8_ball.png"))
eight_ball = Label(root, image=img)
eight_ball.pack()

# Label to display result of "shaking" eight ball.
result = Label(root, pady=10, bg="black", text="", font=("gothic bold", 14))
result.pack()

# "Shake" eight ball.
shake_button = Button(root, pady=10, text="Shake", width=10,
                      bg="red", fg="white", command=shake)
shake_button.pack()

root.mainloop()
