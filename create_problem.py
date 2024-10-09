import os

def create_problem_dir_and_files():
    # 1. 문제 번호를 입력 받는다.
    problem_number = input("문제 번호를 입력하세요: ")

    # 2. 입력 받은 문제 번호와 같은 dir 를 스크립트 파일과 동일 경로에 생성한다.
    dir_path = os.path.join(os.getcwd(), problem_number)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"디렉토리 {dir_path} 생성 완료.")
    else:
        print(f"디렉토리 {dir_path}는 이미 존재합니다.")

    # 3. 생성한 dir 안에 문제번호.py 파일을 만든다.
    py_file_path = os.path.join(dir_path, f"{problem_number}.py")
    with open(py_file_path, "w") as py_file:
        py_file.write("# 문제 해결 코드 작성\n")
    print(f"파일 {py_file_path} 생성 완료.")

    # 4. 생성한 dir 안에 input.txt 파일을 만든다.
    input_file_path = os.path.join(dir_path, "input.txt")
    with open(input_file_path, "w") as input_file:
        input_file.write("# 입력 데이터 작성\n")
    print(f"파일 {input_file_path} 생성 완료.")

if __name__ == "__main__":
    create_problem_dir_and_files()