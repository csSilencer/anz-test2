FROM python:latest as test

COPY . .

RUN pip install --no-cache-dir -r requirements_test.txt

RUN ./linting.sh

FROM python:latest as package

WORKDIR /usr/src/app

COPY --from=test ./anz-test2.py .
COPY --from=test ./requirements.txt .
COPY --from=test ./build_metadata.json .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "./anz-test2.py" ]
