-- create database all4books;
use all4books;

CREATE TABLE `cliente` (
  `cod_cliente` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `morada` varchar(300) NOT NULL,
  `sexo` char(1) NOT NULL,
  `telefone` int(11) DEFAULT NULL,
  `telemovel` int(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cod_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE `editora` (
  `cod_editora` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `editora` varchar(200) NOT NULL,
  PRIMARY KEY (`cod_editora`),
  UNIQUE KEY `editora_UNIQUE` (`editora`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE `livro` (
  `cod_livro` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `titulo` varchar(200) NOT NULL,
  `ano` year(4) NOT NULL,
  `preco` decimal(5,2) NOT NULL,
  `stock` tinyint(3) unsigned NOT NULL DEFAULT 0,
  `cod_editoraFK` smallint(5) unsigned NOT NULL,
  PRIMARY KEY (`cod_livro`),
  KEY `fk_livro_editora_idx` (`cod_editoraFK`),
  CONSTRAINT `fk_livro_editora` FOREIGN KEY (`cod_editoraFK`) REFERENCES `editora` (`cod_editora`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

INSERT INTO `cliente` (`cod_cliente`, `nome`, `morada`, `sexo`, `telefone`, `telemovel`, `email`) VALUES
(1, 'Rui Santos', 'Aveiro', 'M', 234222222, 963333333, 'ruisantos@hotmail.com'),
(2, 'Joana Silva', 'Estarreja', 'F', NULL, 913333333, 'joanasilva@gmail.com'),
(3, 'Carolina Silva', 'Porto', 'F', NULL, NULL, NULL),
(4, 'Vitor Gomes', 'Porto', 'M', NULL, 912222222, NULL);

INSERT INTO `editora` (`cod_editora`, `editora`) VALUES
(1, 'Apress'),
(2, 'Wiley'),
(3, 'Packt');

INSERT INTO `livro` (`cod_livro`, `titulo`, `ano`, `preco`, `stock`, `cod_editoraFK`) VALUES
(100, 'Clean Python', 2019, '26.99', 2, 1),
(101, 'Expert Python Programming - Fourth Edition', 2021, '20.99', 1, 3),
(102, 'Learn SQL Database Programming', 2020, '20.99', 0, 3);




