FROM python

ENV PYTHONPATH="usr/src"

WORKDIR /usr/src

COPY /docker/backend/requirements.txt /opt/requirements.txt

RUN python3 -m pip uninstall JWT
RUN python3 -m pip install --no-cache-dir -r /opt/requirements.txt

COPY /backend /usr/src

EXPOSE 5000

CMD ["python3", "/usr/src/app.py"]