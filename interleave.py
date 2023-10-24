#!/usr/bin/env python3
#Program name = interleave.py
#Imported SeqIO from Biopython module to read/parse the fastq file of the Left & Right reads of Illumina sequencing.
from Bio import SeqIO
#Imported SeqRecord to be able to write the record objects into a file. 
from Bio import SeqRecord

#Specified the file paths where the Left & Right reads of the sequencing exist, named them LR, RR.
#LR-Left Reads
#RR-Right Reads
#Used SeqIO.parse function to open and parse the files. 
LR = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq", "fastq")
RR = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R2.fastq", "fastq")

#Initiating an empty list which can in future contain the data from the record object.
#assigning it to a variable named temp
temp = []

#Initiating a for loop to loop over each element in the Left and Right Reads.
#Zipping both the left and right reads to get an interleaved sequence. 
for left, right in zip(LR, RR):
	#Appending the elements(description, sequence) in the left reads to the empty list that was created. 
	temp.append(left)
	#Appending the elements(description, sequence) in the right reads to the empty list that was created. 
	temp.append(right) 
#Using the SeqIO.write function to write the data of the record object into a fasta file. 
#Specifying the file name of the output file, "interleaved.fasta", also specifying the format "fasta".
#The output would have one left read of R1 followed by the right read of R2 and that pattern continues. 
SeqIO.write(temp, "interleaved.fasta", "fasta")
