'''nm= [1,2,3,4,5]
def square(n):
    return n*n

sqrd_n= map(square, nm)
print(list(sqrd_n))'''

'''l3= ['apple','cherry','banana','date']
def even1(ist):
    for n in ist:
        x=len(n)
        if x%2==0:
            return(n)

l4 = even1(l3)
print(l4)'''

l3 = ['apple', 'cherry', 'banana', 'date']

'''def even1(lst):
    even_list=[]
    for n in lst:
        x = len(n)
        if x % 2 == 0:
            even_list.append(n)
    return even_list

l4 = even1(l3)
print(l4)'''

'''list_2= ['banana','apple','tarbooz','Malta', 'Nashpati','AARO']
def even_words(e):
    even_words1=[]
    for i in e:
        v=len(i)
        if v%2==0:
            even_words1.append(i)
    return even_words1

b= even_words(list_2)
print((b))   '''  

'''#lambda usage
lambda a:a+1
lambda b,c: b+c

kp= ['kaa','kok','kkol','lool','loop']
kp_1=[x for x in kp if len(x)==4]
print(kp_1)
'''
'''contacts = {"Noah": "166 5968014","Emma": "167 4668754","Oliver": "155 6178788","Charlotte": "178 8047640","Elijah": "166 7160871","Amelia": "170 8099931",r"James": "159 9219533","Ava": "145 7395303"}
a_h_names = {name: number for name, number in contacts.items() if name[1] < "H"}
print(a_h_names.keys())'''

'''def is_healthy(food):
    healthy_food = ["Apple", "Apricot", "Araza", "Avocado", "Banana","Bilberry", "Blackberry", "Blackcurrant"]
    return True if food in healthy_food else False
snack = ["Apple", "Coca Cola", "Avocado", "Chips"]
healthy_sanck = filter(is_healthy, snack)
print(healthy_sanck)'''

file_name= Exercise_1
with open(file_name,r):
    v=input('Enter line 1')
    x=input('Enter line 2')
