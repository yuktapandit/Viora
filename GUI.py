from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action


def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, "User--->" + user_val + "\n")   
    if bot_val != None:
        text.insert(END, "BOT <---" + str(bot_val) + "\n")
    if bot_val == "Okay!! Nice meeting you. Have a good day":
        root.destroy()
    if bot_val == "Good Bye!!!":
        root.destroy()
    
def delete():
    text.delete('1.0', "end")

def send():
    send = user_prompt.get("1.0", "end").strip()
    bot = action.Action(send)
    text.insert(END, "User--->" + send + "\n")
    if bot != None:
        text.insert(END, "BOT <---" + str(bot) + "\n")
    if bot == "Okay!! Nice meeting you. Have a good day":
        root.destroy()
    if bot == "Good Bye!!!":
        root.destroy()
    

    
def on_hover(e):
    e.widget.config(bg="#E64A19", relief = "raised")
    
def on_leave(e):
    e.widget.config(bg="#FF6F61", relief = "flat")
    
def on_click(e):
    e.widget.config(relief = "raised")
    
def on_release(e):
    e.widget.config(relief = "sunken")


root = Tk()
root.title("VIORA")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg = "#FFE5D4")   #light peach color


frame = LabelFrame(root, padx=120, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#FFE5D4")
frame.grid(row=0, column=1, padx=55, pady=10)

text_label = Label(frame, text="VIORA", font=("Montserrat", 20, "bold"), fg="#D35400", bg="#FFE5D4")
text_label.grid(row=0, column=0, padx=20, pady=10)

img = Image.open("image/ai-chatbot2.png")
img_width = 205
img_height = 205
resized_img= img.resize((img_width, img_height), Image.LANCZOS)
img = ImageTk.PhotoImage(resized_img)

img_label = Label(frame, image=img, bg="#FFE5D4")
img_label.grid(row=1, column=0, pady=20)

# adding text widget
text = Text(root, font=("Roboto 12 bold"), fg="#333333", bg="#FFE5B4", borderwidth=3, relief="raised")
text.grid(row=2, column=0)
text.place(x=100, y=350, width=375, height=135)

user_prompt = Text(root, font=("Roboto 12"), fg="#4A4A4A", bg="#EFEFEF")
user_prompt.place(x=100, y=500, width=375, height=70)

#adding buttons
btn_ask = Button(root, text="ASK", fg="#333333", bg="#FF6F61", 
                 padx=40, pady=15, borderwidth=3, relief="solid", 
                 activebackground="#E64A19", command=ask)
btn_ask.place(x=50, y=590)
btn_ask.bind("<Enter>", on_hover)
btn_ask.bind("<Leave>", on_leave)
btn_ask.bind("<ButtonPress-1>", on_click)
btn_ask.bind("<ButtonRelease-1>", on_release)

btn_delete = Button(root, text="DELETE", fg="#333333", bg="#FF6F61", 
                 padx=40, pady=15, borderwidth=3, relief="solid", 
                 activebackground="#E64A19", command=delete)
btn_delete.place(x=210, y=590)
btn_delete.bind("<Enter>", on_hover)
btn_delete.bind("<Leave>", on_leave)
btn_delete.bind("<ButtonPress-1>", on_click)
btn_delete.bind("<ButtonRelease-1>", on_release)

btn_send = Button(root, text="SEND", fg="#333333", bg="#FF6F61", 
                 padx=40, pady=15, borderwidth=3, relief="solid", 
                 activebackground="#E64A19", command=send)
btn_send.place(x=390, y=590)
btn_send.bind("<Enter>", on_hover)
btn_send.bind("<Leave>", on_leave)
btn_send.bind("<ButtonPress-1>", on_click)
btn_send.bind("<ButtonRelease-1>", on_release)

root.mainloop()
