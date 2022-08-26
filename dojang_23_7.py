matrix = []
col, row = map(int, input().split())    # col = 가로, row = 세로

for i in range(row):
    matrix.append(list(input()))
    # ex) 입력:*** >>> matrix[i] = ['*', '*', '*'] row번 만큼 입력하면 for 종료

for i in range(len(matrix)):        # 세로열 만큼 반복
  for j in range(len(matrix[i])):   # 가로열 만큼 반복 | 인덱싱으로 주변 요소를 찾아야 하기 때문에 range 사용
    if matrix[i][j] == '.':         # '*'은 따로 수정을 할 필요가 없으므로 '.'이 아니면 건너뜀

      temp = [matrix[k] for k in range(i-1, i+2) if k >= 0 and k < row]
      # temp라는 임시 리스트에 세로열 인덱스의 -1 ~ +1을 불러오면서(range(i-1, i+2)) 인덱스가 음수 혹은 세로열을 초과했는지 검색(if k >= 0 and k < row)
      # temp = []
      # for k in range(i-1, i+2):
      #   if k >= 0 and k < row:
      #     temp.append(matrix[k])

      temp = [v[k] for k in range(j-1, j+2) if k >= 0 and k < col for v in temp]
      # 주변 세로열을 가져온 temp에 담긴 각 리스트들을(for v in temp) 가로열 인덱스의 -1 ~ +1을 불러오면서(range(j-1, j+2)) 인덱스가 음수 혹은 가로열을 초과했는지 검색(if k >= 0 and k < col)하면서
      # 기존 2차원 리스트가 쪼개지도록 대괄호 생략
      # for v in temp:
      #   for k in range(j-1, j+2):
      #     if k >= 0 and k < col:
      #       temp.append(v[k]) -- temp 리스트에 이미 다른 요소가 있어서 실제 코드로 사용하려면 새로운 빈 리스트에 할당해야함

      matrix[i][j] = str(temp.count('*')) # temp에서 별의 총 갯수를 세고(temp.count('*') 리스트를 간단하게 합칠 수 있게 join을 쓰기 전 class를 str으로 변환 후 각 '.'였던 요소에 대입
      
  print(''.join(matrix[i]))   # matrix 리스트를 세로줄 별로(들여쓰기를 가로열 for문 종료에 맞춰주기) join 후 출력
