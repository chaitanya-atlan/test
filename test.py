import requests
import numpy as np

# Test requests
response = requests.get('https://api.github.com')
print('Status Code:', response.status_code)

# Test numpy
array = np.array([1, 2, 3])
print('Numpy Array:', array)
