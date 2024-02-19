import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Function to validate input
def validate_input(text):
    # Add your custom validation logic here
    # For example, check if text is empty or has specific format
    return True

# Function to save data to file
def save_data(name, email, phone):
    with open("Userdata.txt", "w") as file:
        file.write(f"Name: {name}\nEmail: {email}\nPhone: {phone}\n")
    print("Data saved successfully!")

# main window
app = ctk.CTk()
app.geometry("400x400")
app.title("User Data Collector")

# Add labels and entry fields
label = ctk.CTkLabel(master=app, text="Sign In Page", font = ("Roboto", 16))
label.pack(pady=12, padx=10)

name_label = ctk.CTkLabel(app, text="Name:")
name_label.pack(pady=10)
name_entry = ctk.CTkEntry(app, placeholder_text="Enter your name")
name_entry.pack()

email_label = ctk.CTkLabel(app, text="Email:")
email_label.pack(pady=10)
email_entry = ctk.CTkEntry(app, placeholder_text="Enter your email")
email_entry.pack()

phone_label = ctk.CTkLabel(app, text="Phone:")
phone_label.pack(pady=10)
phone_entry = ctk.CTkEntry(app, placeholder_text="Enter your phone number")
phone_entry.pack()

# Add submit button
submit_button = ctk.CTkButton(app, text="Submit", command=lambda: submit_data())
submit_button.pack(pady=25)

# Submit data function
def submit_data():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    # Validate input
    if not validate_input(name) or not validate_input(email) or not validate_input(phone):
        # Show error message
        # (Add your own error message UI logic here)
        return

    save_data(name, email, phone)

    # Reset input fields
    name_entry.delete(0, ctk.END)
    email_entry.delete(0, ctk.END)
    phone_entry.delete(0, ctk.END)

app.mainloop()