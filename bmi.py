height=input()
weight=input()
#converting the inputs into integer
weight_as_int=int(weight)
height_as_float=float(height)
bmi=int(weight_as_int/(height_as_float**2))
print(bmi)