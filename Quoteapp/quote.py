import tkinter as tk
from tkinter import messagebox
import datetime
import os
import pyperclip

# List of quotes
quotes = [
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "Your time is limited, so don't waste it living someone else's life.",
    "Not everything that is faced can be changed, but nothing can be changed until it is faced.",
    "The only way to do great work is to love what you do.",
    "Success is not the key to happiness. Happiness is the key to success."
]

class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inspiring Quotes")
        self.root.geometry("400x300")
        self.root.configure(bg="#ADD8E6")

        self.quote = self.get_today_quote()

        self.quote_label = tk.Label(root, text=self.quote, wraplength=350, justify="center", font=("Helvetica", 14), bg="#ADD8E6", fg="#000000")
        self.quote_label.pack(pady=20)

        self.share_button = tk.Button(root, text="Share Quote", command=lambda: self.share_quote(self.quote), bg="#4CAF50", fg="#FFFFFF", font=("Helvetica", 12))
        self.share_button.pack(pady=10)

        self.save_fav_button = tk.Button(root, text="Save as Favorite", command=lambda: self.save_favorite_quote(self.quote), bg="#4CAF50", fg="#FFFFFF", font=("Helvetica", 12))
        self.save_fav_button.pack(pady=10)

        self.view_fav_button = tk.Button(root, text="View Favorites", command=self.view_favorites, bg="#4CAF50", fg="#FFFFFF", font=("Helvetica", 12))
        self.view_fav_button.pack(pady=10)

    def get_today_quote(self):
        today = datetime.date.today()
        day_of_year = today.timetuple().tm_yday
        return quotes[day_of_year % len(quotes)]

    def share_quote(self, quote):
        pyperclip.copy(quote)
        messagebox.showinfo("Quote Shared", "The quote has been copied to your clipboard.")

    def save_favorite_quote(self, quote):
        with open("favorites.txt", "a") as file:
            file.write(quote + "\n")
        messagebox.showinfo("Favorite Saved", "The quote has been added to your favorites.")

    def load_favorite_quotes(self):
        if os.path.exists("favorites.txt"):
            with open("favorites.txt", "r") as file:
                return file.read().splitlines()
        return []

    def view_favorites(self):
        favorites = self.load_favorite_quotes()
        if not favorites:
            messagebox.showinfo("Favorites", "No favorite quotes saved.")
            return

        fav_window = tk.Toplevel(self.root)
        fav_window.title("Favorite Quotes")
        fav_window.geometry("400x300")
        fav_window.configure(bg="#ADD8E6")

        fav_label = tk.Label(fav_window, text="\n".join(favorites), wraplength=350, justify="left", font=("Helvetica", 12), bg="#ADD8E6", fg="#000000")
        fav_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteApp(root)
    root.mainloop()
