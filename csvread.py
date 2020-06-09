import csv

#with open('names.csv','r') as rr:
#    csvreader=csv.reader(rr)

#    with open('new_name.csv','w') as wr:
#        csv_writer=csv.writer(wr,delimiter='-')
    #next(csvreader) it didnt print 1st line..

#        for line in csvreader:
#            csv_writer.writerow(line)
        #orint(line[2]) it only print email

with open('names.csv','r') as rr:
    csvreader=csv.DictReader(rr)# it prints in dictionary key and value pair

    for line in csvreader:
        print(line)


#del line['email'] it will create a mail column.
