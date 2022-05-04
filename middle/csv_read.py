# CSV파일 읽기
import csv

file_name = 'C:/STUDY/StudyPython22/busanbus_211231.csv'

f = open(file_name, mode='r', encoding= 'cp949')
reader = csv.reader(f, delimiter=',') #구분자가 ,일경우

next(reader) # 제목줄 있을때 필요없을경우
for line in reader:
    print(line)

f.close() 