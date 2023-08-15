-- create a database in MySQL server
IF DB_ID('hbtn_0c_0') IS NULL
BEGIN
	CREATE DATABASE hbtn_0c_0
END
ELSE
BEGIN
	RETURN 1
END
