def AddEmployee(employee, employee_list = []):
   employee_list.append(employee)
   return employee_list

print("default argument are : ",AddEmployee.__defaults__)

print(AddEmployee("Hanouda"))
print("default argument are : ",AddEmployee.__defaults__)

print(AddEmployee("Hindati"))
print("default argument are : ",AddEmployee.__defaults__)

print ("################## Late Binding Closures (or in the surrounding global scope) ########")
# Another common source of confusion is the way Python binds its variables in closures (or in the surrounding global scope).
def create_multipliers():
    return [lambda x, i = i : i * x for i in range(5)]

multi = create_multipliers()
for multiplier in multi:
    print(multiplier(2))

# the problem is with lambda
def simple_create_multipliers():
    list_fct = []
    for i in range(5):
        def fn(x):
            return x*i
        list_fct.append(fn)
    return list_fct

for multii in simple_create_multipliers():
    print(multii(2))

