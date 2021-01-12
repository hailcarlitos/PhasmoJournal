import tkinter as tk

# Ghost Evidence List
ghost_evidence_list = ["None", "EMF Level 5", "Fingers Prints", "Freezing Temperature", "Ghost Orbs", "Ghost Writing", "Sprit Box"]

# Font Definitions
segoe24 = ("Segoe Print", 24)
segoe20 = ("Segoe Print", 20)
segoe16 = ("Segoe Print", 16)

# Basic
root = tk.Tk()
root.title("Phasmophobia Journal")
root.geometry("350x450")
root.resizable(False, False)

# Define Background Image
bg = tk.PhotoImage(file="images/paper-texture.png")

# Create a Canvas
my_canvas = tk.Canvas(root, width=350, height=450)
my_canvas.pack(fill="both", expand=True)

# Set image in Canvas
my_canvas.create_image(0, 0, image=bg, anchor="nw")

# Title Text
my_canvas.create_text( 175, 25, text="Evidence", font=segoe24)

# Ghost Name
my_canvas.create_text( 175, 60, text="Ghost Name", font=segoe20)
ghost_name_textbox = tk.Text(root, width=20, height=1, font=segoe16 )
ghost_name_window = my_canvas.create_window(175, 100, window=ghost_name_textbox)

# Evidence
my_canvas.create_text(175, 150, text="Evidence Found #1", font=segoe20 )
evidence_1 = tk.StringVar(root)
evidence_1.set(ghost_evidence_list[0]) # Default
evidence_1_options = tk.OptionMenu(root, evidence_1, *ghost_evidence_list)
evidence_1_options.config(font=segoe16)
evidence_1_window = my_canvas.create_window(175, 190, window=evidence_1_options)

my_canvas.create_text(175, 240, text="Evidence Found #2", font=segoe20)
evidence_2 = tk.StringVar(root)
evidence_2.set(ghost_evidence_list[0]) # Default
evidence_2_options = tk.OptionMenu(root, evidence_2, *ghost_evidence_list)
evidence_2_options.config(font=segoe16)
evidence_2_window = my_canvas.create_window(175, 280, window=evidence_2_options)

my_canvas.create_text(175, 330, text="Evidence Found #3", font=segoe20)
evidence_3 = tk.StringVar(root)
evidence_3.set(ghost_evidence_list[0]) # Default
evidence_3_options = tk.OptionMenu(root, evidence_3, *ghost_evidence_list)
evidence_3_options.config(font=segoe16)
evidence_3_window = my_canvas.create_window(175, 370, window=evidence_3_options)


# Clear Function
def clear():
    ghost_name_textbox.delete(1.0, tk.END)
    evidence_1.set(ghost_evidence_list[0])
    evidence_2.set(ghost_evidence_list[0])
    evidence_3.set(ghost_evidence_list[0])


clear_button = tk.Button(root, text="Clear", font=("Helvetica", 12), command=clear)
clear_window = my_canvas.create_window(50, 420, window=clear_button)

root.mainloop()
