#!/bin/bash

# 문제 번호를 입력받습니다.
read -p "문제 번호를 입력하세요: " problem_number

# 입력된 문제 번호로 디렉토리를 생성하고 이동합니다.
mkdir "$problem_number"
cd "$problem_number" || exit

# 문제 번호.py 파일과 input.txt 파일을 생성합니다.
touch "${problem_number}.py"
touch input.txt

echo "Directory $problem_number and files ${problem_number}.py, input.txt created successfully."
