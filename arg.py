import argparse

parser = argparse.ArgumentParser(description="Our example parser")
parser.add_argument("--filename","-f",required=True,)
parser.add_argument("--medals", action="store_true", require=False)
parser.add_argument("--output", "-o", require=False)
parser.add_argument("--year", "-y", require=False)
parser.add_argument("--total", "-t", require=False)
parser.add_argument("--team",  require=False)

args = parser.parse_args()

def task1(filename,country,year,output):
    gold = 0
    silver = 0
    bronze = 0
    i = 0
    res = ''
    res_list = ''


    while True:
        line = filename.readlines()
        if not line : break

        information = line.split("\t")
        _year=information[7]
        _medals=information[12]
        _team=information[5]
        _sport=information[10]
        _NOC=information[6]
        _name=information[1]
        if year == _year:
            if country == _NOC or country == _team :
                if _medals != 'NA\t':
                    list = (f"{_name},{_sport},{_medals}")
                    if _medals == 'Gold\n':
                        gold += 1
                    if _medals == 'Silver\n':
                        silver += 1
                    if _medals == 'Bronze\n':
                        bronze += 1


                    total = (f'Medals: {gold},{silver},{bronze}')
                    res = res_list.join(list)
                    i += 1

                    if i == 10:
                        print(res)
                    if output:
                        with open(filename, "w") as file:
                            file.write(f"{total}\n ")







