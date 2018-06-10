# wikitolearn-math-backend

## Synopsis
WikiToLearn Math Backend is a backend service of the WikiToLearn architecture.
The backend service should be imagined as a unique service but its APIs are served by three different backends:

* Formulas backend service: a Python Eve RESTful API which serves rendered formulas stored on MongoDB
* TeXLive backend service: a Flask app which is responsible for rendering the formulas using TexLive. This will ensure formulas will be also rendered within PDFs
* Mathoid backend service: see [mathoid](https://github.com/wikimedia/mathoid)

These three services are exposed behind a reverse proxy that acts as an entrypoint.

## Development
We use Docker to speed-up development and setup the environment without any dependency issues.

### Minimum requirements
* Docker Engine 17.09.0+

### How to run
It is advisable to run using the `docker-compose.yml` file provided.

Run instructions:

* Build all docker containers with: `docker-compose -f docker-compose.yml  -f docker-compose-dev-deps.yml build`
* Run all docker containers with: `docker-compose -f docker-compose.yml  -f docker-compose-dev-deps.yml up`

## Versioning
We use [SemVer](http://semver.org/) for versioning.

## License
This project is licensed under the AGPLv3+. See the [LICENSE.md](LICENSE.md) file for details.
