FROM python:3.13.0b1-bullseye

WORKDIR /horoscope

# SOURCE is the name of the horoscope file that should be copied
# as app.py. This lets us use one project and one Dockerfile to
# build all the different images. So use --build-args SOURCE=filename.py
# with a different filename each time, and change the image tag
# accordingly.

ARG SOURCE
ENV SOURCE_FILE=$SOURCE

COPY $SOURCE_FILE ./app.py
COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 3000

CMD ["python3", "-m", "flask", "run", "-p", "3000", "--host", "0.0.0.0"]