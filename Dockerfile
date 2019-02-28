FROM python:2 as test

COPY requirements_test.txt .
RUN pip install --no-cache-dir -r requirements_test.txt

COPY . .
RUN ./linting.sh && python -m unittest discover

FROM python:2 as package

ARG BUILD_VERSION
ARG COMMIT_SHA

ENV BUILD_VERSION=${BUILD_VERSION}
ENV COMMIT_SHA=${COMMIT_SHA}

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --from=test ./main/app.py .
COPY --from=test ./inject_build_metadata.sh .
COPY --from=test ./main/build_metadata.json .

RUN ./inject_build_metadata.sh

EXPOSE 5000

CMD [ "python", "./app.py" ]
