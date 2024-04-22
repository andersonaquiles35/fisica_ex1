#0.9649145524319053
import matplotlib.pyplot as plt
import numpy as np

data="""1,301 0,326 0,248 -2,186
1,317 0,329 0,120 -1,469
1,334 0,330 0,164 2,186
1,351 0,335 0,240 2,203
1,367 0,338 0,217 -0,612
1,384 0,342 0,221 1,157
1,401 0,346 0,248 2,325
1,417 0,350 0,315 4,629
1,434 0,356 0,405 1,800
1,451 0,364 0,390 -0,257
1,467 0,369 0,367 0,386
1,484 0,376 0,420 1,800
1,501 0,383 0,427 0,900
1,517 0,390 0,443 4,500
1,534 0,398 0,570 3,857
1,551 0,409 0,608 -3,471
1,567 0,418 0,435 -4,629
1,584 0,424 0,420 -0,771
1,601 0,432 0,458 2,957
1,617 0,439 0,480 -0,771
1,634 0,448 0,473 -0,129
1,651 0,455 0,435 -2,571
1,668 0,463 0,420 -1,543
1,684 0,469 0,360 1,543
1,701 0,475 0,465 5,143
1,718 0,484 0,563 -0,386
1,734 0,494 0,450 -5,657
1,751 0,499 0,345 -4,094E-16
1,768 0,505 0,450 6,171
1,784 0,514 0,577 2,443
1,801 0,524 0,533 -1,157
1,818 0,532 0,510 -0,771
1,834 0,541 0,532 1,671
1,851 0,550 0,548 1,157
1,868 0,560 0,585 -1,029
1,884 0,569 0,517 -2,186
1,901 0,577 0,488 0,643
1,918 0,586 0,555 2,057
1,934 0,595 0,562 1,671
1,951 0,604 0,592 3,214
1,968 0,615 0,683 3,214
1,984 0,627 0,705 3,343
2,001 0,639 0,773 4,243
2,018 0,653 0,870 3,600
2,034 0,668 0,885 0,514
2,051 0,682 0,885 -0,257
2,068 0,697 0,877 4,243
2,084 0,712 1,005 5,400
2,101 0,731 1,102 4,500
2,118 0,748 1,117 2,186
2,134 0,768 1,193 2,443
2,151 0,788 1,200 0,771
2,168 0,808 1,207 -4,243
2,184 0,828 1,088 -5,271
2,201 0,844 0,982 -6,043
2,218 0,861 0,930 -1,286
2,234 0,875 0,900 -0,771
2,251 0,891 0,938 2,186
2,268 0,906 0,953 -3,471
2,284 0,923 0,855 -2,829
2,301 0,935 0,802 -0,643
2,318 0,950 0,878 3,214
2,335 0,964 0,892 1,414
2,351 0,979 0,930 1,286
2,368 0,995 0,937 -0,129
2,385 1,011 0,923 -0,643
2,401 1,026 0,915 -1,286
2,418 1,041 0,885 0,257
2,435 1,055 0,907 2,700
2,451 1,071 0,990 3,600
2,468 1,088 1,027 1,157
2,485 1,106 1,028 2,186
2,501 1,123 1,088 4,243
2,518 1,142 1,185 7,457
2,535 1,162 1,320 4,629
2,551 1,186 1,373 6,557
2,568 1,208 1,485 9,257
2,585 1,235 1,725 7,714
2,601 1,265 1,747 0,129
2,618 1,294 1,703 0,900
2,635 1,322 1,778 4,243
2,651 1,353 1,860 6,171
2,668 1,384 1,965 5,400
2,685 1,418 2,063 6,043
2,701 1,453 2,145 1,029
2,718 1,490 2,130 -4,886
2,735 1,524 1,958 -3,986
2,751 1,555 1,973 -3,471
2,768 1,590 1,905 -2,571
2,785 1,619 1,815 -3,600
2,801 1,650 1,838 1,157
2,818 1,680 1,823 0,129
2,835 1,711 1,860 5,914
2,851 1,742 1,995 4,114
2,868 1,777 2,047 -0,643
2,885 1,810 1,935 -8,486
2,901 1,842 1,785 0,257
2,918 1,870 1,883 3,471
2,935 1,905 1,995 3,343
2,952 1,936 1,927 -3,471
2,968 1,969 1,912 -0,643
2,985 2,000 1,883 1,157
3,002 2,032 1,958 2,957
3,018 2,065 1,995 1,800
3,035 2,098 2,003 2,443
3,052 2,132 2,077 4,243
3,068 2,167 2,152 0,900
3,085 2,204 2,115 -0,257
3,102 2,238 2,115 -3,600
3,118 2,274 2,040 -7,971
3,135 2,306 1,815 -5,400
3,152 2,335 1,838 3,214
3,168 2,367 1,965 -3,343
3,185 2,400 1,748 -7,843
3,202 2,425 1,620 -5,914
3,218 2,454 1,628 -0,900
3,235 2,480 1,545 0,514
3,252 2,506 1,650 6,429
3,268 2,535 1,778 1,414
3,285 2,565 1,710 -2,571
3,302 2,592 1,650 -2,314
3,318 2,620 1,665 1,286
3,335 2,647 1,672 -3,471
3,352 2,676 1,582 -4,500
3,368 2,700 1,477 -2,700
3,385 2,725 1,515 5,400
3,402 2,750 1,643 6,043
3,418 2,780 1,748 3,471
3,435 2,809 1,740 -8,188E-16
3,452 2,838 1,747 2,700
3,468 2,867 1,823 7,586
3,485 2,898 2,003 11,19
3,502 2,934 2,205 12,86
3,518 2,972 2,422 1,929
3,535 3,014 2,325 0,514
3,552 3,049 2,325 5,400
3,568 3,092 2,595 7,457
3,585 3,136 2,565 3,086
3,602 3,177 2,648 0,643
3,619 3,224 2,662 -1,671
3,635 3,266 2,527 -1,929
3,652 3,308 2,610 2,829
3,669 3,353 2,648 -1,157
3,685 3,397 2,557 0,643
3,702 3,438 2,640 -2,829
3,719 3,485 2,542 0,643
3,735 3,523 2,543 4,500
3,752 3,569 2,790 6,686
3,769 3,616 2,745 -4,114
3,785 3,661 2,640 0,257
3,802 3,704 2,730 3,343
3,819 3,752 2,805 5,914
3,835 3,798 2,872 0,643
3,852 3,848 2,888 5,271
3,869 3,894 2,970 4,629
3,885 3,947 3,120 9,000
3,902 3,998 3,210 3,086
3,919 4,054 3,277 1,157
3,935 4,107 3,210 -7,714
3,952 4,161 3,052 -15,81
3,969 4,209 2,670 -19,03
3,985 4,250 2,385 -9,000
4,002 4,288 2,378 -1,929
4,019 4,329 2,355 -8,486
4,035 4,367 2,093 -7,954
4,052 4,399 1,921 7,220
4,069 4,434 2,257 10,52
4,085 4,478 2,460 1,958
4,102 4,516 2,355 -1,800
4,119 4,556 2,430 3,343
4,135 4,597 2,468 1,671"""

list = data.replace('\n', ' ').replace(',', '.').split(' ')

c=1

t=[]
zz=[]
vv=[]
aa=[]

for i in list:
        if c==1:
                t.append(float(i)-1.267)
                c=c+1
        elif c==2:
                zz.append(float(i)-0.319)
                c=c+1
        elif c==3:
                vv.append(float(i))
                c=c+1
        elif c==4:
                aa.append(float(i))
                c=1

x=np.arange(0,3,0.01)

def v(x):
	return x

plt.plot(np.array([-0.045, 100]), np.array([-0.045,0]), 'black')
plt.plot(np.array([0.009, 0.009]),  np.array([-10,10]), 'black')

plt.plot(x,v(x),color="blue", linewidth=3.5, label='v(t)')
plt.scatter(np.array(t), np.array(vv), color='black', s=4)

plt.xlabel('t (s)')

plt.ylabel('v (m s⁻¹)')
plt.grid(True)
plt.title("Velocidade\nd = 0.9649")

plt.axis([0,3,-0.05,3.5])
plt.legend(loc='lower right')
plt.show()
