FROM python:3.10-slim AS build
WORKDIR /app
RUN pip install --upgrade pip
COPY . .
EXPOSE 4000

FROM python:3.10-alpine
WORKDIR /app
COPY --from=build /app /app
CMD ["python", "final.py"]