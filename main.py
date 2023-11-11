import turtle
t = turtle.Pen()

def rechtecke():
    t.reset()
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    turtle.exitonclick()
# def herz():
#
#
# def haus():


def menu():
    return """
    Wählen Sie eine Zeichnung aus:
    1 - 2 Rechtecke
    2 - Herz
    3 - 2 Häuser
    0 - exit"""
def main():
    while True:
        print(menu())
        opt = int(input("option "))
        if opt == 1:
            print(rechtecke())
        # if opt == 2:
        #     print(herz())
        # if opt == 3:
        #     print(haus())
        if opt == 0:
            t.reset()
            break
main()
