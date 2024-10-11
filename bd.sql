
CREATE TABLE clients (
    id_client INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    lastname VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    phone VARCHAR(15),
    user_type VARCHAR(50)
);

CREATE TABLE products (
    id_product INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    price DECIMAL(10, 2),
    stock INT,
    imagen_url VARCHAR(255)
);

CREATE TABLE cart (
    id_cart INT AUTO_INCREMENT PRIMARY KEY,
    id_client INT,
    creation_date DATETIME,
    FOREIGN KEY (id_client) REFERENCES clients(id_client)
);

CREATE TABLE porduct_cart (
    id_porduct_cart INT AUTO_INCREMENT PRIMARY KEY,
    id_cart INT,
    id_product INT,
    quantity INT,
    FOREIGN KEY (id_cart) REFERENCES cart(id_cart),
    FOREIGN KEY (id_product) REFERENCES products(id_product)
);

CREATE TABLE transactions (
    id_transaction INT AUTO_INCREMENT PRIMARY KEY,
    id_cart INT,
    transaction_date DATETIME,
    total DECIMAL(10, 2),
    FOREIGN KEY (id_cart) REFERENCES cart(id_cart)
);

CREATE TABLE contact (
    id_contact INT AUTO_INCREMENT PRIMARY KEY,
    id_client INT,
    message TEXT,
    send_date DATETIME,
    FOREIGN KEY (id_client) REFERENCES clients(id_client)
);
