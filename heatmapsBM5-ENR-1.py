import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
pal = sns.color_palette(palette='coolwarm', n_colors=14)
#pal = sns.color_palette(palette='colorblind', n_colors=14)
my_file = pd.ExcelFile('/Users/ricciart/Desktop/Kaust/iterConsRank/BM5/cutoffs/0.85_NL%.xlsx')
# %%
# print ( my_file.sheet_names ) 
# %%
targets=sys.argv[1]
my_names= open(targets).read().splitlines()
my_names_dict={}
z=0
#c= open(targets, "r")
#for lines in c.readline():
#	z=+1
#	my_names.append(str(lines))
#	my_names_dict[z]= b
#print(my_names)
for b in my_names:
	z=z+1
	my_names_dict[z]=b	
#my_names = ['T29', 'T30', 'T32', 'T35', 'T37', 'T39', 'T40CA', 'T40CB', 'T41', 'T46', 'T47', 'T50', 'T53', 'T54']
#my_names_dict = {1:'T29', 2:'T30', 3:'T32', 4:'T35', 5:'T37', 6:'T39', 7:'T40CA', 8:'T40CB', 9:'T41', 10:'T46', 11:'T47', 12:'T50', 13:'T53', 14:'T54'}
# %%
print (len(my_names))
#print(my_names_dict)
my_sel= ['Steps', 'NL']
# %%
temp = [] 
for i in my_names:
#    print(i)
    my_sheet = my_file.parse(i)
#    my_sheet = my_file.format(i)
    my_sheet = my_sheet[my_sel] 
    # sns.lineplot(x='iteration step', y='NL%', data=my_sheet)
    max_value = my_sheet['NL'].max()
    my_sheet['Max_val'] = max_value
    my_sheet['Target'] = i
    temp.append(my_sheet)
#    print(my_sheet)
# %%
my_dataframe = pd.concat(temp)
#print(my_dataframe)
#%%
g = sns.FacetGrid(my_dataframe,row='Target', hue='Max_val', aspect=15, height=0.75, palette=pal)
# then we add the densities kdeplots for each month
g.map(sns.lineplot, 'Steps','NL', data=my_dataframe, lw=1.5 , alpha=0.8,clip_on=False)
# g.map(sns.kdeplot, 'iteration step','NL on 10', data=my_dataframe, #lw=1.5 , alpha=0.8,clip_on=False)
#       bw_adjust=1, 
#       clip_on=False,
#       fill=True, 
#       alpha=1, linewidth=1.5)
# here we add a white line that represents the contour of each kdeplot
# g.map(sns.lineplot,  'Steps','NL%', data=my_dataframe, color='w', lw=1.5, alpha=0.1 , clip_on=False)
    #   bw_adjust=1, 
    #   clip_on=False, 
    #   color="w", 
    #   lw=2)
# here we add a horizontal line for each plot
g.map(plt.axhline, y=0, lw=2, clip_on=False)
# we loop over the FacetGrid figure axes (g.axes.flat) and add the month as text with the right color
# notice how ax.lines[-1].get_color() enables you to access the last line's color in each matplotlib.Axes
for i, ax in enumerate(g.axes.flat):
    # ax.text(-15, 0.02, my_names_dict[i+1],
    ax.text(-5.0, 0.02, my_names_dict[i+1],
            fontweight='bold', fontsize=15,
            color=ax.lines[-1].get_color())
    
# we use matplotlib.Figure.subplots_adjust() function to get the subplots to overlap
# g.fig.subplots_adjust(hspace=-0.1)
# eventually we remove axes titles, yticks and spines
g.set_titles("")
# g.set(yticks=[])
g.despine(bottom=True, left=False)
plt.setp(ax.get_xticklabels(), fontsize=15, fontweight='bold')
# plt.xlabel('Iteration setp', fontweight='bold', fontsize=15)
# g.fig.suptitle('Daily average temperature in Seattle per month',
#                ha='right',
#                fontsize=20,
#                fontweight=20)
plt.show()

my_df_pivot = my_dataframe.pivot_table(index='Steps', columns='Target', values='NL')
cmap_reds = plt.get_cmap('Reds')
num_colors = 120
colors = ['grey'] + [cmap_reds(i / num_colors) for i in range(1, num_colors)]
cmap = LinearSegmentedColormap.from_list('', colors, num_colors)
ax = sns.heatmap(my_df_pivot, cmap=cmap, vmin=0, vmax=num_colors, square=True, cbar=False)
cbar = plt.colorbar(ax.collections[0], ticks=range(num_colors + 1))
#sns.heatmap(data=my_df_pivot, annot=False, cmap='viridis',linewidths=.5)
my_index_rev = my_df_pivot.index.tolist()
my_index_rev =  my_index_rev[::-1]
my_df_pivot.reindex(my_index_rev)
plt.figure(figsize=(15,15))
my_df_pivot = my_df_pivot.reindex(my_index_rev)
my_list = my_names[::-1]
my_df_pivot = my_df_pivot[my_names]
sns.heatmap(data=my_df_pivot.reindex(my_index_rev), annot=False, cmap=cmap, linewidths=.5)
plt.title('BM5 3K - Enrichment', fontsize = 20) # title with fontsize 20
plt.xlabel('Targets', fontsize = 15) # x-axis label with fontsize 15
plt.ylabel('Steps', fontsize = 15) # y-axis label with fontsize 15
plt.show()
