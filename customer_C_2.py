class Customer:
    def __init__(self, first_name, family_name,age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age
    def full_name(self):
        print(self.first_name,self.family_name)
        print(self.age)
        # print(self.age)
    # def age(self):
    #     print(self.age)
    # def age(self):
    #     print(int(self.age))

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)

print(ken.age)
# print(ken.age)
# ken.age
# print(ken.age)
# なぜこれで出力出てこない・・・・
#エラーが出てこないから検討つかない・・・・。こういうときどうしたらいいのだ？

ken.age
# 本当にこれでいいのか？？？？でてきたけども。。。。







# 15 という値を返す
#
# tom = Customer(first_name="Tom", family_name="Ford", age= 57)
# tom.age
# # 57 という値を返す
#
# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu.age
# # 73 という値を返す