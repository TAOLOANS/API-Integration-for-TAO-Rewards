# Python example for API integration to get TAO rewards from Bittensor network
import requests

def get_tao_rewards(address):
    url = f"https://bittensor.com/api/rewards/{address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
