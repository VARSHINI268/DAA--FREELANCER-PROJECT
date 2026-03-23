import json
import sys

freelancers = [
    {"name": "Alice", "skills": ["python", "ml"], "cost": 500, "deadline": 5},
    {"name": "Bob", "skills": ["web", "js"], "cost": 300, "deadline": 3},
    {"name": "Charlie", "skills": ["python", "web"], "cost": 400, "deadline": 4}
]

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


# Read input from JS (stdin)
data = json.loads(sys.stdin.read())

project = {
    "skills": data["skills"],
    "budget": data["budget"],
    "deadline": data["deadline"]
}

result = greedy_match(project)

if result:
    print(json.dumps({"status": "success", "freelancer": result["name"]}))
else:
    print(json.dumps({"status": "fail"}))