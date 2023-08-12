#python example
var1 = 1

var2 = "2"

var3 = [1, 2, 3]

var4 = [1, "2", [1, 2, 3]]

person2 = "personName"

var5 = {
        "person1": "hants",
        "person2": person2
}

var5

type(var5)

type(var3)



number = 5

if number <= 10: 
    print('this is a small number')
else: 
    print('this is a bigger number')


listofNames = ['a', 'b', 'c']

if listofNames[0] != 'a':
    print('ok')
else:
    print('9')

bloodPressure=125
if bloodPressure<=100:
    print('blood presure good', bloodPressure)
elif bloodPressure == 140:
    print('okk')
elif bloodPressure > 200:
    print('high')
else:
    print('yes')


bloodPressure_systolic = 125 
if bloodPressure_systolic <= 100: 
    print('your blood pressure is good, its at: ', bloodPressure_systolic) 
    pointsBelowConerning = 140 - bloodPressure_systolic
    print('you have this many points left before concerning value: ', pointsBelowConerning)
elif bloodPressure_systolic > 100 and bloodPressure_systolic <= 120:
    print('your blood pressure is still healthy, at ', bloodPressure_systolic)
    pointsBelowConerning = 140 - bloodPressure_systolic
    print('you have this many points left before concerning value: ', pointsBelowConerning)
elif bloodPressure_systolic > 120 and bloodPressure_systolic <= 139: 
    print('your blood pressure is a little concerning at: ', bloodPressure_systolic)
    pointsBelowConerning = 140 - bloodPressure_systolic
    print('you have this many points left before concerning value: ', pointsBelowConerning)
else: 
    print('your blood pressure is hypertensive at: ', bloodPressure_systolic)
    pointsBelowConerning = 140 - bloodPressure_systolic
    print('you have this many points left before concerning value: ', pointsBelowConerning)