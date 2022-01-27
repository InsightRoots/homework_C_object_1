class Customer:
    def __init__(self,age):
        self.age = age
    def age(self):
        print(self.age)

ken = Customer(age=15)

print(ken.age)
ken.age
print(ken.age)

#エラーが出てこないから検討つかない・・・・。こういうときどうしたらいいのだ？