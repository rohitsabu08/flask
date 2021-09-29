
#copy base imgae from docker hub
FROM python:3.6.1-alpine   
# changing working directory
WORKDIR /project
#copying local files to project directory
ADD . /project
#installing requirements
RUN pip install --upgrade pip
RUN pip install -r requirement.txt
#  Run file
CMD ["python","main.py"]

