
class Customer:
    def __init__(self, first_name, family_name,age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age
    def full_name(self):
        print(self.first_name,self.family_name)
        print(self.age)
    def entry_fee(self,entry_fee):
        self.entry_fee = entry_fee
        if age < 20 :
            self.entry_fee = 1,000
            print(self.entry_fee)
        elif 20<= age < 60:
            self.entry_fee = 1,500
            print(self.entry_fee)
        elif age >= 65:
            self.entry_fee = 1,200
            print(self.entry_fee)
        # if self.age < 20 :
        #     self.entry_fee = 1,000
        #     print(self.entry_fee)
        # elif 20<= self.age < 60:
        #     self.entry_fee = 1,500
        #     print(self.entry_fee)
        # elif self.age >= 65:
        #     self.entry_fee = 1,200
        #     print(self.entry_fee)

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.entry_fee
# なぜ年齢が出てくる？？？？？？？？？？場所がおかしい？ということはQ2は間違い？
# 今度はなにもでてこない、、、、なぜだ・・・
#　エラーが何も出てこないと、どうしらよい？？考え方の切り口が少なすぎる。
# 定義の位置が悪いのか？

# 1000 という値を返す

# 料金の計算ルール entry_fee
# こども料金(20歳未満): 1000円
# age < 20 →　entry_fee 1,000
#
# # おとな料金(20歳以上65歳未満): 1500円
# 20<= age < 60 →　entry_fee 1500
#
# # シニア料金(65歳以上): 1200円
# age <= 65 →　entry_fee 1200

