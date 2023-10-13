from array_list_home_task.array_list import ArrayList

array = ArrayList()
array.load_from_file('D:\\Python\\AcademIT_oop\\array_list_home_task\\list.dat')
print('Array:', array)

list_without_repetitions = array.remove_repetitions()
print('Array without repetitions:', list_without_repetitions)

array.remove_even_numbers()
print('Array after remove even numbers:', array)
