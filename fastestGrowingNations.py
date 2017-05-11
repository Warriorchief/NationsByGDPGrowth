"""Nation GDP Growth Averaged by Decade 1880-2010"""
import pandas as pd
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

df=pd.read_csv('NationsHistSocEconStatus.csv',index_col='wbid')
del df['SES'],df['popshare'],df['yrseduc'],df['unid']

df=df.sort_values(by=['country','year'])
regions_df=pd.read_csv('NationsPopsRegion.txt',thousands=',')
df=pd.merge(regions_df,df,on='country')
df['avg_growth']=''

mark=0
while mark<1904:
    growths=[df['gdppc'][n+1]/df['gdppc'][n] for n in range(mark,mark+13)]
    avg_growth=sum(growths)/13
    avg_perc_growth=round(float((float(avg_growth)-1)*100),2)
    df['avg_growth'][mark]=avg_perc_growth
    mark+=14

df=df[['country','region','avg_growth','population']]
df=df[df['avg_growth']!='']
df=df[df['population']>5000000]
df=df.set_index(['country'])
df=df.sort_values(['region'])
del df['population']

colors={'Africa':'b','Europe':'r','Asia':'g','Americas':'y','Oceania':'m'}
colorList=list(df['region'].map(colors))
ax=df.plot(kind='bar',figsize=(18,9),y='avg_growth',color=colorList,alpha=.5,
title='Average Percentage GDP Growth/Decade 1880-2010, by Region, of Nations with Current Population > 5,000,000')
ax.set_xlabel("Sovereign Nation",size=40)
ax.set_ylabel("Percentage Growth",size=30)
blue_patch = mpatches.Patch(color='blue', label='Africa',alpha=.5)
yellow_patch = mpatches.Patch(color='yellow', label='Americas',alpha=.5)
green_patch = mpatches.Patch(color='green', label='Asia',alpha=.5)
red_patch = mpatches.Patch(color='red', label='Europe',alpha=.5)
m_patch = mpatches.Patch(color='m', label='Oceania',alpha=.5)
AfricaSTD=round(np.std(df['avg_growth'][0:28]),1)
AmericasSTD=round(np.std(df['avg_growth'][28:47]),1)
AsiaSTD=round(np.std(df['avg_growth'][47:76]),1)
EuropeSTD=round(np.std(df['avg_growth'][76:99]),1)
AfricaSTD_patch=mpatches.Patch(color='blue',label='Africa StdDev: '+str(AfricaSTD),alpha=.5)
AmericasSTD_patch=mpatches.Patch(color='yellow',label='Americas StdDev: '+str(AmericasSTD),alpha=.5)
AsiaSTD_patch=mpatches.Patch(color='green',label='Asia StdDev: '+str(AsiaSTD),alpha=.5)
EuropeSTD_patch=mpatches.Patch(color='red',label='Europe StdDev: '+str(EuropeSTD),alpha=.5)
first_legend=plt.legend(handles=[blue_patch,red_patch,green_patch,yellow_patch,m_patch],fontsize='x-large',loc=1)
ax = plt.gca().add_artist(first_legend) #more than one legend on same chart
plt.legend(handles=[AfricaSTD_patch,AmericasSTD_patch,AsiaSTD_patch,EuropeSTD_patch],loc=2)
plt.show()


