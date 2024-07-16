import tkinter as tk
import subprocess

class EC2ControlApp:
    def __init__(self, master):
        self.master = master
        master.title("Website Controller")
        master.geometry("400x400")

        self.heading_label = tk.Label(master, text="Website Controller", font=("Helvetica", 16))
        self.heading_label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start Instance", command=self.start_instance, bg="green", fg="white")
        self.start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=150, height=50)

        self.stop_button = tk.Button(master, text="Stop Instance", command=self.stop_instance, bg="red", fg="white")
        self.stop_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER, width=150, height=50)

    def start_instance(self):
        subprocess.call(["aws", "ec2", "start-instances", "--instance-ids", "i-059abb85ac6b6e6b2"])
        print("EC2 instance started.")

    def stop_instance(self):
        subprocess.call(["aws", "ec2", "stop-instances", "--instance-ids", "i-059abb85ac6b6e6b2"])
        print("EC2 instance stopped.")

root = tk.Tk()
app = EC2ControlApp(root)
root.mainloop()
