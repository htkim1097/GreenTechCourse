#
# class Test:
#     def __init__(this):
#         this.name = "fds"
#
# print(Test().name)
#

# class St:
#     def __init__(self, name, kor, math, eng, sci):
#         self.name = name
#         self.kor = kor
#         self.math = math
#         self.eng = eng
#         self.sci = sci
#
# student_list = [
#     St("A", 1, 2, 3, 4),
#     St("b", 1, 2, 3, 4),
#     St("c", 1, 2, 3, 4),
#     St("A", 1, 2, 3, 4),
#     St("A", 1, 2, 3, 4),
#     St("A", 1, 2, 3, 4),
# ]


# class Student:
#     def __init__(self, name, kor, math, eng, sci):
#         self.name = name
#         self.kor = kor
#         self.math = math
#         self.eng = eng
#         self.sci = sci
#
#     def get_sum(self):
#         return self.kor + self.math + self.eng + self.sci
#
#     def get_avg(self):
#         return self.get_sum() / 4
#
#     def to_string(self):
#         return f"{self.name}\t{self.get_sum()}\t{self.get_avg()}"
#
# student_list = [
#     Student("Kim", 87, 98, 88, 95),
#     Student("Park", 92, 98, 96, 98),
#     Student("Choi", 76, 96, 94, 90),
#     Student("Seo", 98, 92, 96, 92),
#     Student("Kang", 95, 98, 98, 98),
#     Student("Lee", 64, 88, 92, 92),
# ]
#
# print("이름", "총점", "평균", sep="\t")
# for st in student_list:
#     print(st.to_string())

# class Student:
#     def study(self):
#         print("공부를 합니다.")
#
# class Teacher:
#     def teach(self):
#         print("학생을 가르칩니다.")
#
# classroom = [Student(), Student(), Teacher(), Student(), Student(), Student(),]
#
# for person in classroom:
#     if isinstance(person, Student):
#         person.study()
#     elif isinstance(person, Teacher):
#         person.teach()


# class Student:
#     def __init__(self, name, kor, math, eng, sci):
#         self.name = name
#         self.kor = kor
#         self.math = math
#         self.eng = eng
#         self.sci = sci
#
#     def get_sum(self):
#         return self.kor + self.math + self.eng + self.sci
#
#     def get_avg(self):
#         return self.get_sum() / 4
#
#     def __str__(self):
#         return f"{self.name}\t{self.get_sum()}\t{self.get_avg()}"
#
# student_list = [
#     Student("Kim ", 87, 98, 88, 95),
#     Student("Park", 92, 98, 96, 98),
#     Student("Choi", 76, 96, 94, 90),
#     Student("Seo ", 98, 92, 96, 92),
#     Student("Kang", 95, 98, 98, 98),
#     Student("Lee ", 64, 88, 92, 92),
# ]
#
# print("이름", "총점", "평균", sep="\t")
# for st in student_list:
#     print(str(st))



# class Student:
#     count = 0
#
#     def __init__(self, name, kor, math, eng, sci):
#         self.name = name
#         self.kor = kor
#         self.math = math
#         self.eng = eng
#         self.sci = sci
#
#         # 클래스 변수에 접근하기
#         Student.count += 1
#         print("{}번째 학생이 생성되었습니다.".format(Student.count))
#
# student_list = [
#     Student("Kim", 87, 98, 88, 95),
#     Student("Park", 92, 98, 96, 98),
#     Student("Choi", 76, 96, 94, 90),
#     Student("Seo", 98, 92, 96, 92),
#     Student("Kang", 95, 98, 98, 98),
#     Student("Lee", 64, 88, 92, 92),
# ]
#
# print("현재 생성된 총 학생의 수는 {}명입니다.".format(Student.count))


# class Student:
#     count = 0
#     student_list = []
#
#     def __init__(self, name, kor, math, eng, sci):
#         self.name = name
#         self.kor = kor
#         self.math = math
#         self.eng = eng
#         self.sci = sci
#         Student.count += 1
#         Student.student_list.append(self)
#
#     @classmethod
#     def print(cls):
#         print("---- 학생 목록 ----")
#         print("이름\t총점\t평균")
#
#         for st in cls.student_list: # Student.student_list 라고 사용해도 동일
#             print(str(st))
#
#     def get_sum(self):
#         return self.kor + self.math + self.eng + self.sci
#
#     def get_avg(self):
#         return self.get_sum() / 4
#
#     def __str__(self):
#         return f"{self.name}\t{self.get_sum()}\t{self.get_avg()}"
#
# Student("Kim", 87, 98, 88, 95)
# Student("Park", 92, 98, 96, 98)
# Student("Choi", 76, 96, 94, 90)
# Student("Seo", 98, 92, 96, 92)
# Student("Kang", 95, 98, 98, 98)
# Student("Lee", 64, 88, 92, 92)
#
# Student.print()

# import math
#
# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius
#     def get_circumference(self):
#         return 2 * math.pi * self.__radius
#     def get_area(self):
#         return math.pi * (self.__radius ** 2)
#
#     def get_radius(self):
#         return self.__radius
#
#     def set_radius(self, value):
#         self.__radius = value
#
# circle = Circle(10)
# print("# 원의 둘레와 넓이를 구합니다.")
# print("원의 둘레:", circle.get_circumference())
# print("원의 넓이:", circle.get_area())
#
# print("#__radius에 접근합니다.")
# print(circle.get_radius())
#
# circle.set_radius(2)
# print("# 원의 둘레와 넓이를 구합니다.")
# print("원의 둘레:", circle.get_circumference())
# print("원의 넓이:", circle.get_area())


# class CustomException(Exception):
#     def __init__(self):
#         super().__init__()
#
#     def __str__(self):
#         return "오류 발생 메시지"
#
# raise CustomException


# 소지품 has-a / is-a 관계를 둘 다 사용하는 클래스 간 구조 정의.
# 속성, 함수, 상속 사용.

class ItemObject:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def print_desc(self):
        print(f"{self.name}, {self.desc}")

class Bag(ItemObject):
    def __init__(self, name, desc):
        super().__init__(name, desc)
        self.items = []

    def show_items(self):
        self.print_desc()
        for i in self.items:
            print(i.print_desc())

class Person:
    def __init__(self, bag:Bag):
        self.bag = bag

    def show_items(self):
        self.bag.show_items()

my_bag = Bag("검정 크로스 백", "별로 안들어감")
t_brush = ItemObject("칫솔", "점심 먹고 사용")
charger = ItemObject("충전기", "보조배터리나 핸드폰에 사용")

my_bag.items.append(t_brush)
my_bag.items.append(charger)

me = Person(my_bag)

me.show_items()


# 콘솔 게임
# 사용자 입력을 tick 기준으로
# 사용자가 움직여야 몬스터도 이동
# tick manager -> 여러 클래스에 업데이트
# 여러 클래스는 정보를 -> tick manager로 송신