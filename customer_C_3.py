class Customer:
    def __init__(self, first_name, family_name,age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age
    def full_name(self):
        print(self.first_name,self.family_name)
    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif 20 <= self.age < 60:
            return 1500
        else :
            return 1200

# なぜ年齢が出てくる？？？？？？？？？？場所がおかしい？ということはQ2は間違い？

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.entry_fee())


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

