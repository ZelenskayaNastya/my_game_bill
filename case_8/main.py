
'''import numpy as np
import matplotlib.pyplot as plt
cy = []
date = []
d = 1
with open('ex1.txt') as f:
    for item in f:
        date.append(d)
        cy.append(float(item))
        d += 1
plt.plot(date, cy)
plt.show()'''


import numpy as np
import matplotlib.pyplot as plt
c1 = []
c2 = []
c3 = []
date = []
d = 1
with open('ex2.txt') as ff:
    for item in ff:
        date.append(d)
        a, b, c = item.split()
        c1.append(float(a))
        c2.append(float(b))
        c3.append(float(c))
        d += 1
plt.plot(date, c1, date, c2, date, c3)
plt.show()


'''import numpy as np
import matplotlib.pyplot as plt
c1 = []
c2 = []
c3 = []
date = []
d = 1
with open('ex2.txt') as ff:
    for item in ff:
        date.append(d)
        a, b, c = item.split()
        c1.append(float(a))
        c2.append(float(b))
        c3.append(float(c))
        d += 1
plt.plot(date, c1, date, c2, date, c3)
plt.show()'''


import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
plt.xlabel(r'$date$')
plt.ylabel(r'$course$')
plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
plt.grid(True)
plt.show()

