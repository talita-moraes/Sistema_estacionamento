-- Geração de Modelo físico

CREATE TABLE Usuario (
IDUsuario VARCHAR PRIMARY KEY,
nome VARCHAR(50) NOT NULL,
CPF VARCHAR(11) NOT NULL UNIQUE,
telefone VARCHAR(11),
tipo VARCHAR(1) CHECK (tipo = 'A' OR tipo = 'F' OR tipo='V')
)

CREATE TABLE Acesso (
IDAcesso INT PRIMARY KEY,
data_saida  TIME,
data_entrada TIME,
IDUsuario INT REFERENCES Usuário (IDUsuario)
)

