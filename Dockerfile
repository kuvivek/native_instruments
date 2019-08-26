FROM python:2.7
MAINTAINER Vivek Kumar, vivekkumar.bitsindri@gmail.com
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py


