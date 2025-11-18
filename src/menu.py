from grader import clearScreen, student_output, get_grade
from input import studentinput, input_score
def menu_windows():
    while True:
        clearScreen()
        print("메뉴")
        print("1.학생 성적 입력 ")
        print("2.학생 성적 출력  ")
        print("3. 종료")

        select  = int(input("입력: "))
        if select == 1:
            studentinput()
        elif select ==2:
            student_output("test.json")
        elif select ==3:
            break
        else:
            print("번호의 입력이 아닙니다.")