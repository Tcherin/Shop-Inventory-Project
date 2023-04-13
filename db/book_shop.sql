DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS wholesalers;

CREATE TABLE wholesalers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  contact_number INT,
  activity BOOLEAN
);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  genre VARCHAR(255),
  stock_quanitity INT,
  buying_cost INT,
  selling_price INT,
  wholesaler_id INT NOT NULL REFERENCES wholesalers(id)
);