name = "炭治郎"
item = "みかん"
number = 10
price = 50
tax_rate = 0.1
total = number*price
tax = total*tax_rate
pay = total+tax

print(name,'さんこんにちは。')
print(name,'さんが購入した商品は')
print(name,'さんが好きな',item,number,'個です。')
print(name,'さんの購入金額は',total,'円です。')
print(name,'の購入金額の消費税は',tax,'円です。')
print(name,'さんのお支払い金額は',pay,'円です。')
print(name,'さん、ありがとうございました。')

print("{}さんこんにちは。".format(name))
print("{}さんが購入した商品は。".format(name))
print("{}さんが好きな{}{}個です。".format(name,item,number))
print("{}さんの購入金額は{}円です。".format(name,total))
print("{}の購入金額の消費税は{:.0f}円です。".format(name,tax))
print("{}さんのお支払い金額は{:.0f}円です。".format(name,pay))
print("{}さん、ありがとうございました。".format(name))

my_list=[11,22,33,44,55,66,77,88,99,100]
print(my_list[0],my_list[1],my_list[4],sep=',')
print(my_list[2:5],my_list[1:7],my_list[0])
print(my_list[:8],my_list[0:8],my_list[5:],sep=',')
#全取得
print(my_list[:])
#最後の一桁ずつ取り出すという意味
print(my_list[0:5:2])

my_list2 =['A','B','c']
my_list2.append('D')
print(my_list2[:])
#appendで2つ追加するとエラーが発生する
#my_list2.append('E','F')
print(my_list2[:])

colors = ['red', 'green', 'blue']
r = colors[0]
g = colors[1]
b = colors[2]

print('赤:{},緑:{},青:{}'.format(r,g,b))

aa=['赤','緑','青']

print('{}:{},{}:{},{}:{}'.format(aa[0],r,aa[1],g,aa[2],b))

# age = input('年齢は？')


# if int(age) == 20:
#     print('成人式')
# elif int(age) == 30:
#     print('30歳')
# elif int(age) == 40:
#     print('40歳ね')
# elif int(age) < 20:
#     print('未成年')    
# else:
#     print('成人式ではない')



# 年齢が15未満なら「炭治郎じゃないね、まだ子供だね」と応える
# 年齢が20以上で80までなら「炭治郎じゃないね、大人だね」と応える
# 年齢が81以上で150までなら「炭治郎じゃないね、それにしても長生きだね」と応える
# 年齢が151以上なら「出たな鬼！」と応える


name = input('お名前は？')
age = int(input('年齢は？'))

if name=='炭治郎' and age == 15:
    print('やあ、炭治郎')
elif name != '炭治郎':
    print('誰・・・？')
elif age < 15:
    print('炭治郎じゃないね、まだ子供だね')
elif age < 20:
    print('炭治郎じゃないね、でも仲間だね。')
elif age >= 20 and age <= 80:
    print('炭治郎じゃないね、大人だね')
elif age > 80 and age <= 150:
    print('炭治郎じゃないね、それにしても長生きだね')
elif age > 150:
    print('出たな鬼！')