#Generate a histogram of sequence lengths and GC content using the Lecture11.fasta file
#load data
Infile=open("Lecture11.fasta","r")

#create lists for storing information
seqlength=[]
percentGC=[]
seqID=[]

#need to count the number of characters (sequence length)
#need to count the number of Gs and Cs and divide by length (G,C/# of characters)x 100%
#loop through each line of the file, assigning the seqID and seqlength to the lists
#loop through and count the number of Gs and Cs

