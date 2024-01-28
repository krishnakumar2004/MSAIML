list1 = [5 , 7, 8, 9, 10, 12]

print(sum(list1))

name_age_dict1 = {'John':'35' , 'Jerry':'25' , 'Charles': '45' , 'Nancy':'55' , 'Celina':'38' , 'Jenn':'48'}

print(name_age_dict1)
name_age_dict1.update({'test': 70})
print('After update method',name_age_dict1)
name_age_dict1.pop('Celina')
print('After pop method',name_age_dict1)
name_age_dict1.clear()
print('After clear method',name_age_dict1)

points_list = [5 , 9]

print('Initial points_list',points_list)
points_list.append(6)
print('After append',points_list)
points_list.pop()
print('After pop method',points_list)
points_list.insert(1,15)
print('After insert method',points_list)
points_list.remove(9)
print('After remove method',points_list)
