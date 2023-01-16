FROM jupyter/minimal-notebook

LABEL author="Adam A Butchy"
LABEL org.opencontainers.image.source=https://github.com/aabutchy/Fiddl
LABEL org.opencontainers.image.description="An example repository for the MeLoDy Lab."
LABEL org.opencontainers.image.licenses=MIT

COPY requirements.txt .

RUN pip install -r requirements.txt
