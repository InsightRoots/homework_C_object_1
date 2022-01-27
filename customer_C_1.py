# # class を定義する必要がある。
# class UserName:
#     def __init__(self, name):
#         self.name = name
#
# # 実体化
# tanaka = UserName(name='tanaka')
#
# # 出力
# print(tanaka)

class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name
    # def full_name(self):
    #     self.full_name = full_name
    def full_name(self):
        # self.full_name = full_name
        print(self.first_name,self.family_name)


# ken.full_name = ken.first_name,ken.family_nameとするものを定義すればいいが、このものってなんというのだ。


ken = Customer(first_name="Ken", family_name="Tanaka")
# print(ken.first_name,ken.family_name)
ken.full_name()

# # 実体化
# tanaka = UserName(name='tanaka')
#
# # 出力
# print(tanaka)

#
#
# class Full:
#     full_name = Full()
#     ken = Customer(first_name="Ken", family_name="Tanaka")
#
# print(ken.full_name)
#
# # "Ken Tanaka" という値を返す
#
# tom = Customer(first_name="Tom", family_name="Ford")
# tom.full_name()
# # "Tom Ford" という値を返す