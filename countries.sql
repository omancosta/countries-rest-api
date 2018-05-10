CREATE TABLE IF NOT EXISTS countries (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    capital VARCHAR(100) NOT NULL,
    relevance FLOAT NULL,
    region VARCHAR(14) NULL,
    subregion VARCHAR(25) NULL,
    population INT NULL,
    demonym VARCHAR(45) NULL,
    area FLOAT NULL,
    gini FLOAT NULL,
    native_name VARCHAR(59) NULL,
    alpha2_code VARCHAR(2) NULL,
    alpha3_code VARCHAR(3) NULL
);

INSERT INTO countries VALUES(1,"Germany","Berlin",3.0,"Europe","Western Europe",81083600,"German",357114.0,28.3,"Deutschland","DE","DEU");