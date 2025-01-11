#xml파일 읽기
# 모듈 import하기
import xml.etree.ElementTree as ET

#모듈에서 xml경로 읽어오기
tree = ET.parse('c:/test/person.xml')
#루트가져오기
root = tree.getroot()  
print(root) # <Element 'Person' at 0x0000018A0FE5FF60> => 객체형태
print(root.tag) #Person => 밸류값 가져옴

#Person안에 값 가져오기 => tag로 키값가져옴 & text로 밸류값 가져옴
#i.tag = name, age, address
#i.text = 홍길동, 15, 대구구
for i in root:
    print(i.tag, i.text)