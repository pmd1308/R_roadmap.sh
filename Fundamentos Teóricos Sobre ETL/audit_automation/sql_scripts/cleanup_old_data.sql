-- Limpeza de dados antigos
DELETE FROM AuditFactTable WHERE Date < DATEADD(MONTH, -6, GETDATE());
GO
