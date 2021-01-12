
import tkinter as tk
from pathlib import Path

ghost_evidence_list = ["None", "EMF Level 5", "FingersPrints", "Freezing Temperature", "Ghost Orbs", "Ghost Writing", "Sprit Box"]

window = tk.Tk()

background_image = tk.PhotoImage(file = "images/paper-texture.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

window.title("Evidence Journal")
window.geometry("350x400")
tk.Label(window, text="Evidence", font=("Helvetica", 24)).pack()

# Ghost Name
ghost_name_frame = tk.Frame(window)

tk.Label(ghost_name_frame, text="Ghost's Name", font=("Helvetica", 16)).pack()
ghost_name_box = tk.Text(ghost_name_frame, width=20, height=1, font=("Helvetica", 16) )
ghost_name_box.pack()

ghost_name_frame.pack(pady=10) # Can give these pady and padx to move in frame

# Evidence
evidence_frame = tk.Frame(window)

tk.Label(evidence_frame, text="Evidence Found #1", font=("Helvetica", 16)).pack()
evidence_1 = tk.StringVar(evidence_frame)
evidence_1.set(ghost_evidence_list[0]) # Default
evidence_1_options = tk.OptionMenu(evidence_frame, evidence_1, *ghost_evidence_list)
evidence_1_options.pack(pady=10)

tk.Label(evidence_frame, text="Evidence Found #2", font=("Helvetica", 16)).pack()
evidence_2 = tk.StringVar(evidence_frame)
evidence_2.set(ghost_evidence_list[0]) # Default
evidence_2_options = tk.OptionMenu(evidence_frame, evidence_2, *ghost_evidence_list)
evidence_2_options.pack(pady=10)

tk.Label(evidence_frame, text="Evidence Found #3", font=("Helvetica", 16)).pack()
evidence_3 = tk.StringVar(evidence_frame)
evidence_3.set(ghost_evidence_list[0]) # Default
evidence_3_options = tk.OptionMenu(evidence_frame, evidence_3, *ghost_evidence_list)
evidence_3_options.pack(pady=10)

evidence_frame.pack()

# Clear Function
def clear():
    ghost_name_box.delete(1.0, tk.END)
    evidence_1.set(ghost_evidence_list[0])
    evidence_2.set(ghost_evidence_list[0])
    evidence_3.set(ghost_evidence_list[0])

# Button
button_frame = tk.Frame(window)
button_frame.pack()

clear_button = tk.Button(button_frame, text="Clear", font=("Helvetica", 12), command=clear)
clear_button.pack()

window.mainloop()
