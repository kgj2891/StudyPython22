# 파일 입출력 2 - 파일 읽기

f = open(file='C:/STUDY/StudyPython22/temp.txt', mode='r', encoding='utf-8')

# t = f.read()
while True:
    line = f.readline()
    if not line: break

    print(line, end='')
#print(f)

f.close()
print('파일 읽기 완료')