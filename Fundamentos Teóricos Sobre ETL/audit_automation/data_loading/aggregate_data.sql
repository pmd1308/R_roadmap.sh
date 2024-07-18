-- Agregação de dados por período e categoria
CREATE TABLE AggregatedData AS
SELECT Period, Category, SUM(Value) AS TotalValue
FROM AuditFactTable
GROUP BY Period, Category;
GO
