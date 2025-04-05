print("Enter your marks from your subjects :")
m=int(input("Maths:"))
eng=int(input("English:"))
sci=int(input("Science:"))
avg=(m+eng+sci)/3
print("your average is", avg)
if avg>=90:
    print("you are an A grade Student")
elif avg>=80 and avg<90:
    print("you are a B grade Stundent")
elif avg>=70 and avg<80:
    print("you are a C grade Student")
elif avg>=60 and avg<70:
    print("you are a D grade Student")
elif avg>=50 and avg<60:
    print("you are a E student")
else:
    print("you are a failing student")