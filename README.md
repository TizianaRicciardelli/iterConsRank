# iterConsRank 💻

## Authors

- [@TizianaRicciardelli](https://www.github.com/TizianaRicciardelli)
- [@DidierBarradasBautista](https://www.github.com/D-Barradas)

## Files description
control-gen-MAT0.sh it is a bash script to generate automatically CONTROL files. it hase to be in the same folder of the models.

iter.sh is the main file, containing the pipeline to have a correct execution of the iteration,
  avoid file overwriting, keep track of the cutoff percentage and of the umber of steps.
  
cut is a text file containing a float number from 0 to 1. It is corresponding to the percenage
  of models to keep to next iteration at each step.

cut.f it is fortran code to output interactively the n. of models at the current step and how many models are kept for next iteration step.

CONSRANK is the standalone version of CONSRANK algorithm.

a.out is a fortran code to modify CONTROL file based on the new number of models and new list of them (see control-gen-MAT0.sh)
