"""Nation GDP Growth Averaged by Decade 1880-2010"""
import pandas as pd
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
    #print('avg_growth for',df['country'][mark],'is',avg_perc_growth)
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
title='Average Percentage GDP Growth per Decade 1880-2010 of Nations with Current Population > 5,000,000')
ax.set_xlabel("Sovereign Nation",size=40)
ax.set_ylabel("Percentage Growth",size=30)

blue_patch = mpatches.Patch(color='blue', label='Africa',alpha=.5)
red_patch = mpatches.Patch(color='red', label='Europe',alpha=.5)
green_patch = mpatches.Patch(color='green', label='Asia',alpha=.5)
yellow_patch = mpatches.Patch(color='yellow', label='Americas',alpha=.5)
m_patch = mpatches.Patch(color='m', label='Oceania',alpha=.5)
plt.legend(handles=[blue_patch,red_patch,green_patch,yellow_patch,m_patch],fontsize='x-large')
plt.show()