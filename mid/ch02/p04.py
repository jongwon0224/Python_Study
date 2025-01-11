#파일 읽고 쓰기
#파일변수명 = open함수 ('c드라이브:/폴더명/파일명.파일속성', '모드' ) => 모드종류: r(읽기), w(쓰기), a(추가가)

# 쓰기모드(write)
f = open('c:/test/abc.text','w')
for i in range(1,8):
    f.write('%d번째\n'%i)
f.close()

#추가모드 (add) => f.write로 마지막에 문장추가
f = open('c:/test/abc.text', 'a')
f.write('helloPython')
f.close()

#읽기모드(read) => readline  :1줄 읽기, readlines:모든라인 한줄씩 리스트로 리턴
f = open('c:/test/abc.text', 'r')
m = f.readlines()
for i in m:
    print(i, end='') #end로 줄바꿈 없애기
f.close()