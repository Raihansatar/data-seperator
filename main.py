file = open('dataset.tsv', encoding="utf8")

lines = file.readlines()
for line in lines:
    newLine = line.split("\t")
    newFile = open("dataset-"+line[0]+".txt", "a+", encoding="utf8");
    newFile.write(newLine[0] + ',' + newLine[1]);
    
print('finish')
file.close
newFile.close