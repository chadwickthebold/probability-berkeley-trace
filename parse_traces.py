#script to determine 10 most common hashed URLs from
#UC Berkley's Home IP traces project
#This is for a presentation on the probability of
#web cache replacement algorithms for
#ELEC 471, Bucknell University
#Tyler Chadwick

import sys
import re
from subprocess import call
import subprocess

#given a filename of the traces
#from tracelog, print the 10 most
#seen hashed urls and their count

def parse_trace_file(filename) :
  f = open(filename, 'r')
  d = {}
  i = 0
  topURLs = []

  urls = re.findall(r'GET (\d+).', f.read()) 
  for url in urls:
    if url in d:
      d[url] = d[url]+1
    else:
      d[url] = 1
  for w in sorted(d, key=d.get, reverse=True):
    if (i<10):
      topURLs.append(w)
      i = i + 1
      print(w, d[w])

#  num = 0
#  for line in f:
#
#    print(line)
#    print(num)
#    num = num + 1
#    match = re.search('GET (\d+).', line)
#    if match:
#      url = str(match.group(1))
#      if url in d:
#        d[url] = d[url] + 1
#      else:
#        d[url] = 1
#  for w in sorted(d, key=d.get, reverse=True):
#      if (i<10):
#        topURLs.append(w)
#        i = i + 1
#        print(w, d[w])

  f = open(filename, 'r')
  for line in f:
    match = re.search(r'(\d\d\d\d\d\d+:\d\d\d\d+) (\d\d\d\d\d\d+:\d\d\d\d+) (\d\d\d\d\d\d+:\d\d\d\d+) \d*.\d*.\d*.\d*:\d* \d*.\d*.\d*.\d*:\d* \d* \d* \d* \d* \d* \d* \d* \d* GET (\d+).', line)
    if match:
      i = i + 1
      url = str(match.group(4))
      if url in topURLs:
        time = subprocess.check_output(['./tools/timeconvert', match.group(1)])
        time = time.decode("utf-8")
        time = re.search(r'\w+\s+\w+\s+\d+\s+\d+:\d+:\d+\s+\d+',time)
        time = str(time.group())
        s = time + ' $ ' + url + ' $ '
        print(s)



  return

def test():
  s = '846890339:661920 846890339:755475 846890340:197141 168.237.7.10:1163 83.153.38.208:80 2 8 4294967295 4294967295 846615753 176 2462 39 GET 21068906053917068819..html HTTP/1.0'
  match = re.search(r'(\d\d\d\d\d\d+:\d\d\d\d+) (\d\d\d\d\d\d+:\d\d\d\d+) (\d\d\d\d\d\d+:\d\d\d\d+) \d*.\d*.\d*.\d*:\d* \d*.\d*.\d*.\d*:\d* \d* \d* \d* \d* \d* \d* \d* \d* GET (\d+).', s)
#  print(match.group(1))
#  print(match.group(2))
#  print(match.group(3))
#  print(match.group(4))

  
#  call(['./tools/timeconvert', match.group(1)])
#  call(['./tools/timeconvert', match.group(2)])
#  call(['./tools/timeconvert', match.group(3)])
  r = subprocess.check_output(['./tools/timeconvert', match.group(1)])
  r = r.decode("utf-8")
  match2 = re.search(r'\w+\s+\w+\s+\d+\s+\d+:\d+:\d+\s+\d+',r)
  print(match2.group())
  return

def test_file(filename):
  f = open(filename, 'r')
  num = 0
  for line in f:
    print(line)
    print(num)
    num = num + 1
    match = re.search('GET (\d+).', line)

  return

def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [trace_file]')
    sys.exit(1)

  for arg in args:
#    test_file(arg)
    parse_trace_file(arg)
#    test()

    
if __name__ == '__main__':
  main()
