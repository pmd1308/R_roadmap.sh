-- Limpeza e normalização de dados
-- Exemplo de limpeza de dados inválidos
DELETE FROM AuditFactTable
WHERE Data IS NULL;

-- Normalização de dados
UPDATE AuditFactTable
SET Data = TRIM(Data);
GO
