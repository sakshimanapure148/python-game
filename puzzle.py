import tkinter as tk
from tkinter import messagebox
import random

class PuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Puzzle Game")
        self.root.geometry("400x400")

        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 0]

        # Solvable shuffle ke liye valid moves karte hain
        self.shuffle_puzzle()

        self.buttons = []

        for i in range(9):
            btn = tk.Button(
                root,
                font=("Arial", 24, "bold"),
                command=lambda i=i: self.move_tile(i)
            )

            btn.grid(
                row=i // 3,
                column=i % 3,
                sticky="nsew",
                padx=3,
                pady=3
            )

            self.buttons.append(btn)

        for i in range(3):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

        self.update_buttons()

    def shuffle_puzzle(self):
        for _ in range(100):
            empty_index = self.numbers.index(0)

            empty_row = empty_index // 3
            empty_col = empty_index % 3

            possible_moves = []

            for i in range(9):
                row = i // 3
                col = i % 3

                distance = abs(row - empty_row) + abs(col - empty_col)

                if distance == 1:
                    possible_moves.append(i)

            move_index = random.choice(possible_moves)

            self.numbers[empty_index], self.numbers[move_index] = (
                self.numbers[move_index],
                self.numbers[empty_index]
            )

    def update_buttons(self):
        for i in range(9):
            if self.numbers[i] == 0:
                self.buttons[i].config(text="")
            else:
                self.buttons[i].config(text=str(self.numbers[i]))

    def move_tile(self, clicked_index):
        empty_index = self.numbers.index(0)

        clicked_row = clicked_index // 3
        clicked_col = clicked_index % 3

        empty_row = empty_index // 3
        empty_col = empty_index % 3

        distance = abs(clicked_row - empty_row) + abs(clicked_col - empty_col)

        if distance == 1:
            self.numbers[clicked_index], self.numbers[empty_index] = (
                self.numbers[empty_index],
                self.numbers[clicked_index]
            )

            self.update_buttons()
            self.check_win()

    def check_win(self):
        if self.numbers == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            messagebox.showinfo(
                "Winner",
                "Congratulations! Puzzle Solve Ho Gaya 🎉"
            )

root = tk.Tk()
game = PuzzleGame(root)
root.mainloop()