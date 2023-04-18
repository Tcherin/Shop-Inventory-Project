DROP TABLE IF EXISTS videos;
DROP TABLE IF EXISTS suppliers;

CREATE TABLE suppliers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  contact_number VARCHAR(255),
  activity BOOLEAN
);

CREATE TABLE videos (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  genre VARCHAR(255),
  description VARCHAR(255),
  stock_quantity INT,
  buying_cost INT,
  selling_price INT,
  supplier_id INT NOT NULL REFERENCES suppliers(id)
);