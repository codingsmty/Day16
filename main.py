
#from turtle import Turtle, Screen
#
#timmy = Turtle()
#timmy.shape("turtle")
#timmy.color("darkgreen")
#
#My_Screen = Screen()
#print(My_Screen.canvheight)
#My_Screen.delay(2)
#timmy.forward(100)
#print(timmy)


#import PrettyTable
#table = prettytable
#print(table)
#table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
#


from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5],)
table.add_row(["Hobart", 1357, 205556, 619.5],)
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.align["City name"] = "l"
table.align = "c"
print(table)