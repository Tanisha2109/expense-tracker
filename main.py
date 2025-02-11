import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.expenses = []

        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.amount_label = tk.Label(self.root, text="Amount:")
        self.amount_entry = tk.Entry(self.root)

        self.description_label = tk.Label(self.root, text="Description:")
        self.description_entry = tk.Entry(self.root)

        self.add_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.total_label = tk.Label(self.root, text="Total: ₹ 0.00")

        self.tree = ttk.Treeview(self.root, columns=('Amount', 'Description'), show='headings')
        self.tree.heading('Amount', text='Amount')
        self.tree.heading('Description', text='Description')

    def layout_widgets(self):
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.description_label.grid(row=1, column=0, padx=10, pady=10)
        self.description_entry.grid(row=1, column=1, padx=10, pady=10)

        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.total_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.tree.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(4, weight=1)

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            description = self.description_entry.get()

            if description == "":
                messagebox.showerror("Error", "Description cannot be empty")
                return

            self.expenses.append((amount, description))
            self.tree.insert('', 'end', values=(amount, description))
            self.update_total()

            self.amount_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def update_total(self):
        total = sum(amount for amount, _ in self.expenses)
        self.total_label.config(text=f"Total: ₹{total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()