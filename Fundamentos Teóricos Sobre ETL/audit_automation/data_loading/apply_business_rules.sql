-- Aplicação de regras de negócio específicas
-- Exemplo: Definir regras de auditoria
UPDATE AuditFactTable
SET AuditStatus = CASE
    WHEN Value > 1000 THEN 'High'
    WHEN Value BETWEEN 500 AND 1000 THEN 'Medium'
    ELSE 'Low'
END;
GO
