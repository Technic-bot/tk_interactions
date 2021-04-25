import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import argparse 

# Me mame?
import numpy as np
from scipy.signal import argrelextrema
plt.style.use('seaborn-darkgrid')
plt.style.use('ggplot')

def parse_opt():
  parser = argparse.ArgumentParser("Forum style grapher")
  parser.add_argument('file',type=str,help='Filename to read')
  parser.add_argument('--category',type=str,help='Metric to plot')
  parser.add_argument('--sigma',type=float,help='Number of sigmas for event detection')
  parser.add_argument('--separator',help='file separator')
  parser.add_argument('--time',help='time units in date field',default=None)
  parser.add_argument('--out',help='Output filename',default=None)
  parser.add_argument('--title', help='Title columna name', default='title')
  return parser.parse_args()

def parse_dataframe(filename,prune_thr=5,prune_cat='replies',splt=',',timestamped=None):
  if splt == 'tab':
    separator = '\t'
  else:
    separator = ','
  df = pd.read_csv(filename,sep=separator)
  df['date'] = pd.to_datetime(df['date'],infer_datetime_format=True,unit=timestamped)
  df.sort_values('date',inplace=True)
  df = df.loc[df[prune_cat]>5]
  #print(df.head())
  
  return df

def get_descriptors(df,category='replies'):
  min_date = df['date'].min()
  max_date = df['date'].max()

  average_val =  df[category].mean()
  std_val = df[category].std()
  
  max_val = df[category].max()
  min_val = df[category].min()
  top_date = df[df[category]==max_date]['date']
  
  print("For {} Mean: {} Std dev {}".format(category,average_val,std_val))
  
  descriptor_dic = { 'mean': average_val,
                      'stddev': std_val,
                      'min_date': min_date,
                      'max_date': max_date,
                      'min_val': min_val,
                      'max_val': max_val,
                      'top_date' : top_date}
    
  return descriptor_dic 

def get_events(df, threshold, category='replies',title_col='title'):
  event_df = df.loc[df[category]>=threshold]
  print("Found, {} events in the {} category".format(len(event_df),category))
  print(event_df[['date',title_col,category]].sort_values(category,ascending=False).to_string())
  return event_df
  
def get_extrema(df,category='replies',order=3):
  maxes = argrelextrema(df[category].values, np.greater_equal,order=order)
  ex_df = df.iloc[maxes]
  return ex_df
  
def graph_hits(df,category='replies',std_mul=1,title_name='title'):
  desc = get_descriptors(df,category)
 
  avr = desc['mean']
  stdd = desc['stddev']
  min_d = desc['min_date']
  max_d = desc['max_date']
  ex_df = get_extrema(df,category,3)
  e_df = get_events(ex_df,avr+std_mul*desc['stddev'],category,title_name) 
  fig, ax = plt.subplots(figsize=(10,5))
  # Debug plot
  #ax.hlines(avr+std_mul*desc['stddev'],min_d,max_d,color='r',ls='-')
  ax.hlines([avr+stdd,avr-stdd],min_d,max_d,color='#F7941D',ls='--',
            label='One sigma')
  ax.hlines(avr,min_d,max_d,color='#F7941D',ls='-',
            label='Mean')
  ax.plot(df['date'],df[category],color='#72CDEE',label=category)
  ax.scatter(e_df['date'],e_df[category],color='#F7942D',marker='^'
            ,label='Local Maxima')
  
  #for idx,row in e_df.iterrows():
  #  ax.text(row['date'],row[category],row['title'])
 
  ax.set_title('Date vs '+category)
  ax.set_xlabel('Date')
  ax.set_ylabel(category.title())
  ax.legend()
  
  # Major ticks every 6 months.
  fmt_half_year = mdates.YearLocator()
  ax.xaxis.set_major_locator(fmt_half_year)

  # Minor ticks every month.
  fmt_month = mdates.MonthLocator()
  ax.xaxis.set_minor_locator(fmt_month)

  ax.xaxis.set_major_formatter( mdates.DateFormatter('%Y-%m-%d'))
  ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
  fig.autofmt_xdate() 
  return fig

if __name__=="__main__":
  args = parse_opt()
  pd = parse_dataframe(args.file,prune_cat=args.category,
                      splt=args.separator,timestamped=args.time)
  fig = graph_hits(pd,args.category,args.sigma,args.title)
  if not args.out:
    plt.show()
  else:
    #plt.show()
    fig.savefig(args.out)
