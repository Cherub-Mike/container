def age_calculator(ages, sub):
    return int(sub) - int(ages)

sub =100
age= int(input('enter your age: '))
call = age_calculator(age,sub)
print("you have",call ,'more years to turn',sub)
