REM Build Docker image
docker build -t image-classification-app .

REM Run Docker container
docker run -p 3300:3300 image-classification-app