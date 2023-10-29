import webbrowser
import urllib.parse
import tkinter as tk
from tkinter import font

# Function to handle button click
def submit_item():
    name = entry.get()
    if name.lower() == 'quit':
        root.destroy()
    else:
        encoded_name = urllib.parse.quote(name)
        print('Encoded Name:', encoded_name)
        url = "https://backpack.tf/classifieds?item=%s" % (encoded_name)
        webbrowser.open(url, new=2)

def submit_item_std():
    name = entry.get()
    if name.lower() == 'quit':
        root.destroy()
    else:
        encoded_name = urllib.parse.quote(name)
        print('Encoded Name:', encoded_name)
        url = f"https://stntrading.eu/item/tf2/{encoded_name}"
        webbrowser.open(url, new=2)

def submit_item_stm():
    name = entry.get()
    if name.lower() == 'quit':
        root.destroy()
    else:
        encoded_name = urllib.parse.quote(name)
        print('Encoded Name:', encoded_name)
        url = f"https://steamcommunity.com/market/listings/440/{encoded_name}"
        webbrowser.open(url, new=2)

# Function to handle auto-suggest
def autosuggest(event):
    search_text = entry.get()
    matches = []
    with open('list.txt', 'r') as file:
        items = file.readlines()
        for item in items:
            if search_text.lower() in item.lower():
                matches.append(item.strip())
    if matches:
        listbox.delete(0, tk.END)
        for match in matches:
            listbox.insert(tk.END, match)

# Function to handle listbox selection
def select_item(event):
    selected_item = listbox.get(listbox.curselection())
    entry.delete(0, tk.END)
    entry.insert(tk.END, selected_item)

# Create the main window
root = tk.Tk()
root.title("Item Finder By Phattaraphum")
root.geometry("500x350")  # Set window size to 300x300
root.minsize(500, 350)   # Set minimum window size to 300x300
root.maxsize(500, 350)   # Set maximum window size to 300x300
root.attributes("-topmost", True)

# Create a text box
entry = tk.Entry(root, width=80)
entry.pack(pady=10)
entry.bind("<KeyRelease>", autosuggest)

# Create a listbox for auto-suggest
listbox = tk.Listbox(root, width=80)
listbox.pack()

# Create a font with bold style
bold_font = font.nametofont("TkDefaultFont").copy()
bold_font.configure(weight="bold")

# Create a submit button with green background color, larger size, bold text, and white text color
submit_button = tk.Button(root, text="GO TO BP.TF", command=submit_item, bg="green", height=2, width=20, pady=1, font=bold_font, fg="white")
submit_button.pack()

# Duplicate the submit button with the same properties, bold text, and white text color
submit_button2 = tk.Button(root, text="GO TO STD", command=submit_item_std, bg="blue", height=2, width=20, pady=1, font=bold_font, fg="white")
submit_button2.pack()

submit_button3 = tk.Button(root, text="GO TO STEAM", command=submit_item_stm, bg="red", height=2, width=20, pady=1, font=bold_font, fg="white")
submit_button3.pack()

# Bind the listbox selection event to the select_item function
listbox.bind("<Double-Button-1>", select_item)

root.mainloop()
