import tkinter as tk
from tkinter import messagebox
import time
import random

# FLAMES options and their meanings
flames_meaning = {
    "F": "Friends",
    "L": "Love",
    "A": "Affection",
    "M": "Marriage",
    "E": "Enemy",
    "S": "Siblings"
}

def calculate_relationship(player1, player2):
    player1_clean = player1.lower().replace(" ", "")
    player2_clean = player2.lower().replace(" ", "")

    # Count frequency of characters in both names
    player1_freq = {char: player1_clean.count(char) for char in set(player1_clean)}
    player2_freq = {char: player2_clean.count(char) for char in set(player2_clean)}

    # Calculate total characters
    total_chars = sum(player1_freq.values()) + sum(player2_freq.values())

    # Calculate FLAMES result index
    flames_index = total_chars % len(flames_meaning)

    return list(flames_meaning.keys())[flames_index]

def display_relationship_status(player1, player2):
    relationship_key = calculate_relationship(player1, player2)
    relationship_status = flames_meaning[relationship_key]

    result_message = f"Based on the names '{player1}' and '{player2}':\n"
    result_message += f"Relationship status: {relationship_status}\n\n"

    # Personalized messages based on relationship status
    if relationship_key == "F":
        result_message += f"Congratulations! You have a good chance of being great friends."
    elif relationship_key == "L":
        result_message += f"Wow! Looks like there could be some romantic sparks between you."
    elif relationship_key == "A":
        result_message += f"Sweet! Affection is definitely in the air."
    elif relationship_key == "M":
        result_message += f"Interesting! Marriage might be in the cards for you two."
    elif relationship_key == "E":
        result_message += f"Oops! Watch out, there might be some friction or rivalry."
    elif relationship_key == "S":
        result_message += f"Aww! You two might share a sibling-like bond."

    messagebox.showinfo("Relationship Status", result_message)

def validate_and_display():
    player1 = entry_player1.get().strip()
    player2 = entry_player2.get().strip()

    if not player1 or not player2:
        messagebox.showerror("Error", "Please enter both names.")
        return

    display_relationship_status(player1, player2)

def clear_entries():
    entry_player1.delete(0, tk.END)
    entry_player2.delete(0, tk.END)

# Create tkinter window
window = tk.Tk()
window.title("FLAMES Relationship Calculator")

# Create GUI elements
label_instructions = tk.Label(window, text="Enter names to check relationship status:")
label_instructions.pack(pady=10)

frame_names = tk.Frame(window)
frame_names.pack(padx=20, pady=10)

label_player1 = tk.Label(frame_names, text="Player 1:")
label_player1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

entry_player1 = tk.Entry(frame_names)
entry_player1.grid(row=0, column=1, padx=5, pady=5)

label_player2 = tk.Label(frame_names, text="Player 2:")
label_player2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)

entry_player2 = tk.Entry(frame_names)
entry_player2.grid(row=1, column=1, padx=5, pady=5)

button_check = tk.Button(window, text="Check Relationship", command=validate_and_display)
button_check.pack(pady=10)

button_clear = tk.Button(window, text="Clear Entries", command=clear_entries)
button_clear.pack(pady=5)

# Start the tkinter main loop
window.mainloop()
