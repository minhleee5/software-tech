#tkinter
import tkinter as tk

#window
root = tk.Tk()
root.geometry("400x400")
root.title("My GUI")

#widgets
name_label = tk.Label(root, text="Name:")
age_label = tk.Label(root, text="Age: ")

#entry
name_entry = tk.Entry(root)
age_entry = tk.Entry(root)

#button
submit_button = tk.Button(root, text="Submit")
#pack
# name_label.pack()
# name_entry.pack()
# age_label.pack()
# age_entry.pack()

#grid
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry.grid(row=0, column=1, padx=10, pady=10)
age_label.grid(row=1, column=0, padx=10, pady=10)
age_entry.grid(row=1, column=1, padx=10, pady=10)
submit_button.grid(row=2, columnspan=2)
#main loop
root.mainloop()