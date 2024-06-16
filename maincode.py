import tkinter as tk
import webbrowser
import smtplib
from tkinter import messagebox
import random
import string
import platform
from PIL import Image,ImageTk

system_name = platform.system()
if system_name == "Windows":
    hosts_path = r"C:/Windows/System32/drivers/etc/hosts"
elif system_name == "Linux" or system_name == "Darwin":  # macOS is a Unix-like system
    hosts_path = "/etc/hosts"
project_info_file = "project_info.html"
# Function to block website
def block_website(website):

    try:
        with open(hosts_path, "a") as hosts_file:
            hosts_file.write(f"\n127.0.0.1 {website}")
        messagebox.showinfo("success", f"Website {website} successfully blocked")
    except Exception as e:
        print(f"An error occurred while blocking website: {e}")

# Function to unblock website
def unblock_website(website):
    try:
        with open(hosts_path, "r+") as hosts_file:
            lines = hosts_file.readlines()
            hosts_file.seek(0)
            for line in lines:
                if not line.startswith("127.0.0.1") or website not in line:
                    hosts_file.write(line)
            hosts_file.truncate()
        messagebox.showinfo("success", f"Website {website} successfully unblocked")

    except Exception as e:
        print(f"An error occurred while unblocking website: {e}")

# Function to open block interface
def open_block_interface():
    block_window = tk.Toplevel(root)
    block_window.title("Block Website")
    block_window.geometry("500x200")
    block_window.configure(bg="#9EADC8")  # Set background color

    def block_website_action():
        website = website_entry.get()
        password = password_entry.get()  # Retrieve password
        if password == Password:  # Check password
            block_website(website)
            block_window.destroy()
        else:
            password_entry.delete(0, tk.END)  # Clear incorrect password
            tk.messagebox.showerror("Error", "Incorrect password. Please try again.",parent=block_window)

    website_label = tk.Label(block_window, text="Enter Website:", font=("Arial", 12, "bold"), bg="#9EADC8")  # Bold font and background color
    website_label.pack(pady=5)  # Add margin

    website_entry = tk.Entry(block_window, font=("Arial", 10), bd=2)  # Set font and border width
    website_entry.pack(pady=5)  # Add margin

    password_label = tk.Label(block_window, text="Enter Password:", font=("Arial", 12, "bold"), bg="#9EADC8")  # Bold font and background color
    password_label.pack(pady=5)  # Add margin

    password_entry = tk.Entry(block_window, show="*", font=("Arial", 10), bd=2)  # Set font, show asterisks for password, and border width
    password_entry.pack(pady=5)  # Add margin

    submit_button = tk.Button(block_window, text="Submit", command=block_website_action, font=("Arial", 12, "bold"), bg="#b9e28c")  # Bold font and background color
    submit_button.pack(pady=5)  # Add margin

# Function to open unblock interface
def open_unblock_interface():
    unblock_window = tk.Toplevel(root)
    unblock_window.title("Unblock Website")
    unblock_window.geometry("500x200")
    unblock_window.configure(bg="#9EADC8")  # Set background color

    def unblock_website_action():
        website = website_entry.get()
        password = password_entry.get()  # Retrieve password
        if password == Password:  # Check password
            unblock_website(website)
            unblock_window.destroy()
        else:
            password_entry.delete(0, tk.END)  # Clear incorrect password
            tk.messagebox.showerror("Error", "Incorrect password. Please try again.",parent=unblock_window)

    website_label = tk.Label(unblock_window, text="Enter Website:", font=("Arial", 12, "bold"), bg="#9EADC8")  # Bold font and background color
    website_label.pack(pady=5)  # Add margin

    website_entry = tk.Entry(unblock_window, font=("Arial", 10), bd=2)  # Set font and border width
    website_entry.pack(pady=5)  # Add margin

    password_label = tk.Label(unblock_window, text="Enter Password:", font=("Arial", 12, "bold"), bg="#9EADC8")  # Bold font and background color
    password_label.pack(pady=5)  # Add margin

    password_entry = tk.Entry(unblock_window, show="*", font=("Arial", 10), bd=2)  # Set font, show asterisks for password, and border width
    password_entry.pack(pady=5)  # Add margin

    submit_button = tk.Button(unblock_window, text="Submit", command=unblock_website_action, font=("Arial", 12, "bold"), bg="#b9e28c")  # Bold font and background color
    submit_button.pack(pady=5)  # Add margin

# Function to open project info
def open_project_info():
    project_window = tk.Toplevel(root)
    project_window.title("Project Info")
    project_window.geometry("500x200")
    project_window.configure(bg="#9EADC8")  # Set background color

    def open_in_browser():
        webbrowser.open(project_info_file)
    open_button = tk.Button(project_window, text="Open in Browser", command=open_in_browser, font=("Arial", 12, "bold"), bg="#b9e28c")  # Bold font and background color
    open_button.pack(expand=True,pady=50)  # Add margin

def open_blockpassword_interface():
    password_window = tk.Toplevel(frame)
    password_window.title("Generate password")
    password_window.geometry("500x200")
    password_window.configure(bg="pink")
    def generate_password():
        email = email_entry.get()
        if not email:
            messagebox.showerror("Error", "Please enter an email address.")
            return
        global Password
        Password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

        # SMTP configuration
        smtp_server = 'smtp.gmail.com'  #  SMTP server address
        smtp_port = 587  #  SMTP port
        smtp_username = '21kb1a0552@nbkrist.org'  #  email address
        smtp_password = '21kb1a0552'  #  email password

        try:
            # Establish SMTP connection
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)

            # Compose the email message
            message = f"Subject: Your Random Password\n\nYour random password is: {Password}"

            # Send email
            server.sendmail(smtp_username, email, message)
            server.quit()

            messagebox.showinfo("Success", f"Random password sent to {email}",parent=password_window)


        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {e}")
    email_label = tk.Label(password_window,text="Enter Email:",font=("Arial", 12, "bold"))
    email_label.pack(pady=10)

    email_entry = tk.Entry(password_window,font=("Arial", 10),bd=2,width=25)
    email_entry.pack(pady=10)

    password_button = tk.Button(password_window,text="Generate Password", font=("Arial", 10),command=generate_password)
    password_button.pack(pady=10)

    next_button = tk.Button(password_window, text="Next", font=("Arial", 10), command= lambda: [password_window.destroy(), open_block_interface()])
    next_button.pack(side="top", anchor="ne", padx=10, pady=10)

def open_unblockpassword_interface():
    password_window = tk.Toplevel(frame)
    password_window.title("Generate password")
    password_window.geometry("500x200")
    password_window.configure(bg="pink")
    def generate_password():
        email = email_entry.get()
        if not email:
            messagebox.showerror("Error", "Please enter an email address.")
            return
        global Password
        Password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

        # SMTP configuration
        smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server address
        smtp_port = 587  # Replace with your SMTP port
        smtp_username = '21kb1a0552@nbkrist.org'  # Replace with your email address
        smtp_password = '21kb1a0552'  # Replace with your email password

        try:
            # Establish SMTP connection
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)

            # Compose the email message
            message = f"Subject: Your Random Password\n\nYour random password is: {Password}"

            # Send email
            server.sendmail(smtp_username, email, message)
            server.quit()

            messagebox.showinfo("Success", f"Random password sent to {email}",parent=password_window)


        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {e}")
    email_label = tk.Label(password_window,text="Enter Email:",font=("Arial", 12, "bold"))
    email_label.pack(pady=10)

    email_entry = tk.Entry(password_window,font=("Arial", 10),bd=2,width=25)
    email_entry.pack(pady=10)

    password_button = tk.Button(password_window,text="Generate Password", font=("Arial", 10),command=generate_password)
    password_button.pack(pady=10)

    next_button = tk.Button(password_window, text="Next", font=("Arial", 10), command= lambda: [password_window.destroy(), open_unblock_interface()])
    next_button.pack(side="top", anchor="ne", padx=10, pady=10)



# Create main window
root = tk.Tk()
root.title("Website Blocker")
root.geometry("500x400")
root.configure(bg="#000000")  # Set background color

# Create Frame
frame = tk.Frame(root, bg="#000000")  # Set background color
frame.pack(expand=True,padx=10,pady=10)

info_button = tk.Button(frame, text="Project Info", command=open_project_info, font=("Arial", 14, "bold"), bg="#b9e28c",width=10)  # Bold font and background color
info_button.pack(expand=True,padx=10)# Add margin

lock_image = Image.open("Block-Websites.jpg")
lock_image = lock_image.resize((200, 200))
lock_image = ImageTk.PhotoImage(lock_image)
lock_label = tk.Label(frame,image=lock_image, bg="black")
lock_label.pack(pady=25)
# Block Button
block_button = tk.Button(frame, text="Block", command=open_blockpassword_interface, font=("Arial", 14, "bold"), bg="#b9e28c",width=10)  # Bold font and background color
block_button.pack(side='left', expand=True, padx=15, pady=5)  # Add margin

# Unblock Button
unblock_button = tk.Button(frame, text="Unblock", command=open_unblockpassword_interface, font=("Arial", 14, "bold"), bg="#b9e28c",width=10)  # Bold font and background color
unblock_button.pack(side='left', expand=True, padx=20, pady=5)  # Add margin


root.mainloop()
