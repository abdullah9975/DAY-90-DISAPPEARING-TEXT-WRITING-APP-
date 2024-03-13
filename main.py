import tkinter as tk
import time


class DisappearingTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disappearing Text App")
        self.text_area = tk.Text(root, height=10, width=50)
        self.text_area.pack()
        self.text_area.bind("<Key>", self.start_timer)
        self.timer_running = False
        self.timer_start = None

    def start_timer(self, event):
        if not self.timer_running:
            self.timer_start = time.time()
            self.timer_running = True
            self.root.after(5000, self.check_timer)

    def check_timer(self):
        elapsed_time = time.time() - self.timer_start
        if elapsed_time >= 5:
            self.text_area.delete(1.0, tk.END)  # Delete all text
            self.timer_running = False
        else:
            self.root.after(1000, self.check_timer)  # Check again after 1 second


if __name__ == "__main__":
    root = tk.Tk()
    app = DisappearingTextApp(root)
    root.mainloop()
