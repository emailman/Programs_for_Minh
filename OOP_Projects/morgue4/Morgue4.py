from OOP_Projects.morgue4.Shared import *
from OOP_Projects.morgue4.Intake import intake
from OOP_Projects.morgue4.Inventory import inventory
from OOP_Projects.morgue4.Discharge import discharge


def main():

    Text(app, text="")
    PushButton(app, text="    I n t a k e     ",
               command=intake)

    Text(app, text="")
    PushButton(app, text="D i s c h a r g e",
               command=discharge)

    Text(app, text="")
    PushButton(app, text="I n v e n t o r y",
               command=inventory)

    Text(app, text="")
    PushButton(app, text="       E x i t         ",
               command=exit)

    app.display()


main()
