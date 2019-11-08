DROP TABLE fc.product IF EXISTS;

CREATE TABLE fc.product(
    product_code VARCHAR (30),
    product_type_code VARCHAR (30),
    product_classification_code VARCHAR (30),
    genre_code VARCHAR (30),
    kanji_official_name VARCHAR (50),
    container_capacity_code VARCHAR (30),
    hot_cold_classification VARCHAR (30),
    release_date TIMESTAMP
    );
                                                                            