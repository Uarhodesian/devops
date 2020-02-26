# Metrics collection script
***
#INSTALLATION
***
#1 step: put in work docker dir our files metrics.py and Dockerfile
#2 docker build -t metrics .
#3 docker run metrics
***
#QUICK START
#to specify metrics we should edit the last string Dockerfile
#if we want to see cpu CMD [ "python", "./metrics.py", "cpu" ]
#for memory CMD [ "python", "./metrics.py", "mem" ]
#Cheers!
