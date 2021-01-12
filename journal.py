import tkinter as tk

# Ghost Evidence List
ghost_evidence_list = ["None", "EMF Level 5", "Fingers Prints", "Freezing Temperature", "Ghost Orbs", "Ghost Writing", "Sprit Box"]

# Font Definitions and colors
segoe24 = ("Segoe Print", 24)
segoe20 = ("Segoe Print", 20)
segoe16 = ("Segoe Print", 16)
segoe12 = ("Segoe Print", 12)
box_bg = "#D4C79B"

# Functions for buttons
# For clearing the ghost name and found eveidence
def clear():
    ghost_name_textbox.delete(1.0, tk.END)
    evidence_1.set(ghost_evidence_list[0])
    evidence_2.set(ghost_evidence_list[0])
    evidence_3.set(ghost_evidence_list[0])

# For toggleing between who the ghost talks to Everyone and Alone
def toggle(tog=[0]):
    tog[0] = not tog[0]
    if tog[0]:
        spirit_box_button.config(text="E")
    else:
        spirit_box_button.config(text="A")

# Basic
root = tk.Tk()
root.title("Phasmophobia Journal")
root.geometry("350x480")
root.resizable(False, False)

# Define Background Image and line for Title
bg = tk.PhotoImage(file="images/paper-texture.png")
line = tk.PhotoImage(file="images/line.png")

# Create a Canvas
my_canvas = tk.Canvas(root, width=350, height=480)
my_canvas.pack(fill="both", expand=True)

# Set back ground image in Canvas
my_canvas.create_image(0, 0, image=bg, anchor="nw")

# Title Text
my_canvas.create_text( 175, 25, text="Evidence Journal", font=segoe24)
my_canvas.create_image(175, 60, image=line)

# Ghost Name
my_canvas.create_text( 175, 90, text="Ghost Name", font=segoe20)
ghost_name_textbox = tk.Text(root, width=18, height=1, font=segoe16, bg=box_bg)
ghost_name_textbox.tag_configure("center", justify='center')
ghost_name_textbox.insert(1.0, " ")
ghost_name_textbox.tag_add("center", "1.0", "end")
ghost_name_window = my_canvas.create_window(150, 130, window=ghost_name_textbox)

# Sprit box button net to Ghost name
spirit_box_button = tk.Button(root, text="A", font=segoe12, bg=box_bg, command=toggle)
spirit_box_window = my_canvas.create_window(310, 130, window=spirit_box_button)

# Evidence
my_canvas.create_text(175, 180, text="Evidence Found #1", font=segoe20 )
evidence_1 = tk.StringVar(root)
evidence_1.set(ghost_evidence_list[0]) # Default
evidence_1_options = tk.OptionMenu(root, evidence_1, *ghost_evidence_list)
evidence_1_options.config(font=segoe16, bg=box_bg)
evidence_1_window = my_canvas.create_window(175, 225, window=evidence_1_options)

my_canvas.create_text(175, 275, text="Evidence Found #2", font=segoe20)
evidence_2 = tk.StringVar(root)
evidence_2.set(ghost_evidence_list[0]) # Default
evidence_2_options = tk.OptionMenu(root, evidence_2, *ghost_evidence_list)
evidence_2_options.config(font=segoe16, bg=box_bg)
evidence_2_window = my_canvas.create_window(175, 320, window=evidence_2_options)

my_canvas.create_text(175, 370, text="Evidence Found #3", font=segoe20)
evidence_3 = tk.StringVar(root)
evidence_3.set(ghost_evidence_list[0]) # Default
evidence_3_options = tk.OptionMenu(root, evidence_3, *ghost_evidence_list)
evidence_3_options.config(font=segoe16, bg=box_bg)
evidence_3_window = my_canvas.create_window(175, 415, window=evidence_3_options)


# Clear Function and Button


clear_button = tk.Button(root, text="Clear", font=("Helvetica", 12), command=clear)
clear_window = my_canvas.create_window(40, 460, window=clear_button)


# Main loop for window
root.mainloop()
