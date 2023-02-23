import random
import tkinter as tk


class WheelOfNames:
    def __init__(self, names):
        self.print_names = names.copy()
        self.names = modify_names(names)
        self.win = tk.Tk()
        self.win.title("Wheel of Names")
        self.win.geometry("500x500")

        # Create a canvas for drawing the wheel
        self.canvas = tk.Canvas(self.win, width=400, height=400)
        self.canvas.pack()

        # Draw the wheel
        colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
        start_angle = 0
        arc_angle = 360 / len(names)
        self.arcs = []
        self.texts = []
        for i, name in enumerate(names):
            end_angle = start_angle + arc_angle
            color = colors[i % len(colors)]
            arc = self.canvas.create_arc(
                50,
                50,
                350,
                350,
                start=start_angle,
                extent=arc_angle,
                fill=color,
                outline="black",
            )
            text = self.canvas.create_text(
                200, 200, text=name, angle=start_angle + arc_angle / 2, fill="white"
            )
            self.arcs.append(arc)
            self.texts.append(text)
            start_angle = end_angle

        # Add a spin button
        spin_button = tk.Button(self.win, text="SPIN", command=self.spin)
        spin_button.pack()

        # create label for winner
        self.winner_label = tk.Label(self.win, text="", font=("Arial", 16, "bold"))
        self.winner_label.pack(pady=10)

    def spin(self):
        # Choose a random duration between 3 and 6 seconds
        duration = random.uniform(3, 7)

        # Choose a random name to land on
        selected_name = random.choice(self.names)
        selected_index = self.names.index(selected_name)

        # Calculate the number of color changes and the delay between each change
        delay = 20  # milliseconds
        num_steps = int(duration * 1000 / delay)  # amount of steps to complete spin

        # Spin the wheel
        for i in range(num_steps):
            # Calculate the arc index that should be highlighted
            arc_index = (selected_index + i) % len(self.names)

            # Update the fill color of the arcs and the text color
            for j in range(len(self.names)):
                color = "gold" if j == arc_index else "gray"
                self.canvas.itemconfig(self.arcs[j], fill=color)
                self.canvas.itemconfig(self.texts[j], fill="white")

            # Schedule the next color change
            self.canvas.after(delay)
            self.canvas.update()

        # display winner
        print(self.print_names[arc_index])
        self.winner_label.config(text=f"Congratulations {self.print_names[arc_index]}!")


def modify_names(names):
    # Modify names
    for idx in range(len(names)):
        name = " " * 50 + names[idx]
        if len(name) > 60:
            names[idx] = name[:60] + "..."
        else:
            names[idx] = name

    return names


if __name__ == "__main__":
    with open("names.txt", "r") as f:
        names = f.read().splitlines()
    wheel = WheelOfNames(names)
    wheel.win.mainloop()
