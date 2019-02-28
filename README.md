# anz-test2
Test for ANZ Technical Interview

## Building the Application Artefact

### Commands
- docker build --build-arg BUILD_VERSION=2 --build-arg COMMIT_SHA=abc123 -t anz-test2 .
- A git commit will trigger the Travis CI Build - [GitHub](https://travis-ci.org/csSilencer/anz-test2) - Also see [.travis.yml](.travis.yml)

### Notes on Implementation of build:
- See the Dockerfile
- It is set up as a multistage build to not pull across items not needed for the runtime
- Copying over requirements.txt and requirements_text.txt explicitly so that it doesn't trigger redownloading and rebuilding python requirements on every build.
- Build metadata is injected via build arguments, which are then passed onto the application
  this is a bit sloppy when using the command line, however with more work and docker-compose, this could be tidied up
- When passing the build metadata through build arguments, this gives us the ability to pull in metadata from our build tool, Travis CI in this instance.

## Running the Application
- docker build --build-arg BUILD_VERSION=2 --build-arg COMMIT_SHA=abc123 -t anz-test2 .
- Take the build image
- docker run -p 5000:5000 anz-test2

## Server implementation
- A simple python webapp with the required healthcheck endpoint [Flask](http://flask.pocoo.org/)

## Choice on Docker
Taking, somewhat literally the requirement to: "Containerise your application as a single deployable artifact, encapsulating all dependencies."
I felt Docker was a good choice, although these files could be archived and perhaps run on a PaaS or Serverless platform.
Docker is a quick and easy way to build the app such that artifact and required run-time for development, testing, and deploying is slim and fit to purpose
Bonus points for being the easiest to deploy - No need to write loads of boilerplate / bootstrapping to get it running on a host, or even easier, a serverless platform such as AWS Fargate.