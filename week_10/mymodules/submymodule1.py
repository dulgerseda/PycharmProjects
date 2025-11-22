
import numpy as np

numbers = [
    0.029548892930490567, 0.5511592554631579, 0.2773069769785136,
    0.7275575687582001, 0.867401726407296, 0.9543276773207937,
    0.36067950811038096, 0.018031120836858983, 0.40502129553627654,
    0.47025653079756413, 0.45584147839856937, 0.6286176913123153,
    0.5382626903685851, 0.524902472180474, 0.44960934817355613
]

p_50 = np.percentile(numbers, 50)
p_95 = np.percentile(numbers, 95)

print("50th percentile (median):", p_50)
print("95th percentile:", p_95)

p_50_r = round(np.percentile(numbers, 50), 2)
p_95_r = round(np.percentile(numbers, 95), 2)


print("50th percentile (median):", p_50_r)
print("95th percentile:", p_95_r)