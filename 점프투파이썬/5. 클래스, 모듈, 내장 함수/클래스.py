result = 0

def add(num):
    global result #이전 결과 값을 유지하기 위한 전역변수 사용
    result += num
    return result

print(add(3))
print(add(4))

class Cal:
    def setdata(self,first,second): #여기서 setdata는 메서드이다.
        # 클래스 내부에 구성된 함수 = 메서드
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a= Cal()
a.setdata(4,2)
print(a.first)
print(a.second)
print(a.add()) #add메서드 호출 후 출력

b = Cal()

b.setdata(3,7)
print(b.first)
print(a.first) #서로의 first값에 영향을 주지 않음

