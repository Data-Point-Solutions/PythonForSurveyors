# File path: dms_dd_converter_lat_long_selector.py

import tkinter as tk
from tkinter import messagebox

def dms_to_dd(degrees, minutes, seconds, direction):
    """Converts DMS (Degrees, Minutes, Seconds) to Decimal Degrees (DD)."""
    dd = float(degrees) + float(minutes) / 60 + float(seconds) / 3600
    if direction in ['S', 'W']:
        dd *= -1
    return dd

def dd_to_dms(dd):
    """Converts Decimal Degrees (DD) to DMS (Degrees, Minutes, Seconds)."""
    is_negative = dd < 0
    dd = abs(dd)
    degrees = int(dd)
    minutes = int((dd - degrees) * 60)
    seconds = round((dd - degrees - minutes / 60) * 3600, 6)  # 6 decimal places for seconds
    direction = 'S' if is_negative else 'N'  # Default to 'N' for latitudes
    if degrees >= 90:  # Assuming longitude input
        direction = 'W' if is_negative else 'E'
    return degrees, minutes, seconds, direction

def validate_input(value):
    """Validates that the input is not empty and is a valid number."""
    try:
        return float(value.strip())  # Remove any leading/trailing spaces and convert to float
    except ValueError:
        raise ValueError("Invalid input: please enter numeric values only.")

def convert_dms_to_dd():
    try:
        # Latitude
        lat_deg = validate_input(lat_dms_deg_entry.get())
        lat_min = validate_input(lat_dms_min_entry.get())
        lat_sec = validate_input(lat_dms_sec_entry.get())
        lat_dir = lat_dms_dir_entry.get().upper().strip()

        # Longitude
        lon_deg = validate_input(lon_dms_deg_entry.get())
        lon_min = validate_input(lon_dms_min_entry.get())
        lon_sec = validate_input(lon_dms_sec_entry.get())
        lon_dir = lon_dms_dir_entry.get().upper().strip()

        # Validate directions
        if lat_dir not in ['N', 'S'] or lon_dir not in ['E', 'W']:
            raise ValueError("Invalid direction! Use N/S for latitude and E/W for longitude.")

        # Convert to DD
        lat_dd = dms_to_dd(lat_deg, lat_min, lat_sec, lat_dir)
        lon_dd = dms_to_dd(lon_deg, lon_min, lon_sec, lon_dir)

        # Display DD to 9 decimal places
        dd_result_label.config(text=f"Lat: {lat_dd:.9f}, Lon: {lon_dd:.9f}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def convert_dd_to_dms():
    try:
        # Latitude
        lat_dd = validate_input(lat_dd_entry.get())

        # Longitude
        lon_dd = validate_input(lon_dd_entry.get())

        # Convert to DMS
        lat_dms = dd_to_dms(lat_dd)
        lon_dms = dd_to_dms(lon_dd)

        # Display DMS with seconds to 6 decimal places
        lat_dms_result = f"{lat_dms[0]}° {lat_dms[1]}' {lat_dms[2]:.6f}\" {lat_dms[3]}"
        lon_dms_result = f"{lon_dms[0]}° {lon_dms[1]}' {lon_dms[2]:.6f}\" {lon_dms[3]}"
        
        dms_result_label.config(text=f"Lat: {lat_dms_result}, Lon: {lon_dms_result}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def update_input_mode():
    """Updates input fields based on selected conversion mode."""
    if mode.get() == "DMS to DD":
        # Enable DMS fields
        lat_dms_deg_entry.config(state='normal')
        lat_dms_min_entry.config(state='normal')
        lat_dms_sec_entry.config(state='normal')
        lat_dms_dir_entry.config(state='normal')
        lon_dms_deg_entry.config(state='normal')
        lon_dms_min_entry.config(state='normal')
        lon_dms_sec_entry.config(state='normal')
        lon_dms_dir_entry.config(state='normal')
        # Disable DD fields
        lat_dd_entry.config(state='disabled')
        lon_dd_entry.config(state='disabled')
    else:
        # Enable DD fields
        lat_dd_entry.config(state='normal')
        lon_dd_entry.config(state='normal')
        # Disable DMS fields
        lat_dms_deg_entry.config(state='disabled')
        lat_dms_min_entry.config(state='disabled')
        lat_dms_sec_entry.config(state='disabled')
        lat_dms_dir_entry.config(state='disabled')
        lon_dms_deg_entry.config(state='disabled')
        lon_dms_min_entry.config(state='disabled')
        lon_dms_sec_entry.config(state='disabled')
        lon_dms_dir_entry.config(state='disabled')

# GUI setup
root = tk.Tk()
root.title("DMS to DD Converter (Lat/Long)")

# Mode selection
mode = tk.StringVar(value="DMS to DD")
tk.Radiobutton(root, text="DMS to DD", variable=mode, value="DMS to DD", command=update_input_mode).grid(row=0, column=0, columnspan=2)
tk.Radiobutton(root, text="DD to DMS", variable=mode, value="DD to DMS", command=update_input_mode).grid(row=0, column=2, columnspan=2)

# DMS to DD Conversion Section
tk.Label(root, text="DMS to DD Conversion").grid(row=1, column=0, columnspan=4)

# Latitude DMS input
tk.Label(root, text="Lat Degrees:").grid(row=2, column=0)
lat_dms_deg_entry = tk.Entry(root)
lat_dms_deg_entry.grid(row=2, column=1)

tk.Label(root, text="Minutes:").grid(row=3, column=0)
lat_dms_min_entry = tk.Entry(root)
lat_dms_min_entry.grid(row=3, column=1)

tk.Label(root, text="Seconds:").grid(row=4, column=0)
lat_dms_sec_entry = tk.Entry(root)
lat_dms_sec_entry.grid(row=4, column=1)

tk.Label(root, text="Direction (N/S):").grid(row=5, column=0)
lat_dms_dir_entry = tk.Entry(root)
lat_dms_dir_entry.grid(row=5, column=1)

# Longitude DMS input
tk.Label(root, text="Lon Degrees:").grid(row=2, column=2)
lon_dms_deg_entry = tk.Entry(root)
lon_dms_deg_entry.grid(row=2, column=3)

tk.Label(root, text="Minutes:").grid(row=3, column=2)
lon_dms_min_entry = tk.Entry(root)
lon_dms_min_entry.grid(row=3, column=3)

tk.Label(root, text="Seconds:").grid(row=4, column=2)
lon_dms_sec_entry = tk.Entry(root)
lon_dms_sec_entry.grid(row=4, column=3)

tk.Label(root, text="Direction (E/W):").grid(row=5, column=2)
lon_dms_dir_entry = tk.Entry(root)
lon_dms_dir_entry.grid(row=5, column=3)

# Convert DMS to DD Button
convert_dms_button = tk.Button(root, text="Convert to DD", command=convert_dms_to_dd)
convert_dms_button.grid(row=6, column=0, columnspan=4)

# DMS to DD Result
dd_result_label = tk.Label(root, text="Decimal Degrees: ")
dd_result_label.grid(row=7, column=0, columnspan=4)

# DD to DMS Conversion Section
tk.Label(root, text="DD to DMS Conversion").grid(row=8, column=0, columnspan=4)

# Latitude DD input
tk.Label(root, text="Lat Decimal Degrees:").grid(row=9, column=0)
lat_dd_entry = tk.Entry(root)
lat_dd_entry.grid(row=9, column=1)

# Longitude DD input
tk.Label(root, text="Lon Decimal Degrees:").grid(row=9, column=2)
lon_dd_entry = tk.Entry(root)
lon_dd_entry.grid(row=9, column=3)

# Convert DD to DMS Button
convert_dd_button = tk.Button(root, text="Convert to DMS", command=convert_dd_to_dms)
convert_dd_button.grid(row=10, column=0, columnspan=4)

# DD to DMS Result
dms_result_label = tk.Label(root, text="DMS: ")
dms_result_label.grid(row=11, column=0, columnspan=4)

# Initialize input fields
update_input_mode()

# Start the GUI event loop
root.mainloop()
