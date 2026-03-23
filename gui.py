import tkinter as tk
from tkinter import messagebox

# ---------------- DATA ---------------- #
freelancers = [
    {"name": "nivedh sunil", "skills": ["python", "ml"], "cost": 500, "deadline": 7},
    {"name": "Bob", "skills": ["web", "js"], "cost": 300, "deadline": 3},
    {"name": "Charlie", "skills": ["python", "web"], "cost": 400, "deadline": 4}
]

projects_data = [
    {"title": "E-commerce Website", "skills": "web,js", "budget": "500", "deadline": "5 days"},
    {"title": "AI Chatbot", "skills": "python,ml", "budget": "700", "deadline": "7 days"},
    {"title": "Portfolio Website", "skills": "html,css", "budget": "200", "deadline": "2 days"}
]

# ---------------- ALGORITHM ---------------- #
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


# ---------------- MAIN WINDOW ---------------- #
root = tk.Tk()
root.title("Freelancer Optimizer Pro")
root.geometry("900x600")
root.configure(bg="#0f3d3e")

nav_frame = tk.Frame(root, bg="#134e4a")
nav_frame.pack(fill="x")

content_frame = tk.Frame(root, bg="#0f3d3e")
content_frame.pack(fill="both", expand=True)

active_btn = None

# ---------------- PAGE SWITCH ---------------- #
def show_frame(frame_func, btn):
    global active_btn

    for widget in content_frame.winfo_children():
        widget.destroy()

    frame_func()

    # Toggle effect
    if active_btn:
        active_btn.config(bg="#134e4a")

    btn.config(bg="#0f766e")
    active_btn = btn


# ---------------- DASHBOARD ---------------- #
def dashboard_page():
    frame = tk.Frame(content_frame, bg="#0f3d3e")
    frame.pack(fill="both", expand=True)

    tk.Label(frame,
             text="Freelancer Optimizer",
             font=("Georgia", 28, "bold"),
             bg="#0f3d3e",
             fg="white").pack(pady=30)

    tk.Label(frame,
             text="Smart Project Assignment System 🌿",
             font=("Georgia", 14),
             bg="#0f3d3e",
             fg="#99f6e4").pack()


# ---------------- PROJECTS ---------------- #
def projects_page():
    frame = tk.Frame(content_frame, bg="#0f3d3e")
    frame.pack(fill="both", expand=True)

    tk.Label(frame,
             text="Projects",
             font=("Georgia", 22, "bold"),
             bg="#0f3d3e", fg="white").pack(pady=10)

    for proj in projects_data:
        card = tk.Frame(frame, bg="#ccfbf1")
        card.pack(pady=10, padx=20, fill="x")

        tk.Label(card, text=proj["title"],
                 font=("Arial", 14, "bold"),
                 bg="#ccfbf1").pack(anchor="w", padx=10)

        tk.Label(card,
                 text=f"Skills: {proj['skills']}",
                 bg="#ccfbf1").pack(anchor="w", padx=10)

        tk.Label(card,
                 text=f"Budget: {proj['budget']}",
                 bg="#ccfbf1").pack(anchor="w", padx=10)

        tk.Label(card,
                 text=f"Deadline: {proj['deadline']}",
                 bg="#ccfbf1").pack(anchor="w", padx=10)


# ---------------- ASSIGN ---------------- #
def assign_page():
    frame = tk.Frame(content_frame, bg="#0f3d3e")
    frame.pack(fill="both", expand=True)

    tk.Label(frame,
             text="Assign Project",
             font=("Georgia", 22, "bold"),
             bg="#0f3d3e", fg="white").pack(pady=10)

    # Labels added 🔥
    tk.Label(frame, text="Skills:", bg="#0f3d3e", fg="white").pack()
    skills_entry = tk.Entry(frame, width=40)
    skills_entry.pack(pady=5)

    tk.Label(frame, text="Budget:", bg="#0f3d3e", fg="white").pack()
    budget_entry = tk.Entry(frame, width=40)
    budget_entry.pack(pady=5)

    tk.Label(frame, text="Deadline:", bg="#0f3d3e", fg="white").pack()
    deadline_entry = tk.Entry(frame, width=40)
    deadline_entry.pack(pady=5)

    output_label = tk.Label(frame,
                            text="",
                            font=("Arial", 14, "bold"),
                            bg="#0f3d3e",
                            fg="white")
    output_label.pack(pady=15)

    def assign():
        try:
            project = {
                "skills": [s.strip() for s in skills_entry.get().lower().split(",")],
                "budget": int(budget_entry.get()),
                "deadline": int(deadline_entry.get())
            }

            result = greedy_match(project)

            if result:
                output_label.config(text=f"Assigned to: {result['name']}")
            else:
                output_label.config(text="No suitable freelancer")

        except:
            messagebox.showerror("Error", "Invalid input")

    tk.Button(frame,
              text="Assign Freelancer",
              command=assign,
              bg="#5eead4",
              font=("Arial", 12, "bold"),
              cursor="hand2").pack(pady=10)


# ---------------- FEEDBACK ---------------- #
def feedback_page():
    frame = tk.Frame(content_frame, bg="#0f3d3e")
    frame.pack(fill="both", expand=True)

    tk.Label(frame,
             text="Feedback",
             font=("Georgia", 22, "bold"),
             bg="#0f3d3e", fg="white").pack(pady=10)

    entry = tk.Entry(frame, width=40)
    entry.pack(pady=5)

    tk.Button(frame,
              text="Submit",
              bg="#5eead4",
              command=lambda: messagebox.showinfo("Done", "Feedback submitted")).pack(pady=10)


# ---------------- NAV BUTTON ---------------- #
def create_nav(text, page_func):
    btn = tk.Button(nav_frame,
                    text=text,
                    bg="#134e4a",
                    fg="white",
                    padx=15,
                    pady=5,
                    bd=0,
                    cursor="hand2")

    btn.config(command=lambda: show_frame(page_func, btn))
    btn.pack(side="left", padx=10)

    return btn


# ---------------- NAV ---------------- #
btn1 = create_nav("Dashboard", dashboard_page)
btn2 = create_nav("Projects", projects_page)
btn3 = create_nav("Assign", assign_page)
btn4 = create_nav("Feedback", feedback_page)

# Default page
show_frame(dashboard_page, btn1)

root.mainloop()