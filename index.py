import tkinter as tk
from tkinter import messagebox

# Dictionary of countries and their capitals
country_capital = {
    'USA': 'Washington, D.C.',
    'Canada': 'Ottawa',
    'Japan': 'Tokyo',
    'Germany': 'Berlin',
    'France': 'Paris',
    'India': 'New Delhi',
    'Brazil': 'Brasilia',
    'Australia': 'Canberra',
    'China': 'Beijing',
    'Russia': 'Moscow'
}

class DragDropGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Country-Capital Matching Game")

        self.countries = list(country_capital.keys())
        self.capitals = list(country_capital.values())
        
        self.create_widgets()
        self.shuffle_capitals()

    def create_widgets(self):
        # Create a canvas for the background image
        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack()

        # Load and set the background image
        # self.background_image = tk.PhotoImage(file="./earth.jpg")  # Use your image file here
        # self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        # Create country labels
        self.country_labels = []
        for country in self.countries:
            label = tk.Label(self.canvas, text=country, font=("Arial", 16), bg='lightblue')
            self.canvas.create_window(100, len(self.country_labels) * 40 + 50, window=label)
            label.bind("<Button-1>", self.start_drag)
            label.bind("<B1-Motion>", self.do_drag)
            label.bind("<ButtonRelease-1>", self.end_drag)
            self.country_labels.append(label)

        # Create capital labels
        self.capital_labels = []
        for capital in self.capitals:
            label = tk.Label(self.canvas, text=capital, font=("Arial", 16), bg='lightgreen')
            self.canvas.create_window(400, len(self.capital_labels) * 40 + 50, window=label)
            label.bind("<Button-1>", self.start_drag)
            label.bind("<B1-Motion>", self.do_drag)
            label.bind("<ButtonRelease-1>", self.end_drag)
            self.capital_labels.append(label)

    def shuffle_capitals(self):
        import random
        random.shuffle(self.capitals)
        for i, label in enumerate(self.capital_labels):
            label.config(text=self.capitals[i])

    def start_drag(self, event):
        widget = event.widget
        widget._drag_data = {"x": event.x, "y": event.y}

    def do_drag(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget._drag_data["x"] + event.x
        y = widget.winfo_y() - widget._drag_data["y"] + event.y
        widget.place(x=x, y=y)

    def end_drag(self, event):
        widget = event.widget
        for country_label in self.country_labels:
            if widget.winfo_x() >= country_label.winfo_x() and \
               widget.winfo_x() <= country_label.winfo_x() + country_label.winfo_width() and \
               widget.winfo_y() >= country_label.winfo_y() and \
               widget.winfo_y() <= country_label.winfo_y() + country_label.winfo_height():
                # Check if the capital matches the country
                country_name = country_label['text']
                capital_name = widget['text']
                if country_capital[country_name] == capital_name:
                    messagebox.showinfo("Correct!", f"{capital_name} is the capital of {country_name}!")
                else:
                    messagebox.showinfo("Try Again!", f"{capital_name} is not the capital of {country_name}.")
                widget.place(x=0, y=0)  # Reset position
                break
        else:
            widget.place(x=0, y=0)  # Reset position if not dropped on any country

class StartPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Start Page")

        label = tk.Label(self.master, text="Welcome to the Country-Capital Matching Game!", font=("Arial", 24))
        label.pack(pady=20)

        start_button = tk.Button(self.master, text="Start Game", font=("Arial", 16), command=self.start_game)
        start_button.pack(pady=20)

    def start_game(self):
        self.master.destroy()  # Close the start page
        game_window = tk.Tk()  # Create a new window for the game
        game = DragDropGame(game_window)
        game_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    start_page = StartPage(root)
    root.mainloop()
