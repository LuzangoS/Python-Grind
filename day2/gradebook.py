students = [
    {"name": "Chanda", "score": 72},
    {"name": "Mary", "score": 88},
    {"name": "Tom", "score": 45},
]

def add_student(students, name, score):
    students.append({"name": name, "score": score})

def average_score(students):
    if not students:
        return 0
    total_score = 0
    for s in students:
        total_score += s["score"]
    return total_score / len(students)

def top_student(students):
    if not students:
        return None
    top = students[0]
    for s in students:
        if s["score"] > top["score"]:
            top = s
    return top

def print_report(students):
    print("Student Report")
    for s in students:
        status = "Pass" if s["score"] >= 50 else "Retake"
        print(f"{s['name']}: {s['score']} ({status})")

add_student(students, "Grace", 91)
print_report(students)
print(f"Class average: {average_score(students):.1f}")

top = top_student(students)
print(f"Top student: {top['name']} with score {top['score']}")