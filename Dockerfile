FROM alpine:edge

WORKDIR /usr/src/app

RUN adduser -u 9000 -D app

RUN apk add --no-cache python2 python2-dev py-pip libffi gcc libffi-dev musl-dev openssl openssl-dev make git

COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY codeclimate-ansiblereview /usr/src/app
RUN chown -R app:app /usr/src/app

RUN git clone https://github.com/Rob-Powell/ansible-review.git

USER app

WORKDIR /code

CMD ["/usr/src/app/ansible-review/codeclimate-ansiblereview"]
