# AI Resume Analyzer

keywords = [
    "Python",
    "Java",
    "SQL",
    "AWS",
    "Machine Learning",
    "Data Analysis",
    "Communication",
    "Leadership",
    "AI",
    "Cloud"
]

with open("sample_resume.txt", "r") as file:
    resume = file.read()

score = 0
found_keywords = []

for word in keywords:
    if word.lower() in resume.lower():
        score += 10
        found_keywords.append(word)

if score > 100:
    score = 100

print("===== AI RESUME ANALYZER =====\n")

print("Keywords Found:")
for word in found_keywords:
    print("✔", word)

print("\nATS Score:", score, "/100")

if score >= 80:
    print("Excellent Resume!")
elif score >= 50:
    print("Good Resume. Add more technical skills.")
else:
    print("Resume needs improvement.")

missing = [word for word in keywords if word not in found_keywords]

print("\nSuggested Keywords:")
for word in missing:
    print("-", word)
