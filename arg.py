import argparse

parser = argparse.argumentparser(description="Our example parser")
parser.add_argument("--filename","-f",required=True,)
parser.add_argument("--medals", action="store_true", require=False)
parser.add_argument("--output", "-o", require=False)
parser.add_argument("--year", "-y", require=False)
parser.add_argument("--total", "-t", require=False)
parser.add_argument("--team", require=False)

args = parser.parse_args()
filename = args['filename']
medals = args['medals']
output = args['output']
total = args['total']
overall = args['overall']
interactive = args['interactive']
file= open("filename","r")
def task1(filename,country,year,output):
    gold = 0
    silver = 0
    bronze = 0
    i = 0
    res = ''
    res_list = ''


    while True:
        line = file.readline()
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


task1('data.tsv','USA','1998')

def task2(filename,country,year,output):
    total = 0
    line = file.readline()
    information = line.split("\t")
    _year=information[7]
    _medals=information[12]
    _team=information[5]
    _sport=information[10]
    _NOC=information[6]
    _name=information[1]
    line = filename.readlines()
    line_to_write=""

    if total is not None:
        year = total
        country = {}
    for line in line:
        command = line.split('\t')
        if year in command[9]:
            keys = country.keys()
            if command[6] in keys:
                if "Gold" in command[14]:
                    country[command[6]]["Gold"] +=1
                if "Bronze" in command[14]:
                    country[command[6]]["Bronze"] +=1
                if "Silver" in command[14]:
                    country[command[6]]["Silver"] +=1
                if "NA" in command[14]:
                    country[command[6]]["NA"] +=1
            else:
                country[command[6]] = {"Gold":0, "Bronze":0, "Silver":0, "NA":0}

    for c in country.items():
        if c[1]["Gold"] > 0 or c[1]["Bronze"] > 0 or c[1]["Silver"]:
            # print(c)
            print("{:<20}".format(c[0]),"{:<10}".format(c[1]["Gold"]),"{:<10}".format(c[1]["Silver"]),"{:<10}".format(c[1]["Bronze"]))
            line_to_write+=c[0]+"\t"+str(c[1]["Gold"])+"\t"+str(c[1]["Silver"])+"\t"+str(c[1]["Bronze"])+"\n"

def task3(overall,file):
    lines = file.readlines()
    overall = 0
    line_to_write = ""
    if overall is not None:
        print(overall)
        line_to_write+="Country"+"\t"+"Year"+"\t"+"max Count Medal"+"\n"
    for country in overall:
        countMedalYear = {}
        for line in lines:
            command = line.split('\t')
            if command[6] == country:
                keys = countMedalYear.keys()
                if command[9] in keys:
                    if "Gold" in command[14] or "Bronze" in command[14] or "Silver" in command[14]:
                        countMedalYear[command[9]] +=1
                else:
                    countMedalYear[command[9]] = 0
        Year = 0
        maxCountMedal = 0
        for count in countMedalYear:
            if countMedalYear[count] > maxCountMedal:
                maxCountMedal = countMedalYear[count]
                Year = count
        print(country, Year, maxCountMedal)
        line_to_write+=country+"\t"+str(Year)+"\t"+str(maxCountMedal)+"\n"

