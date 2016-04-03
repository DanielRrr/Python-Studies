from pylab import *

x = linspace(0,5,10)

y = x ** 2

print(x)
[ 0.          0.55555556  1.11111111  1.66666667  2.22222222  2.77777778
  3.33333333  3.88888889  4.44444444  5.        ]

print(y)
[  0.           0.30864198   1.2345679    2.77777778   4.9382716
   7.71604938  11.11111111  15.12345679  19.75308642  25.        ]

figure()
Out[34]: <matplotlib.figure.Figure at 0x1fbb5d534a8>

plot(x, y, 'r')
Out[35]: [<matplotlib.lines.Line2D at 0x1fbb7766a58>]

xlaber('x')
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-36-52e5bac56555> in <module>()
----> 1 xlaber('x')

NameError: name 'xlaber' is not defined

xlabel('x')
Out[37]: <matplotlib.text.Text at 0x1fbb798ac18>


xlabel('y')
Out[39]: <matplotlib.text.Text at 0x1fbb798ac18>

title('title')
Out[40]: <matplotlib.text.Text at 0x1fbb773acc0>

show()

fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(x,y,'r')
Out[44]: [<matplotlib.lines.Line2D at 0x1fbb7571438>]

axes.set_xlabel('x')
Out[45]: <matplotlib.text.Text at 0x1fbb7924588>

axes.set_ylabel('y')
Out[46]: <matplotlib.text.Text at 0x1fbb792fba8>

axes.set_title('title')
Out[47]: <matplotlib.text.Text at 0x1fbb778ccf8>


show()

fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x, y, 'r')
Out[53]: [<matplotlib.lines.Line2D at 0x1fbb788db00>]

axes1.set_xlabel('x')
Out[54]: <matplotlib.text.Text at 0x1fbb792cc88>

axes1.set_ylabel('y')
Out[56]: <matplotlib.text.Text at 0x1fbb606c128>

axes1.set_title('title')
Out[57]: <matplotlib.text.Text at 0x1fbb75ad3c8>

axes2.plot(y, x, 'g')
Out[58]: [<matplotlib.lines.Line2D at 0x1fbb79dfcc0>]

axes2.set_xlabel('y')
Out[59]: <matplotlib.text.Text at 0x1fbb7894f28>

axes2.set_ylabel('x')
Out[60]: <matplotlib.text.Text at 0x1fbb789fa90>

axes2.set_title('insert')
Out[61]: <matplotlib.text.Text at 0x1fbb789b6d8>

show()
