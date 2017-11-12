# Python_Docker_Redis_Flask
It is an exercise to implement a simple use to Python , Docker , Redis and Flask.

The exercise consist in:
1.- Implement a python program that run a web site with a path like  http://localhost/hello and create a response with a Json format.
2.- Implement a Python program that insert a value into Radis Instance using Docker.
3.- Implement a Python program that show a once message getting of the web server - Point 1 - and print it five times with an interval of the 10 seconds
4.- Finally we need to build a  PlayBook (Ansible) that start up the Docker containers to run

Pre requirements
1.- Python 2.7.14 installed on your Desktop
2.- Docker version 17.09.0-ce installed on your Desktop
3.- Internet connection
4.- Root provileges

Procedure to test the python programs.

A) Running the Redis instance into Docket container.
Input the command line suck as:
sudo docker run --name my-redis-container -p 7001:6379 -d redis

B) Running the Python program to insert a value into Redis instance
Input the command line suck as:
python appPython2Redis.py  -n localhost -p 7001 -d 0 -k 'message' -v 'It is a demo to TATA guys'

C) Running the Python program to start up the web site.
Input the command line suck as:
sudo python appWebServer.py --hostnameParameter 'localhost' --hostportParameter 7001 --hostdatabaseName 0 --keyName 'message' --server_host 'localhost' --server_port 7171

D) Running the python program to get a message from the Web site with Json format, then show the message 5 times with 10 seconds interval
Input the command line suck us:
python appGetMesssage.py -u "http://localhost:7171/hello" -k 'message'

You can see something like this:

Consulting to http://localhost:7171/hello
looking for key value for key name message
1
It is a demo to TATA guys
2
It is a demo to TATA guys
3
It is a demo to TATA guys
4
It is a demo to TATA guys
5
It is a demo to TATA guys



