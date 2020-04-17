CREATE TABLE Diamond(
    diamond_index INT NOT NULL,
    color CHAR(1) NOT NULL,
    cut VARCHAR2(9) NOT NULL,
    clarity VARCHAR2(4) NOT NULL,
    price INT NOT NULL,
    carat_weight VARCHAR2(4) NOT NULL);
ALTER TABLE Diamond
    ADD CONSTRAINT diamond_index_pk PRIMARY KEY(diamond_index);

CREATE TABLE Description(
    color CHAR(1) NOT NULL);
ALTER TABLE Description
    ADD CONSTRAINT color_pk PRIMARY KEY(color);    
    
CREATE TABLE Category(
    cut VARCHAR2(9) NOT NULL);
ALTER TABLE Category
    ADD CONSTRAINT cut_pk PRIMARY KEY(cut);    
    
CREATE TABLE Clarity(
    clarity VARCHAR2(4) NOT NULL);
ALTER TABLE Clarity
    ADD CONSTRAINT clarity_pk PRIMARY KEY(clarity);
    
ALTER TABLE Diamond
    ADD CONSTRAINT color_fk FOREIGN KEY(color) REFERENCES Description(color);
ALTER TABLE Diamond
    ADD CONSTRAINT cut_fk FOREIGN KEY(cut) REFERENCES Category(cut);
ALTER TABLE Diamond
    ADD CONSTRAINT clarity_fk FOREIGN KEY(clarity) REFERENCES Clarity(clarity);
