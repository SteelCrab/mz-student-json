import os,platform,json

def clearScreen():
    if platform.system() =="Windows":
        os.system("cls")

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 50:
        return "E"
    else:
        return "F"

def student_output(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            students = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("파일을 찾을 수 없거나 JSON 형식이 잘못되었습니다.")
        return

    print("\n이름  국어  영어  수학  총점  평균  결과")
    print("-------------------------------------------")
    for student in students:
        name = student["이름"]
        korean = student["국어"]
        english = student["영어"]
        math = student["수학"]

        total = korean + english + math
        average = total / 3
        grade = get_grade(average)
        print(f"{name:4} {korean:4}  {english:4}  {math:4}  {total:4}  {average:6.1f}   {grade:2}")
