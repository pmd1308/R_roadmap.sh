library(DBI)
library(odbc)
library(dplyr)

# BD Configuration
con <- dbConnect(odbc::odbc(), "audit_production")
data <- dbGetQuery(con, "SELECT * FROM AuditFactTable WHERE Processed = 1")

# Função para identificar outliers com IQR
find_outliers <- function(values) {
    q1 <- quantile(values, 0.25)
    q3 <- quantile(values, 0.75)
    iqr <- IQR(values)
    lower_bound <- q1 - 1.5 * iqr
    upper_bound <- q3 + 1.5 * iqr
    outliers <- values[values < lower_bound | values > upper_bound]
    return(outliers)
}

# Verificando a correlação entre variáveis

correlation_matrix <- cor(data[c("Value", "OtherVariable")], method = "pearson")

# Segmentação dos dados
# Exemplo de segmentação por categorias
segmented_data <- data %>%
  group_by(Category) %>%
  summarize(mean_value = mean(Value), max_value = max(Value))