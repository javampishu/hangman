stud_score = int(input())
max_scrore = int(input())

procent = (stud_score / max_scrore) * 100

if 90 <= procent <= 100:
    print("A")
elif 80 <= procent < 90:
    print("B")
elif 70 <= procent < 80:
    print("C")
elif 60 <= procent < 70:
    print("D")
else:
    print("F")
