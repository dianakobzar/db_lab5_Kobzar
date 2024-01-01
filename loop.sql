CREATE TABLE engine_copy AS 
SELECT * FROM engine;

SELECT * FROM engine_copy;

DO $$ 
DECLARE
    engsize_id INT;
    engsize NUMERIC;
BEGIN
     engsize_id := 12;
     engsize := 2.7;
    FOR i IN 1..3 
		LOOP
        	INSERT INTO engine_copy(enginesize_id, enginesize) 
			VALUES (engsize_id + i, engsize + i);
    	END LOOP;
END 
$$;

DROP TABLE engine_copy;