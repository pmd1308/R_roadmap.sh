-- Exemplo de análise de plano de execução para otimização de consulta
SET SHOWPLAN_XML ON;

SELECT * FROM AuditFactTable WHERE Data LIKE '%Audit%';

SET SHOWPLAN_XML OFF;
GO
