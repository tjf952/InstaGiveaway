import random
import tkinter as tk


class WheelOfNames:
    def __init__(self, names):
        self.names = names
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
        for i, name in enumerate(names):
            end_angle = start_angle + arc_angle
            color = colors[i % len(colors)]
            self.canvas.create_arc(
                50,
                50,
                350,
                350,
                start=start_angle,
                extent=arc_angle,
                fill=color,
                outline="black",
            )
            self.canvas.create_text(
                200,
                200,
                text=" " * 50 + name,
                angle=start_angle + arc_angle / 2,
                fill="white",
            )
            start_angle = end_angle

        # Add a spin button
        spin_button = tk.Button(self.win, text="SPIN", command=self.spin)
        spin_button.pack()

    def spin(self):
        # Randomly select a name and highlight it
        selected_name = random.choice(self.names)
        start_angle = 0
        arc_angle = 360 / len(self.names)
        for i, name in enumerate(self.names):
            end_angle = start_angle + arc_angle
            if name == selected_name:
                color = "gold"
            else:
                color = "gray"
            self.canvas.create_arc(
                50,
                50,
                350,
                350,
                start=start_angle,
                extent=arc_angle,
                fill=color,
                outline="black",
            )
            self.canvas.create_text(
                200,
                200,
                text=" " * 50 + name,
                angle=start_angle + arc_angle / 2,
                fill="white",
            )
            start_angle = end_angle


if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
    wheel = WheelOfNames(names)
    wheel.win.mainloop()
