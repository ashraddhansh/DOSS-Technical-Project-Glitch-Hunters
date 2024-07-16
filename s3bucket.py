import tkinter as tk
from tkinter import filedialog, messagebox
import boto3

class S3UploaderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("S3 File Uploader")
        self.master.configure(background='#f0f0f0')
        
        self.s3 = boto3.client('s3')
        self.bucket_name = "arpitbucketweb"
        
        # Frame for buttons
        self.button_frame = tk.Frame(self.master, bg='#E79D24')
        self.button_frame.pack(side=tk.LEFT, padx=50, pady=10)
        
        # Upload button
        self.upload_button = tk.Button(self.button_frame, text="Upload File", command=self.upload_file, bg='#4CAF50', fg='white', padx=20, pady=10)
        self.upload_button.pack(pady=5)

        # List button
        self.list_button = tk.Button(self.button_frame, text="List Files", command=self.list_files, bg='#008CBA', fg='white', padx=20, pady=10)
        self.list_button.pack(pady=5)

        # Frame for file list
        self.file_frame = tk.Frame(self.master, bg='#f0f0f0')
        self.file_frame.pack(side=tk.RIGHT, padx=10, pady=10)

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            file_name = file_path.split('/')[-1]
            try:
                self.s3.upload_file(file_path, self.bucket_name, file_name)
                messagebox.showinfo("Success", f"{file_name} uploaded successfully!")
                self.list_files()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to upload {file_name}: {str(e)}")

    def list_files(self):
        try:
            response = self.s3.list_objects_v2(Bucket=self.bucket_name)
            files = response.get('Contents', [])
            
            # Clear previous file list
            for widget in self.file_frame.winfo_children():
                widget.destroy()
            
            # Display files
            for file_info in files:
                file_name = file_info['Key']
                file_size = file_info['Size']
                file_last_modified = file_info['LastModified']
                
                file_frame = tk.Frame(self.file_frame, bg='#ffffff', bd=1, relief=tk.RIDGE)
                file_frame.pack(fill=tk.X, padx=5, pady=2)
                
                file_label = tk.Label(file_frame, text=file_name, bg='#ffffff', padx=10, pady=5)
                file_label.pack(side=tk.LEFT)
                
                size_label = tk.Label(file_frame, text=f"Size: {file_size} bytes", bg='#ffffff', padx=10, pady=5)
                size_label.pack(side=tk.LEFT)
                
                modified_label = tk.Label(file_frame, text=f"Last Modified: {file_last_modified}", bg='#ffffff', padx=10, pady=5)
                modified_label.pack(side=tk.LEFT)
                
                delete_button = tk.Button(file_frame, text="Delete", command=lambda name=file_name: self.delete_file(name), bg='#f44336', fg='white', padx=10, pady=5)
                delete_button.pack(side=tk.RIGHT)
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to list files: {str(e)}")

    def delete_file(self, file_name):
        try:
            self.s3.delete_object(Bucket=self.bucket_name, Key=file_name)
            messagebox.showinfo("Success", f"{file_name} deleted successfully!")
            self.list_files()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete {file_name}: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = S3UploaderApp(root)
    root.geometry('1200x800')
    root.configure(background="#E79D24")
    text_label = tk.Label(root, text="S3 Bucket Manager", fg='white', bg='#E79D24')
    text_label.pack(pady=(10, 10))
    text_label.config(font=("Vandana", 25))
    root.mainloop()
