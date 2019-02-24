class Person:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):           # getter
        return self.__age

    @age.setter
    def age(self, value):    # setter
        self.__age = value

james = Person()
james.age = 20      # �ν��Ͻ�.�Ӽ� �������� �����Ͽ� �� ����
print(james.age)    # �ν��Ͻ�.�Ӽ� �������� ���� ������
