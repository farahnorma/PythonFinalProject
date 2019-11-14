# Norma
# Historic_Dates.py


import datetime


def getCommand():
    command = input("Enter option: ")
    return command


def find_event(file):
    database = 'Database.txt'
    file = open(database, 'r+')
    y = str(input("Enter full year (1999, 1, 200, etc): "))
    ab = str(input("Enter AD or BC: ")).upper()
    m = str(input("Enter month (January, February, etc): ")).upper()
    d = str(input("Enter day (1-31): "))
    print("The date received is: ", m," ",d,",", y,ab)
    print("Is this correct?")
    correct = str(input("y/n    "))
    if correct is "y":
        for line in file:
            aline = line.split()
            line = line.rstrip()
            if y in line and ab in line and m in line and d in line:
                aline1 = aline[0].replace('-', ' ')
                aline2 = aline[1].replace('-', ' ')
                print("\n",aline1,"occurs on",aline2,"\n")
    elif correct is "n":
        print("Try again")
    else:
        print("Not an answer")


def find_date(file):
    database = 'Database.txt'
    file = open(database, 'r+')
    print("\n~The events on file are:\n")
    for aline in file:
        values = aline.split()
        v = values[0].replace('-', ' ')
        v1 = values[1].replace('-', ' ')
        print("Event: ", v, "\n Date: " , v1, '\n')


def write(file):
    file.close()
    database = 'Database.txt'
    file = open(database, 'a')
    e = str(input("Enter a description of the event: ")).replace(' ', '-').upper()

    m = str(input("Enter the month (January, February, etc) :")).upper()
    d = str(input("Enter the day (1-31): "))
    y = str(input("Enter the full year (1999, 1, 200, etc): "))
    ab = str(input("Enter either AD or BC: ")).upper()

    wr = e+' '+m+'-'+d+',-'+y+ab
    file.write( '\n'+wr)

    file.close()


def main():
    database = 'Database.txt'
    file = open(database, 'r+')

    while True:
        print("Options: ")
        print("'F' => Find the event associated with a specific date")
        print("'D' => Display all events and corresponding dates on file")
        print("'A' => Add an event and date to the database")
        print("'Q' => Quit the program")

        cmd = getCommand().upper()[0]

        if cmd is 'F':
            find_event(file)
        elif cmd is 'D':
            find_date(file)
        elif cmd is 'A':
            write(file)
        elif cmd is 'Q':
            break
        else:
            print("Unknown command: %s => try again." % cmd)

    print("Exited program on", datetime.datetime.now())
    file.close()


main()

