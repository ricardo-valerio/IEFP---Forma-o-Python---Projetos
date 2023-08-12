-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 07-Jul-2021 às 11:43
-- Versão do servidor: 10.4.18-MariaDB
-- versão do PHP: 8.0.5

--
-- Banco de dados: `agencia_viagens`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `categorias`
--

CREATE TABLE `categorias` (
  `cod_categoria` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `categorias`
--

INSERT INTO `categorias` (`cod_categoria`, `nome`) VALUES
(100, 'Cidades'),
(101, 'Praias e ilhas'),
(102, 'Cruzeiros');

-- --------------------------------------------------------

--
-- Estrutura da tabela `clientes`
--

CREATE TABLE `clientes` (
  `cod_cliente` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `apelido` varchar(50) NOT NULL,
  `titulo` varchar(20) DEFAULT NULL,
  `telemovel` varchar(20) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `clientes`
--

INSERT INTO `clientes` (`cod_cliente`, `nome`, `apelido`, `titulo`, `telemovel`, `email`) VALUES
(1, 'Joana', 'Santos', 'Eng.ª', '912222222', 'joana@live.com'),
(2, 'André', 'Santos', 'Sr.', '963333333', 'andre@gmail.com'),
(3, 'Carolina', 'Silva', 'Dra.', NULL, 'carolina@hotmail.com'),
(4, 'João', 'Pereira', 'Eng.', NULL, 'joao@gmail.com'),
(5, 'Mariana', 'Campos', 'Sra.', '914444444', NULL);

-- --------------------------------------------------------

--
-- Estrutura da tabela `compras`
--

CREATE TABLE `compras` (
  `id` int(11) NOT NULL,
  `quantidade` tinyint(3) UNSIGNED NOT NULL DEFAULT 1,
  `cod_cliente` int(11) NOT NULL,
  `cod_viagem` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `compras`
--

INSERT INTO `compras` (`id`, `quantidade`, `cod_cliente`, `cod_viagem`) VALUES
(1, 1, 1, 1000),
(2, 1, 1, 1001),
(3, 1, 2, 1000);

-- --------------------------------------------------------

--
-- Estrutura da tabela `viagens`
--

CREATE TABLE `viagens` (
  `cod_viagem` int(11) NOT NULL,
  `destino` varchar(100) NOT NULL,
  `preco` decimal(9,2) NOT NULL,
  `numero_dias` tinyint(3) UNSIGNED NOT NULL,
  `cod_categoria` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `viagens`
--

INSERT INTO `viagens` (`cod_viagem`, `destino`, `preco`, `numero_dias`, `cod_categoria`) VALUES
(1000, 'Barcelona', '200.00', 2, 100),
(1001, 'Republica Dominicana', '1100.00', 7, 101),
(1002, 'Londres', '700.00', 5, 100),
(1003, 'Jamaica', '1300.00', 7, 101);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`cod_categoria`);

--
-- Índices para tabela `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`cod_cliente`);

--
-- Índices para tabela `compras`
--
ALTER TABLE `compras`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_compras_clientes1_idx` (`cod_cliente`),
  ADD KEY `fk_compras_viagens1_idx` (`cod_viagem`);

--
-- Índices para tabela `viagens`
--
ALTER TABLE `viagens`
  ADD PRIMARY KEY (`cod_viagem`),
  ADD KEY `fk_viagens_categorias_idx` (`cod_categoria`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `categorias`
--
ALTER TABLE `categorias`
  MODIFY `cod_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;

--
-- AUTO_INCREMENT de tabela `clientes`
--
ALTER TABLE `clientes`
  MODIFY `cod_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de tabela `compras`
--
ALTER TABLE `compras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `viagens`
--
ALTER TABLE `viagens`
  MODIFY `cod_viagem` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1004;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `compras`
--
ALTER TABLE `compras`
  ADD CONSTRAINT `fk_compras_clientes1` FOREIGN KEY (`cod_cliente`) REFERENCES `clientes` (`cod_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_compras_viagens1` FOREIGN KEY (`cod_viagem`) REFERENCES `viagens` (`cod_viagem`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limitadores para a tabela `viagens`
--
ALTER TABLE `viagens`
  ADD CONSTRAINT `fk_viagens_categorias` FOREIGN KEY (`cod_categoria`) REFERENCES `categorias` (`cod_categoria`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

