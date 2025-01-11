#XML만들기 & 파일 생성하기

#append는 마지막에 넣어줌 & insert는 괄호안 인덱스번호에 맞게 넣어줌
# 모듈 임포트
from xml.etree.ElementTree import *

#최상위 노드 만들기
person = Element('Person')

#방법1 => 태그 생성 -> 태그.text = '문자열' -> person(최상위노드).append(태그)
name = Element('name')
name.text = '홍길동'
person.append(name) #<name>홍길동</name>

age = Element('age')
age.text = '15'
person.append(age) #<age>15</age>

#방법2 => SubElement(최상위노드, 태그).text = '값'
SubElement(person, 'address').text = '대구' #<address>대구</address>

#방법3 => append말고 insert사용 -> insert함수의 인덱스값에 xml넣어짐
no = Element('no')
no.text = '17'
person.insert(1,no)  #<name>홍길동</name><no>17</no><age>15</age><address>대구</address></Person>

#삭제1 => 최상위노드.remove(태그)
person.remove(no) 

#노드에 속성추가하기 => 노드.attrib['속성명'] = '속성값'
person.attrib['date'] = '2020-02-25'  #<Person date="2020-02-25">

dump(person) #print대신 dump를 사용

#xml파일 생성하기
ElementTree(person).write('c:/test/person.xml')