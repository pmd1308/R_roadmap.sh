-- Particionamento dos dados
ALTER PARTITION FUNCTION AuditRangePF()
MERGE RANGE (1000);

-- Atualização dos dados na tabela de fato
UPDATE AuditFactTable
SET Processed = 1
WHERE Processed = 0;
GO