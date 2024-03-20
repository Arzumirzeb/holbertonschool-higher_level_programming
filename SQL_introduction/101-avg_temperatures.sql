-- Script that displays the average temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY agv_temp DESC;
