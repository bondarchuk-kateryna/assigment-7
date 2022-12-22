import argparse
import sys


parser = argparse.ArgumentParser(description="Our example parser")
parser.add_argument("--filename","-f",required=True,)
parser.add_argument("--medals", action="store_true", required=False)
parser.add_argument("--output", "-o", required=False)
parser.add_argument("--year", "-y", required=False)
parser.add_argument("--total", "-t",action="store_true", required=False)
parser.add_argument("--team", required=False)
parser.add_argument("--interactive", "-i" , action="store_true",required=False)
parser.add_argument("--overall",action="store_true", required=False)

args = parser.parse_args()
team = args['team']
year = args['year']
filename = args['filename']
medals = args['medals']
output = args['output']
total = args['total']
overall = args['overall']
interactive = args['interactive']
file = open("filename","r")

def main():

    if not args.filepath:
        parser.print_help()
        sys.exit(1)
    if args.medals:
        task1(args.filename, args.medals, args.output)
    elif args.total:
        task2(args.filename, args.total, args.output)
    elif args.overall:
        task3(args.filename, args.overall, args.output)
    elif args.interactive:
        task4(args.filename)

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
        _year=information[9]
        _medals=information[14]
        _team=information[6]
        _sport=information[12]
        _NOC=information[7]
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

def task2(filename,total):
    total = 0
    line_to_write=""

    lines = filename.readlines()

    if total is not None:
        year = total
        country = {}
    for line in lines:
        lines = filename.readlines()
        command = lines.split('\t')
        if year in command[9]:
            keys = country.keys()
            if command[6] in keys:
                if "Gold" in command[14]:
                    country[command[7]]["Gold"] +=1
                if "Bronze" in command[14]:
                    country[command[7]]["Bronze"] +=1
                if "Silver" in command[14]:
                    country[command[7]]["Silver"] +=1
                if "NA" in command[14]:
                    country[command[7]]["NA"] +=1
            else:
                country[command[6]] = {"Gold":0, "Bronze":0, "Silver":0, "NA":0}

    for c in country.items():
        if c[1]["Gold"] > 0 or c[1]["Bronze"] > 0 or c[1]["Silver"]:

            print("{:<20}".format(c[0]),"{:<10}".format(c[1]["Gold"]),"{:<10}".format(c[1]["Silver"]),"{:<10}".format(c[1]["Bronze"]))
            line_to_write+=c[0]+"\t"+str(c[1]["Gold"])+"\t"+str(c[1]["Silver"])+"\t"+str(c[1]["Bronze"])+"\n"

def task3(overall,file):
    lines = file.readlines()
    for country in overall:
        countMedalYear = {}
        for line in lines:
            command = line.split('\t')
            if command[7] == country:
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

def task4(filename):
    lines = filename.readlines()
    line_to_write = ""
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
                    #cтатистика першої участі в олімпіаді
                    if int(command[9]) <  firstTakePartYear:
                        firstTakePartYear = int(command[9])
                        firstTakePartCity = command[11]
                    #найуспішніша,найневдаліша олімпіада за кількістю медалей
                    keys = countMedalYear.keys()
                    if command[9] in keys:
                        if "Gold" in command[14] or "Bronze" in command[14] or "Silver" in command[14]:
                            countMedalYear[command[9]] +=1
                    else:
                        countMedalYear[command[9]] = 0
                    #середня кількість медалей
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
                #виведення
                print("\tFirst take party: ", firstTakePartYear, firstTakePartCity)
                line_to_write+="\tFirst"
                take_party = "str(firstTakePartYear)"  "firstTakePartCity" "\n"
            #виведення
            maxCountMedalYear = 0
            maxCountMedal = 0
            minCountMedalYear = 0
            minCountMedal = 100
            for count in countMedalYear:
                if int(countMedalYear[count]) > maxCountMedal:
                    maxCountMedal = countMedalYear[count]
                    maxCountMedalYear = count
                if int(countMedalYear[count]) < minCountMedal:
                    minCountMedal = countMedalYear[count]
                    minCountMedalYear = count
            print("\tSuccess olymp: ",maxCountMedalYear, maxCountMedal)
            line_to_write+="\tSuccess olymp: "+str(maxCountMedalYear)+" "+str(maxCountMedal)+"\n"
            print("\tFailed olymp: ",minCountMedalYear, minCountMedal)
            line_to_write+="\tFailed olymp: "+str(minCountMedalYear)+" "+str(minCountMedal)+"\n"

            #виведення
            print("\tAvarage type medal for olymp")
            line_to_write+="\tAvarage type medal for olymp"+"\n"
            print("\t Year Gold Bronze Silver")
            line_to_write+="\t Year Gold Bronze Silver"+"\n"
            for olymp in countMedalOlymp:
                Gold = countMedalOlymp[olymp]["Gold"]
                Bronze = countMedalOlymp[olymp]["Bronze"]
                Silver = countMedalOlymp[olymp]["Silver"]
                countGames = countMedalOlymp[olymp]["countGames"]
                print("\t",olymp, Gold/countGames, Bronze/countGames, Silver/countGames)
                line_to_write+="\t"+olymp+" "+str(Gold/countGames)+" "+str(Bronze/countGames)+" "+str(Silver/countGames)+"\n"
            if output is not None:
                f = open(output, "w")
                f.write(line_to_write)
                f.close()
                print('Output in save file:', output)


main()
