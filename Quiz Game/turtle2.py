# from turtle import Turtle
# from turtle import Screen
import random
import turtle as tim
import colorgram

timmy=tim.Turtle()

# timmy.shape("circle")
# timmy.color("black","red")
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timimy.right(90)
# timmy.forward(100)
# for i in range(3,11):
#     num_sides=i
  #   c=["red","blue","green","cyan","magenta","black"]
  #   color=random.choice(c)  
    # timmy.pencolor(color)
#     for i in range(num_sides):

#         angle=360/num_sides
#         timmy.forward(100)
#         timmy.right(angle)
  

# c=["red","blue","green","cyan","magenta","black"]
# color=random.choice(c)  
# direction=[0,90,180,270]
# # rgb=(r,g,b)


# for i in range(200):
#     timmy.speed(10)
#     timmy.pensize(10) 
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))    

# timmy.speed("fastest")
# for _ in range(100):
#   timmy.color(random_color())
#   timmy.circle(100)
#   c_heading=timmy.heading()
#   timmy.setheading(c_heading+10)
#   timmy.circle(100)




# turtle.colormode(255)
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     rgb=(r,g,b)
#     return rgb
# rgb_colors=[]
# colors=colorgram.extract("20_001.jpg",25)
# for color in colors:
#   r=color.rgb.r
#   g=color.rgb.g
#   b=color.rgb.b
#   new=(r,g,b)
#   rgb_colors.append(new)
tim.hideturtle()
# print(rgb_colors)
tim.penup()
tim.colormode(255)
color_list=[ (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots=100
tim.speed(10)
for i  in range(1,no_of_dots+1):
  c=random.choice(color_list)
  tim.dot(20,c)
  tim.forward(50)
  if i % 10==0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    
screen=timmy.Screen()
screen.exitonclick()