-- Criação de índices para melhorar o desempenho das consultas
CREATE INDEX idx_data ON AuditFactTable (Data);
CREATE INDEX idx_period_category ON AggregatedData (Period, Category);
GO

-- Planos de execução para consultas SQL
-- Exemplo de análise de plano de execução para consulta
EXEC sp_executesql N'SELECT * FROM AuditFactTable WHERE Data LIKE ''%Audit%''';
GO
