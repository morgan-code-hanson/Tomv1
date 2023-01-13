# start by pulling image
FROM python:3.10.7-slim-buster
# set workdir
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install system dependencies
RUN apt-get update && apt-get install -y netcat
# install the dependencies and packages in the requirements file
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
# copy every content from the local file to the image
COPY . /usr/src/app/
# make sure entrypoint has permissions
RUN chmod +x entrypoint.sh
# configure the container to run in an executed manner
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]

