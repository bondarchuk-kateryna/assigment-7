import argparse

parser = argparse.ArgumentParser(description="Our example parser")
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


task1('data.tsv','USA','1998')

def task3(overall,filename):
    lines = filename.readlines()
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

    if interactive is not None:
        inputText = ""
        while(inputText != "exit"):
            foundCountry = False
            inputText = input("Input name/code Country: ")
            if inputText == "exit":
                break
            firstTakePartYear = 2022
            firstTakePartCity = ""
            countMedalYear = {}
            countMedalOlymp = {}
            for line in lines:
                command = line.split('\t')
                if inputText in command[6] or inputText in command[7]:
                    foundCountry = True
                    #1
                    if int(command[9]) <  firstTakePartYear:
                        firstTakePartYear = int(command[9])
                        firstTakePartCity = command[11]
                    #2-3
                    keys = countMedalYear.keys()
                    if command[9] in keys:
                        if "Gold" in command[14] or "Bronze" in command[14] or "Silver" in command[14]:
                            countMedalYear[command[9]] +=1
                    else:
                        countMedalYear[command[9]] = 0
                    #4
                    keys = countMedalOlymp.keys()
                    if command[9] not in keys:
                        countMedalOlymp[command[9]] = {"Gold":0, "Bronze":0, "Silver":0, "countGames":0}
                    if command[9] in keys:
                        if "Gold" in command[14]:
                            countMedalOlymp[command[9]]["Gold"] +=1
                        if "Bronze" in command[14]:
                            countMedalOlymp[command[9]]["Bronze"] +=1
                        if "Silver" in command[14]:
                            countMedalOlymp[command[9]]["Silver"] +=1
                        countMedalOlymp[command[9]]["countGames"] +=1
                    # print(command)
            if foundCountry == False:
                print("Country",inputText," is not find!")
                line_to_write+="Country "+inputText+" is not find!"+"\n"
            else:
                print("\tCountry: ", inputText)
                line_to_write+="\tCountry: "+inputText+"\n"
                #1
                print("\tFirst take party: ", firstTakePartYear, firstTakePartCity)
                line_to_write+="\tFirst"

