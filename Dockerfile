# Official python image
FROM python:3.11-slim-buster as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONOTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base as python-deps

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

#Install python dependencies in /.venv
COPY Pipfile ./
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install

FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH:/usr/local/bin"

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Install application into container
COPY . .