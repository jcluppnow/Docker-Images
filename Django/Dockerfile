#Install python/os.
FROM python:3.8-slim-buster

#Proceed like installing Django.

#Need a folder for Django - Set the working directory.
WORKDIR /app

#COPY requirements to working directory.
COPY requirements.txt requirements.txt

#Run the requirements text to install requirements.
RUN pip3 install -r requirements.txt

# Copy across all other files to get our application working.
# COPY from base directory (.) into this directory (.).
COPY . .

#Run the server from the command line.
#Address makes application available externally (externally visible outside container).
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]