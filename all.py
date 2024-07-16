import tkinter as tk
import subprocess

def run_python_file(file_path):
    subprocess.Popen(['python', file_path])

def button1_clicked():
    run_python_file("./filter.py")

def button2_clicked():
    run_python_file("./latlon.py")

def button3_clicked():
    run_python_file("./emai_gui.py")

def button4_clicked():
    run_python_file("./webhost.py")

def button5_clicked():
    run_python_file("./s3bucket.py")

def button6_clicked():
    run_python_file("./awscontro.py")

def button7_clicked():
    run_python_file("./aico.py")

def button8_clicked():
    run_python_file("./drawcv.py")

# Create the main window
root = tk.Tk()
root.title("Run Python Files")
root.geometry("400x400")
root.configure(bg="light blue")

# Create top frame for the first 3 buttons
top_frame = tk.Frame(root, bg="light blue")
top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

button1 = tk.Button(top_frame, text="Camera", command=button1_clicked, bg="gray")
button1.pack(side=tk.LEFT, padx=10, pady=10)

button2 = tk.Button(top_frame, text="Lat/Log", command=button2_clicked, bg="gray")
button2.pack(side=tk.LEFT, padx=10, pady=10)

button3 = tk.Button(top_frame, text="Email", command=button3_clicked, bg="gray")
button3.pack(side=tk.LEFT, padx=10, pady=10)

button3 = tk.Button(top_frame, text="hand detection", command=button8_clicked, bg="gray")
button3.pack(side=tk.LEFT, padx=10, pady=10)

# Create bottom frame for the last 2 buttons
bottom_frame = tk.Frame(root, bg="light blue")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

button4 = tk.Button(bottom_frame, text="Website", command=button4_clicked, bg="gray")
button4.pack(side=tk.LEFT, padx=10, pady=10)

button5 = tk.Button(bottom_frame, text="S3 Bucket", command=button5_clicked, bg="gray")
button5.pack(side=tk.LEFT, padx=10, pady=10)

button6 = tk.Button(bottom_frame, text="AWS Control", command=button6_clicked, bg="gray")
button6.pack(side=tk.LEFT, padx=10, pady=10)

button7 = tk.Button(bottom_frame, text="Cohere AI", command=button7_clicked, bg="gray")
button7.pack(side=tk.LEFT, padx=10, pady=10)
# Run the GUI
root.mainloop()
