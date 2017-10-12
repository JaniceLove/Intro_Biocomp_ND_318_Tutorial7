# Q2 from tutorial 7 assignment
#Authors: Janice Love and Melissa Stephens
#Date: October 11, 2017

import pandas
import numpy
from plotnine import *

#open data
Infile=open("Q2Arcade_CSdegrees,"r")

#set empty lists

#for loop over lists

#Below is just place holder information until we can fill in the acutal information..


# make lists into a dataframe that you can use to plot a scatterplot
data=pandas.DataFrame(list(zip(seqID,percentGC,seqlength)),columns=['seqID','seqlength','percentGC'])
print (data.shape) #sanity check
print (data.head(5)) #sanity check

import numpy
import pandas
from plotnine import *

#plot of seqID vs seqlength
a=ggplot(data)+theme_classic()+xlab("seqID")+ylab("seqlength")
a+geom_bar(aes(x="seqID",y="seqlength"),stat="summary")

a=ggplot(data)+theme_classic()+xlab("seqID")+ylab("percentGC")
a+geom_bar(aes(x="seqID",y="percentGC"),stat="summary")
