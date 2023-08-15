-- display the average temperature (Fahrenheit) by city ordered by temperature (descending).
curl -O url
mysql -u root -p hbtn_0c_0 < sql_file
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
