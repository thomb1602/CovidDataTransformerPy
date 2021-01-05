import pandas

infilename = "C:\\Git\\source\\repos\\Tom\\CovidDataTransformerPy\\data\\covid_data.csv"
outfilename = "C:\\Git\\source\\repos\\Tom\\CovidDataTransformerPy\\data\\output.csv"

csvfile = pandas.read_csv(infilename, usecols=['date', 'region', 'number'])
csvdates = csvfile.date.values  # need to only get unique
csvregions = csvfile.region.values

outputrowobjects = []

# pre-populate the output row objects with dates and region pairs
for date in csvdates:
    newrowobj = type("", (object,), {"date": date, "regionPairs": []})
    for region in csvregions:
        regionpair = type("", (object,), {"region": region, "number": "-"})
        newrowobj.regionPairs.append(regionpair)
    outputrowobjects.append(newrowobj)
