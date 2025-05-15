#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# reaction_timer_game/main.py

import tkinter as tk
import time
import random

class ReactionGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Reaction Timer Game")
        self.root.geometry("400x300")
        self.root.configure(bg='gray')

        self.label = tk.Label(root, text="Click 'Start' to play", font=("Arial", 16), bg='gray')
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_game, font=("Arial", 14))
        self.start_button.pack(pady=10)

        self.root.bind('<Button-1>', self.record_click)

        self.game_running = False
        self.waiting_to_click = False
        self.start_time = 0

    def start_game(self):
        self.label.config(text="Wait for green...", bg='gray')
        self.root.configure(bg='gray')
        self.start_button.config(state='disabled')
        self.game_running = True
        self.waiting_to_click = False

        delay = random.randint(2000, 5000)  # 2 to 5 seconds
        self.root.after(delay, self.show_green_screen)

    def show_green_screen(self):
        if self.game_running:
            self.root.configure(bg='green')
            self.label.config(text="CLICK NOW!", bg='green')
            self.start_time = time.time()
            self.waiting_to_click = True

    def record_click(self, event):
        if self.game_running and self.waiting_to_click:
            reaction_time = round((time.time() - self.start_time) * 1000)
            self.label.config(text=f"Reaction Time: {reaction_time} ms")
            self.root.configure(bg='gray')
            self.start_button.config(state='normal')
            self.waiting_to_click = False
            self.game_running = False
        elif self.game_running and not self.waiting_to_click:
            self.label.config(text="Too soon! Wait for green.")
            self.start_button.config(state='normal')
            self.root.configure(bg='gray')
            self.game_running = False

if __name__ == "__main__":
    root = tk.Tk()
    game = ReactionGame(root)
    root.mainloop()

