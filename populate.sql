--Додавання інформації в таблицю Diamond

INSERT INTO Diamond (diamond_index, color, cut, clarity, price,carat_weight)
VALUES ('1', 'E', 'Ideal', 'SI2', '326', '0.23');

INSERT INTO Diamond (diamond_index, color, cut, clarity, price,carat_weight)
VALUES ('2', 'E', 'Premium', 'SI1', '326', '0.21');

INSERT INTO Diamond (diamond_index, color, cut, clarity, price,carat_weight)
VALUES ('3', 'F', 'Good', 'VS1', '327', '0.23');

INSERT INTO Diamond (diamond_index, color, cut, clarity, price,carat_weight)
VALUES ('4', 'I', 'Premium', 'VS2', '334', '0.29');

INSERT INTO Diamond (diamond_index, color, cut, clarity, price,carat_weight)
VALUES ('5', 'G', 'Good', 'VVS2', '335', '0.31');

INSERT INTO Diamond (diamond_index, color, cut, clarity, price,carat_weight)
VALUES ('6', 'J', 'Very Good', 'I1', '336', '0.24');

INSERT INTO Diamond (diamond_index, color, cut, clarity, price,carat_weight)
VALUES ('7', 'D', 'Very Good', 'SI2', '336', '0.24');

INSERT INTO Diamond (diamond_index, color, cut, clarity, price,carat_weight)
VALUES ('8', 'H', 'Fair', 'VVS1', '337', '0.26');

--Додавання інформації в таблицю Desctiption

INSERT INTO Description (color) VALUES ('D');

INSERT INTO Description (color) VALUES ('E');

INSERT INTO Description (color) VALUES ('F');

INSERT INTO Description (color) VALUES ('G');

INSERT INTO Description (color) VALUES ('H');

INSERT INTO Description (color) VALUES ('I');

INSERT INTO Description (color) VALUES ('J');

--Додавання інформації в таблицю Category

INSERT INTO Category (cut) VALUES ('Ideal');

INSERT INTO Category (cut) VALUES ('Premium');

INSERT INTO Category (cut) VALUES ('Very Good');

INSERT INTO Category (cut) VALUES ('Good');

INSERT INTO Category (cut) VALUES ('Fair');

--Додавання інформації в таблицю Clarity

INSERT INTO Clarity (clarity) VALUES ('IF');

INSERT INTO Clarity (clarity) VALUES ('VVS1');

INSERT INTO Clarity (clarity) VALUES ('VVS2');

INSERT INTO Clarity (clarity) VALUES ('VS1');

INSERT INTO Clarity (clarity) VALUES ('VS2');

INSERT INTO Clarity (clarity) VALUES ('SI1');

INSERT INTO Clarity (clarity) VALUES ('SI2');

INSERT INTO Clarity (clarity) VALUES ('I1');