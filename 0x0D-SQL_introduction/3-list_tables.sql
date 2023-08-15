-- list all the tables of a database my MySQL server
SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_type = 'BASE TABLE' ORDER BY table_name ASC;
