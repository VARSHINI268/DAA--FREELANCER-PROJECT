import tkinter as tk
from tkinter import messagebox

# Freelancers Data
freelancers = [
    {"name": "Alice", "skills": ["python", "ml"], "cost": 500, "deadline": 5},
    {"name": "Bob", "skills": ["web", "js"], "cost": 300, "deadline": 3},
    {"name": "Charlie", "skills": ["python", "web"], "cost": 400, "deadline": 4}
]

# Greedy Algorithm
def greedy_match(project):
    best_match = None
    best_score = float('inf')

    for f in freelancers:
        skill_match = len(set(project["skills"]) & set(f["skills"]))

        if skill_match == 0:
            continue

        score = f["cost"] + (f["deadline"] * 10) - (skill_match * 50)

        if score < best_score:
            best_score = score
            best_match = f

    return best_match


# Button Click Function
def assign_project():
    skills_input = skills_entry.get()
    budget = budget_entry.get()
    deadline = deadline_entry.get()

    if not skills_input or not budget or not deadline:
        messagebox.showerror("Error", "Please fill all fields!")
        return

    try:
        project = {
            "skills": [s.strip().lower() for s in skills_input.split(",")],
            "budget": int(budget),
            "deadline": int(deadline)
        }

        result = greedy_match(project)

        if result:
            output_label.config(
                text=f"✅ Assigned to: {result['name']}",
                fg="green"
            )
        else:
            output_label.config(
                text="❌ No suitable freelancer found",
                fg="red"
            )

    except ValueError:
        messagebox.showerror("Error", "Budget & Deadline must be numbers!")


# GUI Window
root = tk.Tk()
root.title("Freelancer Project Assignment Optimizer")
root.geometry("400x350")
root.configure(bg="#f4f4f4")

# Title
title = tk.Label(root, text="Freelancer Optimizer", font=("Arial", 16, "bold"), bg="#f4f4f4")
title.pack(pady=10)

# Skills Input
skills_label = tk.Label(root, text="Skills (comma separated):", bg="#f4f4f4")
skills_label.pack()
skills_entry = tk.Entry(root, width=40)
skills_entry.pack(pady=5)

# Budget Input
budget_label = tk.Label(root, text="Budget:", bg="#f4f4f4")
budget_label.pack()
budget_entry = tk.Entry(root, width=40)
budget_entry.pack(pady=5)

# Deadline Input
deadline_label = tk.Label(root, text="Deadline (days):", bg="#f4f4f4")
deadline_label.pack()
deadline_entry = tk.Entry(root, width=40)
deadline_entry.pack(pady=5)

# Button
assign_btn = tk.Button(root, text="Assign Freelancer", command=assign_project, bg="#007bff", fg="white")
assign_btn.pack(pady=15)

# Output
output_label = tk.Label(root, text="", font=("Arial", 12), bg="#f4f4f4")
output_label.pack(pady=10)

# Run App
root.mainloop()