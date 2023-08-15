-- create a database in MySQL server
CREATE DATABASE hbtn_0c_0
IF DB_ID('hbtn_0c_0') IS NOT NULL
BEGIN
	return 1
END
