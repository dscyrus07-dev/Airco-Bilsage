import jwt
import requests
import os
from dotenv import load_dotenv
import threading
import time

load_dotenv("backend/.env")

secret = os.getenv("SUPABASE_JWT_SECRET")
supabase_url = os.getenv("SUPABASE_URL")

payload = {
    "role": "authenticated",
    "sub": "e613cd3a-c4bd-45f9-a5d6-6bedbf19743b",
    "email": "demo1@gmail.com",
    "aud": "authenticated",
    "iss": f"{supabase_url}/auth/v1",
    "exp": int(time.time()) + 3600
}

token = jwt.encode(payload, secret, algorithm="HS256")

url = "http://localhost:8000/api/auth/me"
headers = {"Authorization": f"Bearer {token}"}

def make_request(req_id):
    print(f"Request {req_id} starting...")
    try:
        res = requests.get(url, headers=headers, timeout=15)
        print(f"Request {req_id} finished with status {res.status_code}")
        print(f"Request {req_id} response: {res.text[:100]}")
    except Exception as e:
        print(f"Request {req_id} failed: {e}")

# Try 1 request
make_request(1)
print("---")
# Try 2nd request
make_request(2)

print("--- Concurrent ---")
t1 = threading.Thread(target=make_request, args=(3,))
t2 = threading.Thread(target=make_request, args=(4,))
t1.start()
t2.start()
t1.join()
t2.join()
