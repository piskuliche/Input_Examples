#MSUB -N argon_test
#MSUB -q thompson
#MSUB -j oe
#MSUB -M piskuliche@ku.edu
#MSUB -m ae
#MSUB -d ./
#MSUB -l nodes=1:ppn=20:intel,mem=50gb,walltime=50:00:00

module load legacy
module load intel_compiler_2016
module load intel_mpi_intel64/5.1.2.150
module load lammps/20161117

echo Time is `date`
echo Directory is `pwd`

mpirun lmp_g++ < in.nvt -screen none

echo Ending Time is `date`
exit 0
