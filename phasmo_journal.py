
import tkinter as tk

ghost_evidence_list = ["None", "EMF Level 5", "FingersPrints", "Freezing Temperature", "Ghost Orbs", "Ghost Writing", "Sprit Box"]

window = tk.Tk()
window.title("Evidence Journal")
window.geometry("350x500")
tk.Label(window, text="Evidence", font=("Helvetica", 24)).pack()

ghost_name_frame = tk.Frame(window)

tk.Label(ghost_name_frame, text="Ghost's Name", font=("Helvetica", 16)).pack()
ghost_name_box = tk.Text(ghost_name_frame, width=20, height=1, font=("Helvetica", 16) )
ghost_name_box.pack()

ghost_name_frame.pack(pady=10) # Can give these pady and padx to move in frame

evidence_1_frame = tk.Frame(window)

tk.Label(evidence_1_frame, text="Evidence Found #1", font=("Helvetica", 16)).pack()
evidence_1 = tk.StringVar(evidence_1_frame)
evidence_1.set("None") # Default
evidence_1_options = tk.OptionMenu(evidence_1_frame, evidence_1, *ghost_evidence_list)
evidence_1_options.pack()

evidence_1_frame.pack(pady=10)

evidence_2_frame = tk.Frame(window)

tk.Label(evidence_2_frame, text="Evidence Found #2", font=("Helvetica", 16)).pack()
evidence_2 = tk.StringVar(evidence_2_frame)
evidence_2.set("None") # Default
evidence_2_options = tk.OptionMenu(evidence_2_frame, evidence_2, *ghost_evidence_list)
evidence_2_options.pack()

evidence_2_frame.pack(pady=10)

evidence_3_frame = tk.Frame(window)

tk.Label(evidence_3_frame, text="Evidence Found #3", font=("Helvetica", 16)).pack()
evidence_3 = tk.StringVar(evidence_3_frame)
evidence_3.set("None") # Default
evidence_3_options = tk.OptionMenu(evidence_3_frame, evidence_3, *ghost_evidence_list)
evidence_3_options.pack()

evidence_3_frame.pack(pady=10)

window.mainloop()
