import pandas
import os

infilename = "C:\\Git\\source\\repos\\Tom\\CovidDataTransformerPy\\data\\covid_data.csv"
outfilename = "C:\\Git\\source\\repos\\Tom\\CovidDataTransformerPy\\data\\output.csv"

fieldnames = ['date', 'region', 'number']
csvfile = pandas.read_csv(infilename, usecols=fieldnames)
csvdates = list(dict.fromkeys(csvfile.date.values))  # use dict to get unique
csvregions = list(dict.fromkeys(csvfile.region.values))

# add header row to output.csv
if not os.path.isfile(outfilename):
    with open(outfilename, mode='w', encoding='utf-8') as f:
        f.write('date' + ',')
        for region in csvregions:
            f.write(region)
            if not csvregions.index(region) == len(csvregions) - 1:
                f.write(',')
        f.write('\n')

outputrowobjects = []

# pre-populate the output row objects with dates and region pairs
for date in csvdates:
    newrowobj = type("", (object,), {"date": date, "regionPairs": []})
    for region in csvregions:
        regionpair = type("", (object,), {"region": region, "number": "-"})
        newrowobj.regionPairs.append(regionpair)
    outputrowobjects.append(newrowobj)

# loop through csv to fill in outputrowobjects
for i, inrow in csvfile.iterrows():
    numberadded = False
    for outrow in outputrowobjects:
        if outrow.date == inrow.date:
            for regionpair in outrow.regionPairs:
                if regionpair.region == inrow.region:
                    regionpair.number = inrow.number
                    numberadded = True
                    break
        if numberadded:
            break

# outputrowobjects to output.csv
with open(outfilename, mode='a+', encoding='utf-8') as f:
    for row in outputrowobjects:
        f.write(row.date + ',')
        for pair in row.regionPairs:
            f.write(str(pair.number))
            if not row.regionPairs.index(pair) == len(row.regionPairs) - 1:
                f.write(',')
        f.write('\n')
