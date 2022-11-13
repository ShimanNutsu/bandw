FROM python:3.7
ADD ./examples /code
WORKDIR /code
COPY bandw bandw
RUN pip install -r requirements.txt
CMD [ "python", "main.py" ]