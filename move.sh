ssh zlatkin@linprog.cs.fsu.edu 'rm -rf /home/grads/zlatkin/cap5778'
#scp -r ../Memory_Hierarchy_Simulator  zlatkin@linprog.cs.fsu.edu:/home/grads/zlatkin/cda5105
rsync -a --exclude '../Advanced_Data_Mining//cmake-build-debug' ../Advanced_Data_Mining//  zlatkin@linprog.cs.fsu.edu:/home/grads/zlatkin/cap5778/

#tar cvf assignment_1_ilia_zlatkin.tar mhc.cpp mhc.h makefile PageTable.h PageTable.hpp TLB.h TLB.hpp trace.config
#scp -r assignment_1_ilia_zlatkin.tar zlatkin@linprog.cs.fsu.edu:/home/grads/zlatkin/.
