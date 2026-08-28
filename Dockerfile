FROM python:3.11

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# System deps required by weasyprint (PDF generation) and PyMuPDF.
# Retry apt-get a few times to work around transient mirror/network
# failures, and always clean up the apt cache afterwards to keep the
# image small.
RUN set -eux; \
    for i in 1 2 3; do \
        apt-get update && break || sleep 5; \
    done; \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        libffi-dev \
        fonts-liberation \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/data

# Mini App server port (only listens if MINI_APP_DOMAIN is configured / the
# miniapp component is actually started -- harmless to expose otherwise).
EXPOSE 8080

CMD ["python", "run.py"]
