"""
Created on Nov 10 2017

@author: EnriqueAldana
"""

import sys,getopt
import redis

    
def main(argv):
   hostnameParameter = 'localhost'
   hostportParameter = 6379
   hostdatabaseName =0 
   keyName='key1'
   keyValue='value0'
   arguments=0
   
   try:
      opts, args = getopt.getopt(argv,"h:n:p:d:k:v:",["hostnameParameter=","hostportParameter=","hostdatabaseName=","keyName=","keyValue="])
      arguments=args
   except getopt.GetoptError:
       print ('appPython2Redis.py -n <Redis host name>  -p <Redis host port> -d <Redis Database name> -k <key Name> -v <key Value> ')
       sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':   # Requested Help to use it
         print ('appPython2Redis.py -n <Redis host name>  -p <Redis host port> -d <Redis Database name> -k <key Name> -v <key Value>')
         sys.exit()
      
       elif opt in ("-n", "--hostnameParameter"):
         hostnameParameter = arg
         
       elif opt in ("-p", "--hostportParameter"):
         hostportParameter = arg
         
       elif opt in ("-d", "--hostdatabaseName"):
         hostdatabaseName = arg
       elif opt in ("-k", "--keyName"):
         keyName = arg
       elif opt in ("-v", "--keyValue"):
         keyValue = arg
      
   if len(arguments)== 0:
          if hostnameParameter==None:
              hostnameParameter = 'localhost'
          if hostportParameter==None:
              hostportParameter= 6779
          if hostdatabaseName==None:
              hostdatabaseName=0
             
          print('appPython2Redis program has been started ')      
          print ('Host name is ', hostnameParameter)
          print ('Port number is ', hostportParameter)
          print ('hostdatabaseName ' ,hostdatabaseName)
          print ('Key Name ' ,keyName)
          print ('Key Value ' ,keyValue)
          
          try :
          	client = redis.StrictRedis(host=hostnameParameter,port=hostportParameter,db=hostdatabaseName)
          	client.set(keyName,keyValue)
          	print("Get value from " , keyName, " " , client.get(keyName))
          except  redis.exceptions.ConnectionError:
           	print("Error trying to connect to Redis: ", sys.exc_info()[0])
         
          
   
   
if __name__ == "__main__":
   main(sys.argv[1:])  
   
