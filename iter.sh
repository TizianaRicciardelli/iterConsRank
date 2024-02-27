#!/bin/bash

gfortran cut.f

#to generate the CONTROL input file needed to run CONSRANK
sh control-gen-MAT1.sh

read line < cut #file containing a float number between 0-1, corresponding to the % models to keep to next iteration
i=1 #flag for starting the iteration
while [ $i -le 30 ] #change 30 with the number of steps of your preference
do
	echo $i"th step"
	CONSRANK -c CONTROL
        #to avoid overwriting of output files during the iteration
        #we change output files name, adding cutoff iteration step index to them  
	str1="Zscore-"$line"-"$i".txt"
	cp Zscore.txt $str1 #it copies the Zscore.txt output to Zscore-cutoff-ithstep.txt
	str1="CONTROL-"$line"-"$i".txt"
	cp CONTROL $str1 #it do the same with the CONTROL file, to keep track of the models ids involved in each iteration
	str1="consensus_tableALL-"$line"-"$i".txt"
	mv consensus_tableALL.txt $str1 #same for consensus tables
	str1="conservation_score-"$line"-"$i".txt"
	mv conservation_score.txt $str1 #same for conservation score
        #to start the new iteration, we create a new CONTROL file, to input to CONSRANK
	sort -k 2 Zscore.txt > temp
	mv temp Zscore.txt
        head -6 CONTROL > temp0
	./a.out #this is a fortran script that from the CONTROL file list of models takes out only the % models we set (cutoff)   
	cat temp >> temp0
	mv temp0 CONTROL
	let "i=i+1"
done

