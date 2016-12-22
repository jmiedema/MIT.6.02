from pylab import *

figure(1)
plot([1,2,3,4], [1, 7, 3, 5])
figure(2)
plot([1,2,3,4,5,6,7], [1,4,9,16,25,36,49])
savefig("new_figure")