CREATE DATABASE ent_database;
USE ent_database;

CREATE TABLE user(
    id int primary key auto_increment,
    Nome varchar(100),
    Telefone varchar(30),
    Minibio varchar(200),
    Entrevista int,
    Teorico int,
    Pratico int,
    Soft_Skills int
);


INSERT INTO user VALUES(0,'Mathias Luz de Aleluia','(15) 99999-9999','I Dont know what to put here',10,5,9,2);
INSERT INTO user VALUES(0,'Lucas Fernando Alejado','(15) 99999-9999','I Dont know what to put here',8,4,10,10);
INSERT INTO user VALUES(0,'Matheus Abreu Curvelo Luz','(15) 99999-9999','I Dont know what to put here',5,10,10,1);
INSERT INTO user VALUES(0, 'João Silva', '(15) 12345-6789', 'I Dont know what to put here', 3, 6, 9, 7);
INSERT INTO user VALUES(0, 'Ana Santos', '(15) 98765-4321', 'I Dont know what to put here', 2, 8, 4, 3);
INSERT INTO user VALUES(0, 'Mariana Oliveira', '(15) 55555-5555', 'I Dont know what to put here', 7, 1, 2, 8);
INSERT INTO user VALUES(0, 'Pedro Pereira', '(15) 77777-7777', 'I Dont know what to put here', 10, 9, 6, 4); 
INSERT INTO user VALUES(0, 'Carla Ferreira', '(15) 11111-1111', 'I Dont know what to put here', 1, 5, 3, 10); 
INSERT INTO user VALUES(0, 'Rafaela Mendes', '(15) 44444-4444', 'I Dont know what to put here', 6, 2, 7, 0); 
INSERT INTO user VALUES(0, 'Gustavo Rodrigues', '(15) 22222-2222', 'I Dont know what to put here', 8, 10, 5, 9); 
INSERT INTO user VALUES(0, 'Luis Barbosa', '(15) 88888-8888', 'I Dont know what to put here', 4, 3, 8, 6); 
INSERT INTO user VALUES(0, 'Cristina Ribeiro', '(15) 66666-6666', 'I Dont know what to put here', 0, 7, 1, 2);
INSERT INTO user VALUES(0, 'Fernando Almeida', '(15) 99999-9999', 'I Dont know what to put here', 9, 4, 10, 7);
INSERT INTO user VALUES(0, 'Beatriz Nogueira', '(15) 12345-6789', 'I Dont know what to put here', 5, 6, 3, 1);
INSERT INTO user VALUES(0, 'Ricardo Oliveira', '(15) 98765-4321', 'I Dont know what to put here', 2, 8, 7, 5);
INSERT INTO user VALUES(0, 'Lucia Santos', '(15) 55555-5555', 'I Dont know what to put here', 8, 1, 9, 10);
INSERT INTO user VALUES(0, 'Eduardo Lima', '(15) 77777-7777', 'I Dont know what to put here', 6, 9, 2, 4);
INSERT INTO user VALUES(0, 'Isabel Fernandes', '(15) 11111-1111', 'I Dont know what to put here', 3, 5, 10, 8);
INSERT INTO user VALUES(0, 'Miguel Ribeiro', '(15) 44444-4444', 'I Dont know what to put here', 7, 2, 4, 1);
INSERT INTO user VALUES(0, 'Carolina Alves', '(15) 22222-2222', 'I Dont know what to put here', 4, 10, 8, 6);
INSERT INTO user VALUES(0, 'Hugo Pereira', '(15) 88888-8888', 'I Dont know what to put here', 1, 3, 5, 9);
INSERT INTO user VALUES(0, 'Sofia Barbosa', '(15) 66666-6666', 'I Dont know what to put here', 9, 7, 6, 3);
INSERT INTO user VALUES(0, 'Antonio Nogueira', '(15) 12345-6789', 'I Dont know what to put here', 0, 4, 1, 7);