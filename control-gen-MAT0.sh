#!bin/bash
#script to create CONTROL FILE to run ConsRank - always check the GenMat field: 0-for non generate matrix, 1-  to generate it

rm CONTROL
echo "PairwiseChain1          1       ! # of chains in pairK
A # substitute with your chain/s
C
PairwiseChain2          1       ! # of chains in pairL
B # substitute with your chain/s
CUTOffDistance           5.0    ! # cutoff distance in Angstrom
GenMat			0
NumberOfPDBFiles       XXXX  ! # number of pdb files the code going to deal with" > CONTROL
n=$(ls *model-*.pdb|wc -l)
sed -i "s/XXXX/$n/g" CONTROL
ls *model-*.pdb >> CONTROL
