import tkinter as tk
from tkinter import ttk, messagebox

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Account Creation")
        self.root.geometry("300x200")
        
        # Initialize variables for storing user inputs
        self.name = tk.StringVar()
        self.email = tk.StringVar()

        # Account Creation Page UI
        tk.Label(root, text="Name:").pack(pady=5)
        self.entry_name = tk.Entry(root, textvariable=self.name, width=30)
        self.entry_name.pack(pady=5)

        tk.Label(root, text="Email:").pack(pady=5)
        self.entry_email = tk.Entry(root, textvariable=self.email, width=30)
        self.entry_email.pack(pady=5)

        tk.Button(root, text="Create Account", command=self.open_subject_page).pack(pady=10)

    def open_subject_page(self):
        name = self.name.get()
        email = self.email.get()

        if not name or not email:
            messagebox.showerror("Error", "Name and Email are required!")
            return

        # Hide the Account Creation Window
        self.root.withdraw()

        # Open Subject Management Page
        self.subject_window = tk.Toplevel()
        self.subject_window.title("Subject Management")
        self.subject_window.geometry("400x500")

        # Initialize subject-related variables
        self.subjects = ["Mathematics", "Science", "History", "English", "Art"]
        self.added_subjects = []

        # UI for Subject Management Page
        tk.Label(self.subject_window, text=f"Welcome, {name}!", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.subject_window, text="Select Subject:").pack()
        self.subject_dropdown = ttk.Combobox(self.subject_window, values=self.subjects)
        self.subject_dropdown.pack(pady=5)

        tk.Button(self.subject_window, text="Add Subject", command=self.add_subject).pack(pady=5)
        tk.Button(self.subject_window, text="Update Subject", command=self.update_subject).pack(pady=5)
        tk.Button(self.subject_window, text="Delete Subject", command=self.delete_subject).pack(pady=5)

        self.listbox = tk.Listbox(self.subject_window, width=30, height=10)
        self.listbox.pack(pady=10)

        tk.Button(self.subject_window, text="Refresh Dropdown", command=self.refresh_dropdown).pack(pady=5)

    # Refreshes the dropdown options to exclude already added subjects.
    def refresh_dropdown(self):
        available_subjects = [subject for subject in self.subjects if subject not in self.added_subjects]     # Create a list of subjects that are not already added
        self.subject_dropdown["values"] = available_subjects                                                  # Update the dropdown values to reflect the available subjects

     # Adds the selected subject to the list if not already added.
    def add_subject(self):
        selected_subject = self.subject_dropdown.get()
        if selected_subject and selected_subject not in self.added_subjects:     # Check if a subject is selected and not already added to the list
            self.added_subjects.append(selected_subject)                         # Add the selected subject to the list of added subjects
            self.listbox.insert(tk.END, selected_subject)                        # Insert the selected subject at the end of the listbox
            self.refresh_dropdown()                                              # Refresh the dropdown to exclude the newly added subject
        else:
            messagebox.showinfo("Info", "Subject already added or not selected.")

    #  Deletes the selected subject from the list.
    def delete_subject(self):
        selected = self.listbox.curselection()     
        if selected:                                  # Check if a subject is selected in the listbox                
            subject = self.listbox.get(selected)      # Get the subject from the listbox using the selected index
            self.added_subjects.remove(subject)       # Remove the selected subject from the list of added subjects
            self.listbox.delete(selected)             # Delete the selected subject from the listbox
            self.refresh_dropdown()                   # Refresh the dropdown to exclude the deleted subject
        else:
            messagebox.showinfo("Info", "Please select a subject to delete.")

    # Updates the selected subject in the list.
    def update_subject(self):
        selected = self.listbox.curselection()
        new_subject = self.subject_dropdown.get()
        if selected and new_subject and new_subject not in self.added_subjects:  # Check if a subject is selected and if the new subject is valid and not already added
            old_subject = self.listbox.get(selected)                             # Get the old subject that was previously selected
            self.added_subjects.remove(old_subject)                              # Remove the old subject from the list of added subjects
            self.added_subjects.append(new_subject)                              # Add the new subject to the list of added subjects
            self.listbox.delete(selected)                                        # Remove the old subject from the listbox
            self.listbox.insert(selected, new_subject)                           # Insert the new subject in the same position in the listbox
            self.refresh_dropdown()                                              # Refresh the dropdown to exclude already added subjects
        else:
            messagebox.showinfo("Info", "Please select a valid subject to update.")

# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
