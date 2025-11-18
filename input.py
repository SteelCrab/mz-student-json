import json
import os

def reset_json(filename):
    # 파일 리셋 (빈 리스트로 초기화)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False)

def input_score(msg):
    num = input(msg)
    try:
        return int(num)
    except:
        print_msg = f"정수값 아님 \n{msg}"
        return input_score(print_msg)

def studentinput():
    #학생 리스트
    studentList = {"국어":0, "영어":0, "수학":0}
    students =  ("홍길동","김유신","이순신")
    students_info = list()
    loadPath = os.path.join(os.getcwd(),"test.json")

    for name in students:
        dic = dict()
        dic.update({"이름":name})
        for key,val in studentList.items():
            msg = f"{name}의 {key}점수를 입력하세요. ==>"
            tmp_item = input_score(msg)
            dic.update({key:tmp_item})
            print(dic)
        students_info.append(dic)
        json_val = json.dumps(students_info, ensure_ascii=False, indent=2)
        with open(loadPath,"w",encoding="utf-8") as fp:
            fp.write(json_val)
            fp.close()
        # 전체 출력해서 확인 
        print(students_info)
