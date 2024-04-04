# syntax=docker/dockerfile:1

FROM python:3.12-alpine

WORKDIR /app

#copy contents into the working dir
ADD . /app

# install the dependencies
RUN pip install -r requirements.txt

COPY . .

# change app.py to app.run(port=443, host='0.0.0.0')
EXPOSE 443
ENTRYPOINT [./app.py]

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]