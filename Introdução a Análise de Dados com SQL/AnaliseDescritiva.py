def distribuição_frequencia(dados):
    """
    This function calculates the frequency distribution of elements in a given list.

    Parameters:
    dados (list): A list of elements for which the frequency distribution needs to be calculated.

    Returns:
    dict: A dictionary where the keys are the unique elements from the input list, and the values are the corresponding frequencies.
    """
    frequencia = {}
    for v in dados:
        if v in frequencia:
            frequencia[v] += 1
        else:
            frequencia[v] = 1
    return frequencia

def padroes_temporais(dados_temporais):
    """
    This function calculates the average values for each unique date in a given list of temporal data.

    Parameters:
    dados_temporais (list): A list of tuples, where each tuple contains a datetime object and a numerical value. 
                            The datetime object represents the temporal data, and the numerical value represents the corresponding data.

    Returns:
    dict: A dictionary where the keys are the unique dates (in 'YYYY-MM-DD' format) from the input list, 
          and the values are the average of the corresponding numerical values for each date.
    """
    padroes = {}
    for data, valor in dados_temporais:
        periodo = data.strftime('%Y-%m-%d')
        if periodo in padroes:
            padroes[periodo].append(valor)
        else:
            padroes[periodo] = [valor]
    
    return {periodo: sum(valores)/len(valores) for periodo, valores in padroes.items()}

def tendencia_central_e_dispersao(dados):
    """
    This function calculates the central tendency (mean, median) and dispersion (standard deviation, variance) of a given list of numbers.

    Parameters:
    dados (list): A list of numerical values for which the central tendency and dispersion need to be calculated.

    Returns:
    tuple: A tuple containing four values: the mean, median, standard deviation, and variance of the input list.
    """
    n = len(dados)
    media = sum(dados) / n
    dados_ordenados = sorted(dados)
    mediana = dados_ordenados[n // 2] if n % 2 == 1 else (dados_ordenados[n // 2 - 1] + dados_ordenados[n // 2]) / 2
    variancia = sum((x - media) **2 for x in dados) /n
    desvio_padrao = variancia ** 0.5
    return media, mediana, desvio_padrao, variancia

def outliers(data):
    """
    This function identifies and returns the outliers in a given list of numerical data using the Interquartile Range (IQR) method.

    Parameters:
    data (list): A list of numerical values for which outliers need to be identified.

    Returns:
    list: A list of outliers present in the input data. An outlier is defined as a data point that falls below the lower bound or above the upper bound,
          calculated as follows:
          lower_bound = Q1 - 1.5 * IQR
          upper_bound = Q3 + 1.5 * IQR
          where Q1 is the first quartile (25th percentile), Q3 is the third quartile (75th percentile), and IQR is the interquartile range (Q3 - Q1).
    """
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data) // 4]
    q3 = sorted_data[3 * len(sorted_data) // 4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return [x for x in data if x < lower_bound or x > upper_bound]

def distribuicao(data, num_bins):
    """
    This function calculates the frequency distribution of a given list of numerical data into specified bins.

    Parameters:
    data (list): A list of numerical values for which the frequency distribution needs to be calculated.
    num_bins (int): The number of bins into which the data will be divided.

    Returns:
    list: A list of integers representing the frequency of each bin. The length of the list is equal to num_bins.
          The index of each integer in the list corresponds to the bin number, starting from 0.
    """
    min_val = min(data)
    max_val = max(data)
    interval = (max_val - min_val) / num_bins
    bins = [0] * num_bins
    for x in data:
        bin_index = int((x - min_val) / interval)
        if bin_index == num_bins:
            bins[bin_index] -= 1    
        bins[bin_index] += 1
    return bins

def correlacao(x, y):
    """
    Calculates the Pearson correlation coefficient between two lists of numerical data.

    The Pearson correlation coefficient measures the linear relationship between two variables.
    It ranges from -1 to 1, where -1 indicates a strong negative linear relationship, 0 indicates no linear relationship,
    and 1 indicates a strong positive linear relationship.

    Parameters:
    x (list): A list of numerical values representing the first variable.
    y (list): A list of numerical values representing the second variable. The length of this list must be equal to the length of the first list.

    Returns:
    float: The Pearson correlation coefficient between the two input lists.
    """
    n = len(x)
    media_x = sum(x) / n
    media_y = sum(y) / n
    numerador = sum((xi - media_x) * (yi - media_y) for xi, yi in zip(x, y))
    denominador = (sum((xi - media_x) ** 2 for xi in x) * sum((yi - media_y) ** 2 for yi in y))
    return numerador / denominador

def kmmeans(data, k):
    """
    Performs the K-means clustering algorithm on a given dataset.

    The K-means algorithm is an unsupervised learning method used to partition n observations into k clusters,
    where each observation belongs to the cluster with the nearest mean (cluster centers or centroids).

    Parameters:
    data (list): A list of n-dimensional data points. Each data point is represented as a list of n values.
    k (int): The number of clusters to form.

    Returns:
    list: A list of k clusters. Each cluster is represented as a list of data points belonging to that cluster.
    """
    import random
    centroid = random.sample(data, k)
    while True:
        clusters = [[] for _ in range(k)]
        for point in data:
            cluster_index = min(range(k), key=lambda i: sum((point[i] - centroid[i]) ** 2 for i in range(len(point))))
            clusters[cluster_index].append(point)
        new_centroids = []
        for cluster in clusters:
            if len(cluster) > 0:
                new_centroid = [sum(point[i] for point in cluster) / len(cluster) for i in range(len(cluster[0]))]
                new_centroids.append(new_centroid)
        if new_centroids == centroid:
            break
        centroid = new_centroids
    return clusters

"""
################################################################
Using GPU
"""

import cupy as cp

def distribuicao_frequencia_cuda(dados):
    """
    This function calculates the frequency distribution of elements in a given list using GPU acceleration.

    Parameters:
    dados (list): A list of elements for which the frequency distribution needs to be calculated. 
                  The elements can be of any type that is supported by the 'cupy' library.

    Returns:
    dict: A dictionary where the keys are the unique elements from the input list, and the values are the corresponding frequencies.
          The frequencies are calculated using GPU acceleration, which can significantly improve performance for large datasets.
    """
    data_gpu = cp.array(dados)
    unique_values, count = cp.unique(data_gpu, return_counts=True)
    return {unique_value.item(): count_value.item() for unique_value, count_value in zip(unique_values, count)}






def padroes_temporais_cuda(dados_temporais):
    """
    This function calculates the average values for each unique month in a given list of temporal data using GPU acceleration.

    Parameters:
    dados_temporais (list): A list of tuples, where each tuple contains a datetime object and a numerical value. 
                            The datetime object represents the temporal data, and the numerical value represents the corresponding data.

    Returns:
    dict: A dictionary where the keys are the unique months (in 'YYYY-MM' format) from the input list, 
          and the values are the average of the corresponding numerical values for each month.
          The averages are calculated using GPU acceleration, which can significantly improve performance for large datasets.
    """
    import pandas as pd
    import cupy as cp

    df = pd.DataFrame(dados_temporais, columns=['data', 'valor'])
    df['data'] = pd.to_datetime(df['data'])
    df['periodo'] = df['data'].dt.to_period('M')

    dados_gpu = cp.array(df[['periodo', 'valor']].values)
    periodos, valores = dados_gpu[:, 0], dados_gpu[:, 1]
    unicos, inversos = cp.unique(periodos, return_inverse=True)
    somas = cp.zeros(len(unicos))
    contagem = cp.zeros(len(unicos))

    for i, valor in enumerate(valores):
        somas[inversos[i]] += valor
        contagem[inversos[i]] += 1

    return {unico.get(): (soma / cont).get() for unico, soma, cont in zip(unicos, somas, contagem)}

def tendencia_central_e_dispersao_cuda(dados):
    dados_gpu = cp.array(dados)
    media = cp.mean(dados_gpu)
    dados_ordenados = cp.sort(dados_gpu)
    n = len(dados_ordenados)
    mediana = dados_ordenados[n // 2] if n % 2 == 1 else (dados_ordenados[n // 2 - 1] + dados_ordenados[n // 2]) / 2
    variancia = cp.var(dados_gpu)
    desvio_padrao = cp.std(variancia)
    minimo = cp.min(dados_gpu)
    maximo = cp.max(dados_gpu)
    return media.get(), mediana.get(), desvio_padrao.get(), variancia.get(), minimo.get(), maximo.get()

def outliers_cuda(dados):
    dados_gpu = cp.array(dados)
    q1 = cp.percentile(dados_gpu, 25)
    q3 = cp.percentile(dados_gpu, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return cp.where((dados_gpu < lower_bound) | (dados_gpu > upper_bound))[0].tolist()

def distribuicao_cuda(dados, num_bins):
    dados_gpu = cp.array(dados)
    min_val = cp.min(dados_gpu)
    max_val = cp.max(dados_gpu)
    intervalo = (max_val - min_val) / num_bins
    bins = cp.zeros(num_bins, dtype=cp.int32)
    for x in dados_gpu:
        bin_index = cp.int32((x - min_val) / intervalo)
        if bin_index == num_bins:
            bins[bin_index - 1] -= 1    
        bins[bin_index] += 1
    return bins.tolist()

def correlacao_cuda(x, y):
    x_gpu = cp.array(x)
    y_gpu = cp.array(y)
    correlacao = cp.corrcoef(x_gpu, y_gpu)[0, 1]
    return correlacao.get()

def kmmeans_cuda(dados, k):
    """
    Performs the K-means clustering algorithm on a given dataset using GPU acceleration.

    The K-means algorithm is an unsupervised learning method used to partition n observations into k clusters,
    where each observation belongs to the cluster with the nearest mean (cluster centers or centroids).
    This implementation uses the GPU for acceleration, which can significantly improve performance for large datasets.

    Parameters:
    dados (list): A list of n-dimensional data points. Each data point is represented as a list of n values.
    k (int): The number of clusters to form.

    Returns:
    list: A list of k clusters. Each cluster is represented as a list of data points belonging to that cluster.
          The data points are converted back to Python lists before being returned.
    """
    dados_gpu = cp.array(dados)
    centroids = cp.random.choice(dados_gpu, k)
    while True:
        clusters = [[] for _ in range(k)]
        for point in dados_gpu:
            cluster_index = cp.argmin(cp.sum((point - centroid) ** 2 for centroid in centroids), axis=1)
            clusters[cluster_index].append(point)
        new_centroids = cp.array([cp.mean(cluster, axis=0) for cluster in clusters])
        if cp.allclose(new_centroids, centroids):
            break
        centroids = new_centroids
    return [cluster.tolist() for cluster in clusters]
