# written by Mobolaji Williams,
# AC209-Final Proj

# creates scatter matrix plot

# We note that we manually created these plots because
# it doesn't seem that pandas offers a function to label points
# while taking into account the relative distances to other points:

fig = plt.figure()

X=list(mgf['Competition'])
Y=list(mgf['Gamer Interest'])
Z=list(mgf['Public Opinion'])

f, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3, 3)


ax1.plot(X, Z, 'k.')
ax1.set_xlim([-5,200])
ax1.set_ylim([0,5])
ax1.set_ylabel('Public Opinion',color ='r')
ax1.plot( range(-5,201),  [mean_po]*206, 'r-')
ax1.plot([mean_comp]*6, range(0,6), 'b-')
ax1.grid()

ax1.annotate('T', 
    xy = ( mgf['Competition'][mgf['Genre'] == 'Tennis'],mgf['Public Opinion'][mgf['Genre'] == 'Tennis']), 
    arrowprops = dict(arrowstyle = '->',  facecolor = 'black' , connectionstyle = 'arc3,rad=0'), 
    xytext = (10, -55), textcoords = 'offset points', ha = 'right', va = 'bottom',
    bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5))

ax1.annotate('B', 
    xy = ( mgf['Competition'][mgf['Genre'] == 'Bowling'],mgf['Public Opinion'][mgf['Genre'] == 'Bowling']), 
    arrowprops = dict(arrowstyle = '->',  facecolor = 'black' , connectionstyle = 'arc3,rad=0'), 
    xytext = (55, -15), textcoords = 'offset points', ha = 'right', va = 'bottom',
    bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5))


ax2.plot(Y, Z, 'k.')
ax2.set_xlim([0,12])
ax2.set_ylim([0,5])
ax2.plot(range(0,13), [mean_po]*13, 'r-')
ax2.plot([mean_gi]*6, range(0,6) , 'g-')
ax2.grid()

ax2.annotate('T', 
    xy = (mgf['Gamer Interest'][mgf['Genre'] == 'Tennis'],  mgf['Public Opinion'][mgf['Genre'] == 'Tennis']),
    arrowprops = dict(arrowstyle = '->',  facecolor = 'black' , connectionstyle = 'arc3,rad=0'), 
    xytext = (30, -30), textcoords = 'offset points', ha = 'right', va = 'bottom',
    bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5))

ax2.annotate('B', 
    xy = (mgf['Gamer Interest'][mgf['Genre'] == 'Bowling'],  mgf['Public Opinion'][mgf['Genre'] == 'Bowling']),
    arrowprops = dict(arrowstyle = '->',  facecolor = 'black' , connectionstyle = 'arc3,rad=0'), 
    xytext = (30, -30), textcoords = 'offset points', ha = 'right', va = 'bottom',
    bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5))



ax3.plot(Z, Z, 'k.')
ax3.set_xlim([0,5])
ax3.set_ylim([0,5])
ax3.plot( range(0,6),  [mean_po]*6, 'r-')
ax3.plot( [mean_po]*6, range(0,6), 'r-')
ax3.grid()




ax4.plot(X, Y, 'k.')
ax4.set_xlim([-5,200])
ax4.set_ylim([0,12])
ax4.set_ylabel('Gamer Interest',color ='g')
ax4.plot([mean_comp]*13, range(0,13), 'b-')
ax4.plot(range(0,201), [mean_gi]*201, 'g-')
ax4.grid()



ax4.annotate('T', 
    xy = (mgf['Competition'][mgf['Genre'] == 'Tennis'],  mgf['Gamer Interest'][mgf['Genre'] == 'Tennis']),
    arrowprops = dict(arrowstyle = '->',  facecolor = 'black' , connectionstyle = 'arc3,rad=0'), 
    xytext = (40, 30), textcoords = 'offset points', ha = 'right', va = 'bottom',
    bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5))

ax4.annotate('B', 
    xy = (mgf['Competition'][mgf['Genre'] == 'Bowling'],  mgf['Gamer Interest'][mgf['Genre'] == 'Bowling']),
    arrowprops = dict(arrowstyle = '->',  facecolor = 'black' , connectionstyle = 'arc3,rad=0'), 
    xytext = (55, 20), textcoords = 'offset points', ha = 'right', va = 'bottom',
    bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5))



ax5.plot(Y, Y, 'k.')
ax5.set_ylim([0,12])
ax5.set_xlim([0,12])
ax5.plot([mean_gi]*13, range(0,13) , 'g-')
ax5.plot(range(0,13), [mean_gi]*13, 'g-')
ax5.grid()



ax6.plot(Z, Y, 'k.')
ax6.set_xlim([0,5])
ax6.set_ylim([0,12])
ax6.plot(range(0,6), [mean_gi]*6, 'g-')
ax6.plot( [mean_po]*13, range(0,13), 'r-')
ax6.grid()



ax7.plot(X, X, 'k.')
ax7.set_ylim([0,200])
ax7.set_xlim([0,200])
ax7.set_xlabel('Competition',color ='b')
ax7.set_ylabel('Competition',color ='b')
ax7.plot([mean_comp]*201, range(0,201), 'b-')
ax7.plot(range(0,201), [mean_comp]*201, 'b-')
ax7.grid()



ax8.plot(Y, X, 'k.')
ax8.set_xlim([0,12])
ax8.set_ylim([-5,200])
ax8.set_xlabel('Gamer Interest',color ='g')
ax8.plot([mean_gi]*206, range(-5,201) , 'g-')
ax8.plot(range(0,13), [mean_comp]*13, 'b-')
ax8.grid()



ax9.plot(Z,X, 'k.')
ax9.set_xlim([0,5])
ax9.set_ylim([-5,200])
ax9.set_xlabel('Public Opinion',color ='r')
ax9.plot(range(0,6), [mean_comp]*6, 'b-')
ax9.plot( [mean_po]*206, range(-5,201), 'r-')
ax9.grid()


plt.suptitle('Public Opinion, Gamer Interest, and Competition Distributions for Giant Bomb Genres',fontsize = 20)


f.set_size_inches(14.5,10.5)
f.subplots_adjust(hspace=.25)
