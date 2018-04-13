import csv
with open("citydata/uscitiesv1.4.csv","rb") as source:
    rdr= csv.reader( source )
    with open("citydata/result.csv","wb") as result:
        wtr= csv.writer( result )
        #c = 0
        for r in rdr:
            wtr.writerow( (r[0], r[2], r[3], r[6], r[7]) )
            #c = c+ 1
            # if c > 10:
            # 	break