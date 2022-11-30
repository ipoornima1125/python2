
a=int(input("enter first no.:"))
b=int(input("enter second no.:"))
c=int(input("enter third no.:"))
avg= a+b+c/3
print(avg)


gross_income=int(input(" salary:"))
number_of_dependents=int(input(" dependents:"))
standard_deduction= 10000
dependent_deduction=3000
tax_rate= 0.2
taxable_income= gross_income - standard_deduction-(dependent_deduction*number_of_dependents)
Tax= taxable_income*tax_rate
print("tax is:",Tax)



time = int(input(' time:'))
minutes=time//60
seconds=time%60
print(minutes)
print(seconds)

a=25
b='25'
c=25.0


result=a +int( b)+int( c)
str( result)
print(result)




import math

for item in range(0,345,15):

    print(item,"....",round(math.sin(math.radians(item)),4),"   ",round(math.cos(math.radians(item)),4))



    


