##코드 예제
import re
p = re.compile('[a-z]+')

#re.match() 예제
m = p.match("regular")
if m:
    print("match : ", m)
else:
    print("No match")

#re.search() 예제
m = p.search("123regular")
print(m)

#re.findall() 예제
m = p.findall("regular expression")
print(m)

#re.finditer() 예제
m = p.finditer("big data reqgular expression")
print(m)

#match 객체 메소드 예제
m = p.match("regular")
m.group()
m.start()
m.end()
m.span()
