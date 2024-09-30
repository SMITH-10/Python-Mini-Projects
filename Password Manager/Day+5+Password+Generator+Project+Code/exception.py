# try:
#     file=open("a_file.txt")
#     a={"key":"value"}
# except FileNotFoundError:
#     file=open("a_file.txt","w")
# except KeyError as errormessage:
#     print(f"The key {errormessage} does not exist.")
# else:
#     content=file.read()
#     print(content)
# finally:
#    raise KeyError("This error is made up")


height=float(input("Height: "))
weight=int(input("Height: "))
if height > 3:
    raise ValueError("Human  height must be less than 4 meters")
bmi=weight/(height*height)
print(bmi)
