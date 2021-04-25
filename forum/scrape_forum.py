import requests
from bs4 import BeautifulSoup

forum_url='https://www.twokinds.net/forum/'
discussion_url=forum_url+"viewforum.php?f=1&start={}"

import random
import time

import csv
import pprint
import argparse 
from datetime import datetime 

def get_threads(start=1):
  jitter = random.uniform(1,2)
  time.sleep(jitter)

  query_url=discussion_url.format(start)
  r = requests.get(query_url)
  return r.text

def parse_topic(topic,author):
  topic_txt = topic.text.strip()
  author_txt  = author.text.strip()
  
  if not topic_txt.startswith("Comic for"):
    return {}
  
  sanitized_str = topic_txt.replace('Comic for ', '')
  sanitized_str = sanitized_str.replace(';',':')
  sanitized_str = sanitized_str.replace('th','',1)

  if ':' in sanitized_str:
    title = sanitized_str.split(':')[1]
  else:
    title = sanitized_str

  try:
    #date_str, title = sanitized_str.split(':')
    date_str = author_txt.split('»')[1].strip()
    data_dic = { 'date': date_str.strip(), 'title': title.strip()}
  except ValueError as e:
    print("Failed to parsed date: {}".format(sanitized_str))
    print(str(e))
    data_dic = {'title': sanitized_str,'date':''}
 
  return data_dic 

def parse_opts():
  default_filename = "forumQuery-" + datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + '.csv'
  parser = argparse.ArgumentParser('Forum scraper')
  parser.add_argument('topics',type=int)
  parser.add_argument('--outfile',default=default_filename)
  return parser.parse_args()

def parse_page(page):
  parsed_threads = []
  try:
    sopa = BeautifulSoup(page,'html.parser')
    forum_title = sopa.find(class_='forum-title')
    forum_title = sopa.find('h2')
    #print(forum_title.text)
    topics_list = sopa.find_all(class_='topiclist topics')[1]
    topics = topics_list.find_all(class_='row-item')
    n_topics = len(topics)
    print("Detected {} threads".format(n_topics))
    for top in topics:
      topic_title = top.find(class_='topictitle')
      author = top.find(class_='topic-poster')
      replies = top.find(class_='posts')
      views = top.find(class_='views')
      parsed = parse_topic(topic_title,author)
      if parsed:
        parsed['views'] = int(views.text.replace('Views',''))
        parsed['replies'] = int(replies.text.replace('Replies',''))
        parsed_threads.append(parsed)

  except Exception as e:
    print(str(e))  
  
  print("Parsed {} topics".format(len(parsed_threads))) 
  return parsed_threads, n_topics

def persist(collection,filename):
  fields = ['title','date','views','replies']
  with open(filename,'w') as csv_file:
    writer=csv.DictWriter(csv_file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(collection)

  return

if __name__=='__main__':
  args = parse_opts()
  read_threads = 0
  collection = [] 
  while read_threads < args.topics:
    print("Reading from thread: {}".format(read_threads+1))
    pag = get_threads(read_threads+1)   
    data,hits = parse_page(pag)
    read_threads += hits
    collection.extend(data)
  #pprint.pprint(collection)
  #alt_parse(pag)
  persist(collection,args.outfile)
