#for local testing, you can build and run your docker image locally
docker build . -f Dockerfile -t my_image

#to run the docker image:
docker run -p 8080:8080 -v $GOOGLE_APPLICATION_CREDENTIALS:/my-project-ycng-228-363013-b46cd4c4412c.json -e GOOGLE_APPLICATION_CREDENTIALS=/my-project-ycng-228-363013-b46cd4c4412c.json my_image
#to log into the docker image:
docker run -it -p 8080:8080 -v $GOOGLE_APPLICATION_CREDENTIALS:/my-project-ycng-228-363013-b46cd4c4412c.json -e GOOGLE_APPLICATION_CREDENTIALS=/my-project-ycng-228-363013-b46cd4c4412c.json my_image /bin/bash
