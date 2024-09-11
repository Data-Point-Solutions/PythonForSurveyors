import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        side1 = side1_entry.get()
        side2 = side2_entry.get()
        area_acres = area_entry.get()

        if calc_mode.get() == "area":
            # Calculate area in acres when both sides are provided
            side1 = float(side1)
            side2 = float(side2)
            
            if side1 <= 0 or side2 <= 0:
                raise ValueError("Both sides must be positive numbers.")
                
            area_sq_ft = side1 * side2
            area_acres = area_sq_ft / 43560
            result_label.config(text=f"The area is: {area_acres:.4f} acres")

        elif calc_mode.get() == "side":
            # Calculate the missing side when one side and area are provided
            side1 = float(side1)
            area_acres = float(area_acres)
            
            if side1 <= 0 or area_acres <= 0:
                raise ValueError("Side and area must be positive numbers.")

            area_sq_ft = area_acres * 43560
            side2 = area_sq_ft / side1
            result_label.config(text=f"The other side is: {side2:.2f} feet")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def update_fields():
    if calc_mode.get() == "area":
        side2_entry.config(state="normal")
        area_entry.config(state="disabled")
    elif calc_mode.get() == "side":
        side2_entry.config(state="disabled")
        area_entry.config(state="normal")

# Create the main window
root = tk.Tk()
root.title("Rectangle Calculator")

calc_mode = tk.StringVar(value="side")

# Radio buttons to select mode
tk.Radiobutton(root, text="Calculate Area", variable=calc_mode, value="area", command=update_fields).grid(row=0, column=0, columnspan=2)
tk.Radiobutton(root, text="Calculate Side", variable=calc_mode, value="side", command=update_fields).grid(row=0, column=2, columnspan=2)

# Entries for sides and area
tk.Label(root, text="Side 1 (feet):").grid(row=1, column=0, padx=10, pady=10)
side1_entry = tk.Entry(root)
side1_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Side 2 (feet):").grid(row=2, column=0, padx=10, pady=10)
side2_entry = tk.Entry(root)
side2_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Area (acres):").grid(row=3, column=0, padx=10, pady=10)
area_entry = tk.Entry(root)
area_entry.grid(row=3, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Result display
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Set initial state
update_fields()

# Run the application
root.mainloop()
