import pandas

infilename = "C:\\Git\\source\\repos\\Tom\\CovidDataTransformerPy\\data\\covid_data.csv"
outfilename = "C:\\Git\\source\\repos\\Tom\\CovidDataTransformerPy\\data\\output.csv"

fieldnames = ['date', 'region', 'number']

csvfile = pandas.read_csv(infilename, usecols=fieldnames)
csvdates = list(dict.fromkeys(csvfile.date.values))  # use dict to get unique
csvregions = list(dict.fromkeys(csvfile.region.values))

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

# add header row to output.csv
