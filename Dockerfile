# syntax=docker/dockerfile:1
FROM python:3.13.0-slim AS builder

COPY . /taylorsbot/
WORKDIR /taylorsbot/

RUN python -m pip install --upgrade pip poetry-core
#RUN pip wheel --no-deps -w wheels .

FROM python:3.13.0-slim

#COPY --from=builder /louisoix-bot/wheels/ /wheels/

# Find and install the most recent version of the wheel, in case there are multiple (local dev, mainly)
#RUN pip install $(find /wheels -name 'louisoix_bot*.whl' -exec stat -c '%Y %n' {} \; | sort -nr | awk '{print $2}')
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "taylorsbot.py", "--dry-run" ]