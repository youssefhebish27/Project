import tkinter as tk
import pyttsx3
def play_text():
    text = text_entry.get()
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def exit_program():
    root.quit()
def clear_text():
    text_entry.delete(0, "end")
root = tk.Tk()
root.title("Text to Speech")
root.geometry("400x300")

header = tk.Label(root, text="Text to Speech", font=("Arial", 20 ,"bold"))
header.pack(pady=10)

sub_header = tk.Label(root, text="Enter your text below:", font=("Arial", 12))
sub_header.pack()

text_entry = tk.Entry(root, width=25, font=("Arial", 14), justify="center")
text_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

play_button = tk.Button(button_frame, text="Play",font=("Arial", 12, "bold"), width=7, command=play_text)
play_button.grid(row=0,column=0, padx=10)

set_button = tk.Button(button_frame, text="Set", font=("Arial", 12, "bold"),width=7, command=clear_text)
set_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 12, "bold"), width=7, command=exit_program)
exit_button.grid(row=0, column=2, padx=10)

root.mainloop()