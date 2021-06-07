FROM python:3.6.13-stretch
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN useradd --create-home --shell /bin/bash covo
USER covo
RUN pip3 install --user --upgrade pip
RUN mkdir /home/covo/djangoapp
WORKDIR /home/covo/djangoapp
COPY requirements.txt .
ENV PATH="/home/covo/.local/bin:${PATH}"
RUN pip3 install --user -r requirements.txt
COPY . /home/covo/djangoapp/
USER root
RUN chown -R covo /home/covo/djangoapp && chmod a+x ./launch.sh
USER covo
ENTRYPOINT ["./launch.sh"]