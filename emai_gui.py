import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSenderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Email Sender")
        self.master.geometry("600x300")  # Adjusted size for better visibility
        self.master.configure(bg="#f0f8ff")  # Light blue background color

        # Left side - To, Subject, Send Button
        self.label_to = tk.Label(self.master, text="To:", bg="#7AB6D1", font=("Helvetica", 12))
        self.label_to.grid(row=0, column=0, padx=10, pady=10, sticky="w")  # Adjusted position to the left
        self.entry_to = tk.Entry(self.master, width=40, font=("Helvetica", 12))
        self.entry_to.grid(row=0, column=1, padx=10, pady=10)  # Adjusted position to the left

        self.label_subject = tk.Label(self.master, text="Subject:", bg="#7AB6D1", font=("Helvetica", 12))
        self.label_subject.grid(row=1, column=0, padx=10, pady=10, sticky="w")  # Adjusted position to the left
        self.entry_subject = tk.Entry(self.master, width=40, font=("Helvetica", 12))
        self.entry_subject.grid(row=1, column=1, padx=10, pady=10)  # Adjusted position to the left

        self.button_send = tk.Button(self.master, text="Send", command=self.send_email, bg="#add8e6", fg="#ffffff", font=("Helvetica", 12, "bold"))
        self.button_send.grid(row=2, column=1, padx=10, pady=10, sticky="e")  # Adjusted position to the left

        # Right side - Body Text
        self.label_body = tk.Label(self.master, text="Body:", bg="#7AB6D1", font=("Helvetica", 12))
        self.label_body.grid(row=0, column=2, padx=10, pady=10, sticky="w")  # Adjusted position to the right
        self.text_body = tk.Text(self.master, width=40, height=10, font=("Helvetica", 12))
        self.text_body.grid(row=1, column=2, padx=10, pady=10, rowspan=2)  # Adjusted position to the right

    def send_email(self):
        recipient = self.entry_to.get()
        subject = self.entry_subject.get()
        body = self.text_body.get("1.0", "end")

        try:
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            sender_email = "ashraddhansh@gmail.com"
            password = "pgkq qiyu hmjf ndwh"

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, recipient, message.as_string())

            messagebox.showinfo("Success", "Email sent successfully!")

            self.clear_input_fields()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def clear_input_fields(self):
        self.entry_to.delete(0, 'end')
        self.entry_subject.delete(0, 'end')
        self.text_body.delete('1.0', 'end')

def main():
    root = tk.Tk()
    app = EmailSenderApp(root)
    root.geometry('900x400')  # Adjusted size for better visibility
    root.configure(background="#7AB6D1")
    root.mainloop()

if __name__ == "__main__":
    main()
