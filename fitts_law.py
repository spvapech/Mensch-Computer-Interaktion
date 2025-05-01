import tkinter as tk
import time
import random
import math
import csv

# Parameter
WIDTH = 800
HEIGHT = 600
CIRCLE_DIAMETERS = [30, 60, 90]
DISTANCES = [100, 200, 300]
REPEATS = 3

class FittsLawApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()
        self.trials = [(d, dist) for d in CIRCLE_DIAMETERS for dist in DISTANCES for _ in range(REPEATS)]
        random.shuffle(self.trials)
        self.current_trial = 0
        self.start_time = None
        self.results = []
        self.circle_items = []
        self.phase = 0  # 0 = first circle, 1 = second circle
        self.master.title("Fitts's Law Experiment")
        self.draw_next_trial()
        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_next_trial(self):
        self.canvas.delete("all")
        if self.current_trial >= len(self.trials):
            self.save_results_to_csv()
            self.show_results()
            return

        d, dist = self.trials[self.current_trial]

        # Choose a random center for the first circle within bounds
        margin = max(CIRCLE_DIAMETERS)
        x1 = random.randint(margin, WIDTH - margin)
        y1 = random.randint(margin, HEIGHT - margin)

        # Compute second circle position
        angle = random.uniform(0, 2 * math.pi)
        x2 = int(x1 + math.cos(angle) * dist)
        y2 = int(y1 + math.sin(angle) * dist)

        # Keep second circle within bounds
        if not (margin <= x2 <= WIDTH - margin and margin <= y2 <= HEIGHT - margin):
            return self.draw_next_trial()  # retry

        self.circle_coords = [(x1, y1), (x2, y2)]
        self.diameter = d

        colors = ["blue", "red"]
        for i, (x, y) in enumerate(self.circle_coords):
            r = d // 2
            circle = self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=colors[i])
            self.circle_items.append(circle)

        self.phase = 0

    def handle_click(self, event):
        x, y = event.x, event.y
        cx, cy = self.circle_coords[self.phase]
        r = self.diameter / 2
        if (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2:
            if self.phase == 0:
                self.start_time = time.time()
                self.phase = 1
            else:
                reaction_time = time.time() - self.start_time
                d, dist = self.trials[self.current_trial]
                index_of_difficulty = math.log2(dist / d + 1)
                self.results.append((d, dist, round(index_of_difficulty, 3), reaction_time))
                self.current_trial += 1
                self.circle_items.clear()
                self.draw_next_trial()

    def show_results(self):
        self.canvas.delete("all")
        self.canvas.create_text(WIDTH//2, HEIGHT//2 - 20, text="Experiment beendet", font=("Arial", 24))
        for i, (d, dist, idf, t) in enumerate(self.results):
            print(f"Trial {i+1}: Diameter={d}, Distance={dist}, ID={idf}, Time={t:.3f}s")

    def save_results_to_csv(self):
        with open("fitts_law_results.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Trial", "Diameter", "Distance", "Index of Difficulty (ID)", "Time (s)"])
            for i, (d, dist, idf, t) in enumerate(self.results):
                writer.writerow([i + 1, d, dist, idf, round(t, 3)])

if __name__ == "__main__":
    root = tk.Tk()
    app = FittsLawApp(root)
    root.mainloop()