FROM python:3.10.5
WORKDIR /flaskBlog
COPY . .
RUN pip3 install -r requirements.txt
#RUN python create_db.py
#ENTRYPOINT ["python3"]
#CMD ["run.py"]
