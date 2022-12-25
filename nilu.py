#!/bin/python3

import requests

import argparse
  
  
# Initialize the Parser
parser = argparse.ArgumentParser(description ='-w for wordlists and -u for urls')
  
# Adding Arguments
parser.add_argument('-w', metavar ='N', 
                    type = str, nargs ='+',
                    help ='wordlists for Brute Froce')
parser.add_argument('-u', metavar ='N', 
                    type = str, nargs ='+',
                    help ='urls for Brute Froce')   

args = parser.parse_args()                                  
  
  
with open(args.w[0],'r') as wordlist:
   words = wordlist.readlines()
   
for i in words:
   response = requests.get(args.u[0]+"/"+i[:-1]+"/")
   if(response.status_code != 404):
      print(i[:-1]+"\t"+str(response.status_code))    
   
   
   
   
