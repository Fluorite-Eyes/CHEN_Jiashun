import os
import requests
import time

os.makedirs('assets/lottie', exist_ok=True)
files = {
    'synthetic-biology-1-optimized.lottie': 'https://integratedbiosciences.com/wp-content/themes/integratedbio/src/static/dotlottie/synthetic-biology-1-optimized.lottie',
    'synthetic-biology-2-optimized.lottie': 'https://integratedbiosciences.com/wp-content/themes/integratedbio/src/static/dotlottie/synthetic-biology-2-optimized.lottie',
    'synthetic-biology-3-optimized.lottie': 'https://integratedbiosciences.com/wp-content/themes/integratedbio/src/static/dotlottie/synthetic-biology-3-optimized.lottie',
    'chemistry-optimized.lottie': 'https://integratedbiosciences.com/wp-content/themes/integratedbio/src/static/dotlottie/chemistry-optimized.lottie',
    'ai-optimized.lottie': 'https://integratedbiosciences.com/wp-content/themes/integratedbio/src/static/dotlottie/ai-optimized.lottie'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://integratedbiosciences.com/'
}

for name, url in files.items():
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            with open(f'assets/lottie/{name}', 'wb') as f:
                f.write(r.content)
            print(f"Downloaded {name}")
        else:
            print(f"Failed to download {name}: {r.status_code}")
    except Exception as e:
        print(f"Error downloading {name}: {e}")
    time.sleep(1)
