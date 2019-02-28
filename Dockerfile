FROM python:latest as test

COPY requirements_test.txt .
RUN pip install --no-cache-dir -r requirements_test.txt

COPY . .
RUN ./linting.sh

FROM python:latest as package

ARG BUILD_VERSION
ARG COMMIT_SHA

ENV BUILD_VERSION=${BUILD_VERSION}
ENV COMMIT_SHA=${COMMIT_SHA}

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --from=test ./anz-test2.py .
COPY --from=test ./inject_build_metadata.sh .
COPY --from=test ./build_metadata.json .

RUN ./inject_build_metadata.sh

EXPOSE 5000

CMD [ "python", "./anz-test2.py" ]
