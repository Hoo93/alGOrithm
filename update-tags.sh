#!/bin/bash

# readme.md 기본 템플릿 확인 및 생성
if [ ! -f "readme.md" ]; then
  cat <<EOL > readme.md
# 알고리즘 문제 풀이 모음

## 소개
이 레포지토리는 백준 사이트에서 푼 알고리즘 문제들의 풀이를 모아둔 저장소입니다. 각 문제는 알고리즘 태그에 따라 분류되어 있으며, 클릭하면 해당 문제의 Python 코드로 바로 이동할 수 있습니다.

## 목차
<!-- 목차가 여기에 추가됨 -->

## 알고리즘별 문제 목록

<!-- 알고리즘 섹션이 여기에 추가됨 -->
EOL
fi

# 새로운 알고리즘 태그 처리
for dir in */; do
  problem_dir=$(basename "$dir")
  
  if [ -f "$dir/tag.txt" ]; then
    while IFS= read -r tag; do
      # 목차에서 해당 태그가 없으면 추가
      if ! grep -q "## $tag" readme.md; then
        # 목차에 태그 추가 (명시적으로 줄바꿈 \n 추가)
        sed -i '' "/<!-- 목차가 여기에 추가됨 -->/a\\
- [$tag](#$tag)\n" readme.md
        # 알고리즘 섹션에 태그 추가 (명시적으로 줄바꿈 \n 추가)
        sed -i '' "/<!-- 알고리즘 섹션이 여기에 추가됨 -->/a\\
### $tag\n| Problem 1 | Problem 2 | Problem 3 |/a//
|-----------|-----------|-----------|\a\\
<!-- $tag 문제들이 여기에 추가됨 -->" readme.md
      fi
      
      # 이미 존재하는 문제인지 확인 후 추가
      if ! grep -q "$problem_dir" readme.md; then
        # 태그 섹션에 문제 추가
        problem_link="[Problem $problem_dir](./$problem_dir/$problem_dir.py)"
        
        # 문제를 테이블에 3열로 추가
        current_problems=$(grep -A 1 "<!-- $tag 문제들이 여기에 추가됨 -->" readme.md | tail -1)
        if [[ "$current_problems" == *"|"* ]]; then
          # 마지막 행이 다 채워지지 않았다면 추가
          num_columns=$(echo "$current_problems" | grep -o "|" | wc -l)
          if [ "$num_columns" -lt 4 ]; then
            sed -i '' "/<!-- $tag 문제들이 여기에 추가됨 -->/a\\
${problem_link} |" readme.md
          else
            sed -i '' "/<!-- $tag 문제들이 여기에 추가됨 -->/a\\
| $problem_link |" readme.md
          fi
        else
          # 새 행 추가
          sed -i '' "/<!-- $tag 문제들이 여기에 추가됨 -->/a\\
| $problem_link |" readme.md
        fi
      fi
    done < "$dir/tag.txt"
  fi
done
