DROP TABLE IF EXISTS films;
DROP TABLE IF EXISTS directors;

CREATE TABLE directors (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  contact_number INT,
  activity BOOLEAN
);

CREATE TABLE films (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  genre VARCHAR(255),
  description TEXT,
  stock_quanitity INT,
  buying_cost INT,
  selling_price INT,
  director_id INT NOT NULL REFERENCES directors(id)
);