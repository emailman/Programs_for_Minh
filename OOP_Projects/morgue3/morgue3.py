from guizero import *

# Global widgets
app = None
tbx_delete_id = None
win_discharge = None
btg_gender = None

# Global list
bodies = []


class Corpse:
    count = 0

    def __init__(self, gender):
        Corpse.count += 1
        self.index = Corpse.count
        self.gender = gender
        if gender == "M":
            self.name = "John Doe"
        else:
            self.name = "Jane Doe"

    def __str__(self):
        return str(self.index) + " : " + self.gender + " : " +\
               self.name


def add():
    yes_no = yesno(title="The Morgue", text="OK to add")
    if yes_no:
        bodies.append(Corpse(btg_gender.value))
        info(title="The Morgue", text="Added")
    else:
        info(title="The Morgue", text="Not Added")


def remove():
    try:
        delete_id = int(tbx_delete_id.value)
        index_id = None
        found = False
        gone = None
        for each in bodies:
            if delete_id == each.index:
                index_id = bodies.index(each)
                gone = each
                found = True
                break

        if found:
            yes_no = yesno(title="The Morgue",
                           text="Confirm discharging id " + str(gone))
            if yes_no:
                del bodies[index_id]
                win_discharge.destroy()
        else:
            error(title="The Morgue", text="ID not found")
    except ValueError:
        error(title="The Morgue", text="ID must be an integer")


def intake():
    global btg_gender

    win_intake = Window(app, title="Intake",
                        height=280, width=400, layout="grid")
    win_intake.show(wait=True)

    Text(win_intake, text=10 * " ", grid=[0, 0])

    btg_gender = ButtonGroup(win_intake,
                             options=[
                                 ["Male", "M"],
                                 ["Female", "F"]
                             ], grid=[1, 1])

    Text(win_intake, text="Name", align="left", grid=[1, 5])
    TextBox(win_intake, width=30, align="left", grid=[2, 5])

    Text(win_intake, text="Age", align="left", grid=[1, 7])
    TextBox(win_intake, width=3, align="left", grid=[2, 7])

    Text(win_intake, text="Height", align="left", grid=[1, 9])
    TextBox(win_intake, width=5, align="left", grid=[2, 9])

    Text(win_intake, text="Weight", align="left", grid=[1, 11])
    TextBox(win_intake, width=5, align="left", grid=[2, 11])

    Text(win_intake, grid=[1, 12])

    PushButton(win_intake, text="  A d d  ", align="left",
               grid=[1, 13], command=add)

    PushButton(win_intake, text=" E x i t ", align="right",
               grid=[2, 13], command=win_intake.destroy)


def discharge():
    global tbx_delete_id, win_discharge

    win_discharge = Window(app, title="Discharge",
                           height=300, width=300,
                           layout="grid")
    win_discharge.show(wait=True)

    Text(win_discharge, text=10 * " ", grid=[0, 0])
    Text(win_discharge, text="ID : Gender : Name",
         align="right", grid=[1, 1])

    report = ""
    for each in bodies:
        report += str(each) + "\n"

    Text(win_discharge, text=report, grid=[1, 3])

    Text(win_discharge, text="Enter ID to Delete ",
         align="right", grid=[1, 5])
    tbx_delete_id = TextBox(win_discharge,
                            align="left", grid=[2, 5])

    Text(win_discharge, grid=[1, 6])

    PushButton(win_discharge, text=" D e l e t e ",
               grid=[1, 7], command=remove)
    PushButton(win_discharge, text=" E x i t ", grid=[2, 7],
               command=win_discharge.destroy)


def inventory():
    win_inventory = Window(app, title="Inventory",
                           height=300, width=300,
                           layout="grid")
    win_inventory.show(wait=True)

    Text(win_inventory, text=10 * " ", grid=[0, 0])
    Text(win_inventory, text="Bodies in morgue: " +
                             str(len(bodies)),
         align="right", grid=[1, 1])

    report = ""
    for each in bodies:
        report += str(each) + "\n"

    Text(win_inventory, text=report, grid=[1, 3])

    PushButton(win_inventory, text=" E x i t ", grid=[1, 5],
               command=win_inventory.destroy)


def main():
    global app, bodies

    app = App(title="Welcome to the Morgue",
              height=300, width=300)

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
