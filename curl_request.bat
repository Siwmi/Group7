@echo off

REM Define the URL
set URL=http://127.0.0.1:3300/api

REM Make a simple GET request
curl -X GET %URL%
