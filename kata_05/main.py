shopping_list = []
while True:
    print('Что добавим в список покупок?') 
    print('(для завершения введите "выход")')
    enter = input()
    if enter == 'выход':
        break
    else:
        shopping_list.append(enter)
print("Ваш список покупок:")
for i in shopping_list:
    print(i)