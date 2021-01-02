import pandas

infilename = "C:\\Git\\source\\repos\\Tom\\CovidDataTransformerPy\\data\\covid_data.csv"
outfilename = "C:\\Git\\source\\repos\\Tom\\CovidDataTransformerPy\\data\\output.csv"

csvfile = pandas.read_csv(infilename, delimiter=',', header='infer')
print(csvfile.header)

# with open("data\covid_data.csv") as csvfile:
#     reader = csv.DictReader(csvfile)

#     dates = reader['date']

#     print(dates)
