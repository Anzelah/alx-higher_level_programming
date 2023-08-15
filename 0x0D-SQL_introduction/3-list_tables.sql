-- list all the tables of a database my MySQL server
SELECT table_name 
FROM information_schema.tables 
WHERE table_type = 'BASE TABLE'
	AND table_schema = 'mysql'
ORDER BY table_name ASC;
