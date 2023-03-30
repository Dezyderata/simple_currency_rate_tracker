FROM python:3.10

COPY . /src


RUN pip install --upgrade pip
RUN pip install -r /src/requirements.txt

ENTRYPOINT ["python", "/src/manage.py", "runserver", "0.0.0.0:8000" ]