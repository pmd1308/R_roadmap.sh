-- Carregamento de dados a partir de fontes externas
-- Exemplo de carga incremental
INSERT INTO RawData_ERP (ID, Data)
SELECT ID, Data
FROM ExternalERPSource
WHERE Date > @LastExtractDate;
GO

-- Recarregamento de dados
EXEC ExtractFromAPI;
EXEC ExtractFromCSV;
