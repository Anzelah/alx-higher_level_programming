-- create a database in MySQL server
CREATE DATABASE hbtn_0c_0
IF DB_ID('hbtn_0c_0') IS NULL
BEGIN
	RETURN 0;
END
ELSE
BEGIN
	RETURN 1;
END
