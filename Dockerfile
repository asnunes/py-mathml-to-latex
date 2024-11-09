FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml setup.cfg setup.py MANIFEST.in README.md LICENSE.md /app/

RUN pip install --upgrade pip
RUN pip install build twine pytest

COPY . .

CMD ["python", "-m", "unittest", "discover", "tests"]
