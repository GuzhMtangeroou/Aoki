import tkinter as tk
from tkinter import messagebox
import random
import hashlib
import struct

def generate_identifier(seed, additional_string):
    # Ensure the seed is a 4-digit integer
    if not (1000 <= seed <= 9999):
        raise ValueError("Seed must be a 4-digit integer.")
    
    # Ensure the additional string is 16 characters long by padding with '0' if necessary
    additional_string = additional_string.ljust(16, '0')
    
    # Pack the seed into bytes
    seed_bytes = struct.pack('>I', seed)[2:]  # We only need the last 2 bytes of a 4-byte int
    
    # Hash the additional string using SHA-256 and take the first 8 bytes
    hash_bytes = hashlib.sha256(additional_string.encode()).digest()[:8]
    
    # Generate random bytes for the rest of the identifier
    random_bytes = random.randbytes(6)  # We already have 8 bytes from the hash, so we need 6 more to make it 14 bytes total
    
    # Combine seed, hash, and random bytes
    combined_bytes = seed_bytes + hash_bytes + random_bytes
    
    # Convert bytes to hexadecimal string
    hex_string = combined_bytes.hex()
    
    # Format the string as "xxxx-xxxx-xxxxxxxx-xxxxxxxx-xxxx-xxxx"
    formatted_identifier = f"{hex_string[:4]}-{hex_string[4:8]}-{hex_string[8:16]}-{hex_string[16:24]}-{hex_string[24:28]}-{hex_string[28:32]}"
    
    return formatted_identifier

def on_generate():
    try:
        additional_string = entry_additional_string.get().strip()
        seed = 2502  # Fixed seed value
        identifier = generate_identifier(seed, additional_string)
        label_result.config(text=f"Generated Identifier: {identifier}")
        button_copy.config(state=tk.NORMAL)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def on_copy():
    try:
        identifier = label_result.cget("text").split(": ")[1]
        root.clipboard_clear()
        root.clipboard_append(identifier)
        messagebox.showinfo("Success", "Identifier copied to clipboard!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Identifier Generator and Extractor")

# Additional string input section
label_additional_string_input = tk.Label(root, text="Enter up to 16-character String (will be padded with '0' if less):")
label_additional_string_input.grid(row=0, column=0, padx=10, pady=5)

entry_additional_string = tk.Entry(root)
entry_additional_string.grid(row=0, column=1, padx=10, pady=5)

button_generate = tk.Button(root, text="Generate Identifier", command=on_generate)
button_generate.grid(row=0, column=2, padx=10, pady=5)

# Result display section
label_result = tk.Label(root, text="")
label_result.grid(row=1, columnspan=3, padx=10, pady=5)

# Copy button
button_copy = tk.Button(root, text="Copy Identifier", command=on_copy, state=tk.DISABLED)
button_copy.grid(row=2, columnspan=3, padx=10, pady=5)

# Start the GUI event loop
root.mainloop()