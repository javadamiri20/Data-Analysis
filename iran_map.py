from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.ndimage import label

# create new figure, axes instances.
df = pd.read_csv('iran_dataset.csv')
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
# setup mercator map projection.
m = Basemap(llcrnrlon=40.,llcrnrlat=20.,urcrnrlon=70.,urcrnrlat=45.,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='h',projection='merc',\
            lat_0=40.,lon_0=-20.,lat_ts=20.)
# nylat, nylon are lat/lon of New York
nylat = 40.78; nylon = -73.98
# lonlat, lonlon are lat/lon of London.
lonlat = 51.53; lonlon = 0.08
# draw great circle route between NY and London
m.drawgreatcircle(nylon,nylat,lonlon,lonlat,linewidth=2,color='b')
m.drawcoastlines()
m.fillcontinents()
m.drawcountries()

#tehran
x,y = m(df.iloc[0,1],df.iloc[0,2])
m.scatter(x,y, s= df.iloc[0,3]/10000, c= 'black' ,label= df.iloc[0,0])
plt.legend(markerscale=0.2)

#tabriz
x,y = m(df.iloc[1,1],df.iloc[1,2])
m.scatter(x,y, s= df.iloc[1,3]/10000, c= 'white' ,label= df.iloc[1,0])
plt.legend(markerscale=0.2)

#shiraz
x,y = m(df.iloc[2,1],df.iloc[2,2])
m.scatter(x,y, s= df.iloc[2,3]/10000, c= 'red' ,label= df.iloc[2,0])
plt.legend(markerscale=0.2)

#esfahan
x,y = m(df.iloc[3,1],df.iloc[3,2])
m.scatter(x,y, s= df.iloc[3,3]/10000, c= 'blue' ,label= df.iloc[3,0])
plt.legend(markerscale=0.2)

#yazd
x,y = m(df.iloc[4,1],df.iloc[4,2])
m.scatter(x,y, s= df.iloc[4,3]/10000, c= 'yellow' ,label= df.iloc[4,0])
plt.legend(markerscale=0.2)

#qom
x,y = m(df.iloc[5,1],df.iloc[5,2])
m.scatter(x,y, s= df.iloc[5,3]/10000, c= 'green' ,label= df.iloc[5,0])
plt.legend(markerscale=0.2)

#ilam
x,y = m(df.iloc[6,1],df.iloc[6,2])
m.scatter(x,y, s= df.iloc[6,3]/10000, c= 'purple' ,label= df.iloc[6,0])
plt.legend(markerscale=0.2)

#boushehr
x,y = m(df.iloc[7,1],df.iloc[7,2])
m.scatter(x,y, s= df.iloc[7,3]/10000, c= 'gray' ,label= df.iloc[7,0])
plt.legend(markerscale=0.2)

#khouzestan
x,y = m(df.iloc[8,1],df.iloc[8,2])
m.scatter(x,y, s= df.iloc[8,3]/10000, c= 'pink' ,label= df.iloc[8,0])
plt.legend(markerscale=0.2)

#zanjan
x,y = m(df.iloc[9,1],df.iloc[9,2])
m.scatter(x,y, s= df.iloc[9,3]/10000, c= 'orange' ,label= df.iloc[9,0])
plt.legend(markerscale=0.2)

#semnan
x,y = m(df.iloc[10,1],df.iloc[10,2])
m.scatter(x,y, s= df.iloc[10,3]/10000, c= 'brown' ,label= df.iloc[10,0])
plt.legend(markerscale=0.2)

#fars
x,y = m(df.iloc[11,1],df.iloc[11,2])
m.scatter(x,y, s= df.iloc[11,3]/10000, c= 'violet' ,label= df.iloc[11,0])
plt.legend(markerscale=0.2)

#qazvin
x,y = m(df.iloc[12,1],df.iloc[12,2])
m.scatter(x,y, s= df.iloc[12,3]/10000, c= 'navy' ,label= df.iloc[12,0])
plt.legend(markerscale=0.2)

#kerman
x,y = m(df.iloc[13,1],df.iloc[13,2])
m.scatter(x,y, s= df.iloc[13,3]/10000, c= 'plum' ,label= df.iloc[13,0])
plt.legend(markerscale=0.2)

#gilan
x,y = m(df.iloc[14,1],df.iloc[14,2])
m.scatter(x,y, s= df.iloc[14,3]/10000, c= 'lightgreen' ,label= df.iloc[14,0])
plt.legend(markerscale=0.2)


ax.set_title('Iran cities latitude and longitude')
plt.show()