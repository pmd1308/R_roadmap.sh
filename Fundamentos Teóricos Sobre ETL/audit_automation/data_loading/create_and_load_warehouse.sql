-- Criação do Data Warehouse
CREATE DATABASE AuditDataWarehouse;
GO

USE AuditDataWarehouse;
GO

-- Criação de tabelas para dados brutos
CREATE TABLE RawData_ERP (
    ID INT PRIMARY KEY,
    Data NVARCHAR(MAX)
);

CREATE TABLE RawData_CSV (
    ID INT PRIMARY KEY,
    Data NVARCHAR(MAX)
);

CREATE TABLE RawData_API (
    ID INT PRIMARY KEY,
    Data NVARCHAR(MAX)
);

-- Criação de tabelas de fato e dimensão
CREATE PARTITION FUNCTION AuditRangePS (INT)
AS RANGE LEFT FOR VALUES (1, 1000, 2000, 3000);

CREATE PARTITION SCHEME AuditRangePS
AS PARTITION AuditRangePS
ALL TO ([PRIMARY]);

CREATE TABLE AuditFactTable (
    ID INT PRIMARY KEY,
    Data NVARCHAR(MAX),
    Processed BIT
) ON AuditRangePS(ID);

CREATE TABLE AuditDimensionTable (
    DimensionID INT PRIMARY KEY,
    DimensionData NVARCHAR(MAX),
);
GO

-- Inserção de dados brutos

INSERT INTO AuditFactTable (ID, Data, Processed)
    SELECT ID, Data, 0
    FROM RawData_ERP;
    UNION ALL
    SELECT ID, Data, 0
    FROM RawData_CSV;
    UNION ALL
    SELECT ID, Data, 0
    FROM RawData_API;
GO