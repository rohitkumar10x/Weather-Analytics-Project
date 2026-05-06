CREATE DATABASE weather_db;

USE weather_db;
CREATE TABLE weather_data (
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    weather VARCHAR(50),
    timestamp DATETIME
);
