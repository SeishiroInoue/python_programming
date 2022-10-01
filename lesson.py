func = lambda x, y: print(f'{x}さんは{y}です')
func('鈴木','学生')

n1 = ['鈴木','斎藤','田中']
n2 = ['めい','ゆづき','ひなた']
result = list(map(lambda x,y:x+y+'さん',n1,n2))
print(result)

numbers =[5,8,10,12,15]
result = list(filter(lambda x:x>=10,numbers))
print(result)

x = [i for i in range(6)]
print(x)

names = ['鈴木','斎藤','田中']
x = [i+'さん' for i in names]
print(x)

x = [i for i in range(11) if i%2 != 0]
print(x)

foods = ['apple','banana','lemon']
x = [i for i in foods if 'a' in i]
print(x)

x1 = [i for i in range(6)]
x2 = ['ぐ' if i%2 == 0 else i for i in range(6)]
print(x1)
print(x2)

kanto = ['千葉','栃木','東京','埼玉','茨城','群馬','神奈川']
x = [i+'都' if i == '東京' else i+'県' for i in kanto]
print(x)