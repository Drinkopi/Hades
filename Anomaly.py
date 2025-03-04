import tkinter as tk
from tkinter import messagebox

class LoginUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.geometry("300x200")
        
        # Username
        self.username_label = tk.Label(self.window, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack(pady=5)
        
        # Password
        self.password_label = tk.Label(self.window, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack(pady=5)
        
        # Login button
        self.login_button = tk.Button(self.window, text="Login", command=self.login)
        self.login_button.pack(pady=20)
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Add your authentication logic here
        if username == "admin" and password == "password":
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    login_window = LoginUI()
    login_window.run()
