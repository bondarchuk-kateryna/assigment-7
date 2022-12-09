def task1(filename,country,year):
    head = None
    is_first_line = True
    with open(filename,"r") as file:
        for line in file.readlines():
            if is_first_line:
                head = line.split("\t")
                is_first_line = False
                continue

            head.index("NOC")


task1("data.csv", "USA", "1996")


print("Katya loh")
