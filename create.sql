CREATE TABLE transmission
(
  transmission_id INT NOT NULL,
  type_transmission CHAR(40) NOT NULL,
  PRIMARY KEY (transmission_id)
);

CREATE TABLE fuel
(
  fuelType_id INT NOT NULL,
  fuelType CHAR(40) NOT NULL,
  PRIMARY KEY (fuelType_id)
);

CREATE TABLE engine
(
  engineSize_id INT NOT NULL,
  engineSize FLOAT NOT NULL,
  PRIMARY KEY (engineSize_id)
);

CREATE TABLE Mercedes
(
  mers_class CHAR(40) NOT NULL,
  model_id INT NOT NULL,
  mers_year INT NOT NULL,
  price INT NOT NULL,
  transmission_id INT NOT NULL,
  fuelType_id INT NOT NULL,
  engineSize_id INT NOT NULL,
  PRIMARY KEY (model_id),
  FOREIGN KEY (transmission_id) REFERENCES transmission(transmission_id),
  FOREIGN KEY (fuelType_id) REFERENCES fuel(fuelType_id),
  FOREIGN KEY (engineSize_id) REFERENCES engine(engineSize_id)
);