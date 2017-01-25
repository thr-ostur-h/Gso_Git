#Þröstur Haraldsson
#25.1.2017

skra=input("Sláðu inn nafn á skrá")
nafnskra=skra + ".txt"
skrainmin=open(nafnskra,'w+')

skrainmin.write("Fyrsta linan i skranni"'\n')
skrainmin.close()

skrainmin = open(nafnskra,'a')
lina1 = input("Skráðu inn línu eitt")
lina2 = input("Skráðu inn línu tvö")
lina3 = input("Skráðu inn lína þrjú")
skrainmin=open(nafnskra,'a')
skrainmin.write(lina1+'\n')
skrainmin.write(lina2+'\n')
skrainmin.write(lina3+'\n')
skrainmin.close()
skrainmin =open(nafnskra,'r')
print(skrainmin.read())