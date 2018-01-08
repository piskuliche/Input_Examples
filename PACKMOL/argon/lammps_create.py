import numpy as np

x,y,z = np.genfromtxt("argon_out.xyz", unpack=True, usecols=(1,2,3), skip_header=2)

print "LAMMPS Description"
print " "
print "200 atoms"
print "0 bonds"
print "0 angles"
print "0 dihedrals"
print "0 impropers"
print " "
print "1 atom types"
print " "
print "0. 40. xlo xhi"
print "0. 40. ylo yhi"
print "0. 40. zlo zhi"
print " "
print "Masses"
print " "
print "1 39.948"
print " "
print "Atoms"
print " "
for i in range(0, len(x)):
    step=i+1
    print("%s %s 1 0.0 %s %s %s" % (step, step, x[i], y[i], z[i]))



