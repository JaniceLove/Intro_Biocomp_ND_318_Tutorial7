#Generate a histogram of sequence lengths and GC content using the Lecture11.fasta file
#import packages
import pandas
import numpy
from plotnine import *

#open data
Infile=open("Lecture11.fasta","r")
all_lines=Infile.readlines()

#create lists for storing information
seqlength=[]
percentGC=[]
seqID=[]
Gcount=0
Ccount=0
Slength=0

#need to count the number of characters (sequence length)
#need to count the number of Gs and Cs and divide by length (G,C/# of characters)x 100%
#loop through each line of the file, assigning the seqID and seqlength to the lists
#loop through and count the number of Gs and Cs

for line in all_lines:
	line=line.strip()
	if '>' in line:
		seqID.append(line[1:])
	else:
		Slength=float(len(line))
		Gcount=line.count("G")
		Ccount=line.count("C")
		seqlength.append(Slength)
		percentGC.append(float(Gcount+Ccount)/Slength*100)

# make lists into a dataframe that you can use to plot the histogram
data=pandas.DataFrame(list(zip(seqID,percentGC,seqlength)),columns=['seqID','seqlength','percentGC'])
print (data.shape) #sanity check
print (data.head(5)) #sanity check

import numpy
import pandas
from plotnine import *)

#plot of seqID vs seqlength
a=ggplot(data,aes(x="seqID",y="seqlength"))
a+geom_point()+coord_cartesian()
