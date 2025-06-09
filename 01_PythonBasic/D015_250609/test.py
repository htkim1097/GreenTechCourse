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