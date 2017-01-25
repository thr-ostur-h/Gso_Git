#Þröstur Haraldsson
#25.1.2017

skra=input("Sláðu inn nafn á skrá")
nafnskra=skra + ".txt"
skrainmin=open(nafnskra,"w+")

skrainmin.write("Fyrsta linan i skranni")
skrainmin.close()