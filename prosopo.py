import curl_cffi # Don't use requests, request with no HTTP/2 fingerprint will be rejected
import ua_generator

import base64
import random
import time
import math

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

import mnemonic
from substrateinterface import Keypair, KeypairType
import secrets

import hashlib

# from web2Chunk-BAiIXh43.js | Convert Binary Data to Some hex
He = []
Nn = [None]*(256*256)
for n in range(256):
    He.append(hex(n)[2:].rjust(2,"0"))
for n in range(256):
    e = n << 8
    for t in range(256):
        Nn[e | t] = He[n] + He[t]

def st(n, e):
    t = len(n) % 2 | 0
    r = len(n) - t | 0
    i = 0
    while i < r:
        e += Nn[n[i] << 8 | n[i + 1]]
        i += 2
    if t != 0:
        e += He[n[r] | 0]
    return e

def Ye(n):
    r = "0x"
    return st(n, r)

# from web2Chunk-BAiIXh43.js | Generate "Prosopo-User"
def createAccount():
    # t = "348f9b7369c8f7649f3c4ac8f9f96efe"
    t = secrets.token_hex(16)
    r = hashlib.blake2b(t.encode(), digest_size=16).hexdigest()
    i = r.encode()
    o = mnemonic.Mnemonic(language="english").to_mnemonic(i)
    a = "sr25519"
    c = Keypair.create_from_mnemonic(o, crypto_type=KeypairType.SR25519)
    return {
        "address": c.ss58_address,
        "keypair": c
    }

# from index-CvvIJ1eU.js | Generate "token" for /frictionless request
def mx(n):
    public_key = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtJjBk4884quOzXZYCnD/\ndXKAqPUkwtb76WtbG0rM5s2p2htyFT9Zo3PR/BT87OExVDfAy0iN1e2HGEQWsLAM\n8QZ7xWnG1zYolsARNhHAwv/IXsH1zUZmkujTaBpb8S4IHDHAjZLm7i4Qhr7lk/0n\nSJ+Oh2NtCkbKfjlsyoxMoN4IdE4u6T8cSn+AXwZ3F7Bk+NlkmzGMQHYeobD5Mstv\ncDsbwPCJstdnESnTxCiUSrS9SYCgxaxMB8TbmcVx5NImz0HbPZmj/nnpHJOIUR+T\nekMdw3FfZqAyAC4ARXlyWxZbOm0rF4B98HtXwVqfzcQmN9AzJBLW+p3/PXjvZECx\nZwIDAQAB\n-----END PUBLIC KEY-----\n"
    public_key = serialization.load_pem_public_key(
      public_key.encode("utf-8"),
      backend=default_backend()
    )
    cipher_text = public_key.encrypt(
      n.encode(),
      padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
      )
    )
    return base64.b64encode(cipher_text).decode()

def xe(n):
    a = int(time.time() * 1000)
    s = ((int(str(a)[-3:]) + n) / 999 * math.pi) - (math.pi / 2)
    t = math.sin(s) * 1e3
    return [a,t]

def ne():
    a = [0]*2 + [0.2] + [0]*21
    s = random.random() * 0.3
    t = min((sum(a) + s), 1)
    return {"token": mx(str(xe(t)).replace(" ",""))}

# from web2Chunk-BAiIXh43.js | just Generate PoW nonce
def i(n, e):
    t = 0
    r = "0"*e
    while True:
        i = (str(t) + n).encode()
        if hashlib.sha256(i).hexdigest().startswith(r):
            return t
        t += 1

# from web2Chunk-BAiIXh43.js | Generate Prosopo-Response
def tt(n):
    e = len(n)
    t = 0
    for i in range(e):
        t += len(n[i])
    r = [0]*t
    s = 0
    for i in range(e):
        o = n[i]
        for ii in range(len(o)):
            r[s+ii] = o[ii]
        s += len(o)
    return r

def Sr_enc(n):
    if n < 64:
        return [n << 2]
    else:
        count = int(n / 64)
        e = (n << 2) | 1
        return [(e - (255 * int(e / 256))) - count, count]

def ya(n):
    # tt([Sr.enc(new TextEncoder().encode("https://pronode2.prosopo.io").length), new TextEncoder().encode("https://pronode2.prosopo.io")])
    data1 = [n.get(r, None) for r in ['commitmentId', 'providerUrl', 'dapp', 'user', 'challenge', 'nonce', 'timestamp', 'signature']]
    e = list(data1[1].encode())
    data2 = [1] + tt([Sr_enc(len(e)), e])
    e = list(data1[2].encode())
    data3 = tt([Sr_enc(len(e)), e])
    e = list(data1[3].encode())
    data4 = tt([Sr_enc(len(e)), e])
    e = list(data1[4].encode())
    data5 = [1] + tt([Sr_enc(len(e)), e])
    n = data1[5]
    n = hex(n)[2:]
    nl = []
    while True:
        nl.append(n[-2:].rjust(2,"0"))
        n = n[:-2]
        if n == "":
            break
    while len(nl) != 3:
        nl.append("00")
    nl = [int("0x"+n, 16) for n in nl]
    data6 = [1] + nl + [0]
    e = list(data1[6].encode())
    data7 = tt([Sr_enc(len(e)), e])
    e = list(data1[7]["provider"]["challenge"].encode())
    data8 = [1] + tt([Sr_enc(len(e)), e]) + [0]
    e = list(data1[7]["user"]["timestamp"].encode())
    data8_1 = [1] + tt([Sr_enc(len(e)), e]) + [0]
    data8 = data8 + data8_1
    final = tt([[0], data2, data3, data4, data5, data6, data7, data8])
    return Ye(bytes(final))

# Solver
def solve(sitekey, siteurl, proxy=None):
    s = curl_cffi.Session(impersonate="chrome131")
    s.headers = {
        "user-agent": ua_generator.generate(browser="chrome").text,
        "referer": f"{siteurl.split('://')[0]}://{siteurl.split('/')[2]}/",
        "origin": f"{siteurl.split('://')[0]}://{siteurl.split('/')[2]}"
    }
    if proxy != None:
        s.proxies.update({"https": proxy})
    account = createAccount()
    s.headers.update({
        "Prosopo-Site-Key": sitekey,
        "Prosopo-User": account["address"]
    })
    node = random.randint(2,14)
    r = s.post(f"https://pronode{node}.prosopo.io/v1/prosopo/provider/client/captcha/frictionless", json={
        "token": ne()["token"],
        "dapp": sitekey,
        "user": account["address"]
    })
    if "captchaType" not in r.json():
        return "Failed"
    if r.json()["captchaType"] != "pow":
        return "Unsupported CAPTCHA type"
    sessionId = r.json()["sessionId"]
    r = s.post(f"https://pronode{node}.prosopo.io/v1/prosopo/provider/client/captcha/pow", json={
        "user": account["address"],
        "dapp": sitekey,
        "sessionId": sessionId
    })
    c = r.json()
    b = i(c["challenge"], c["difficulty"])
    U = Ye(account["keypair"].sign(c["timestamp"].encode()))
    r = s.post(f"https://pronode{node}.prosopo.io/v1/prosopo/provider/client/pow/solution", json={
        "challenge": c["challenge"],
        "difficulty": c["difficulty"],
        "signature": {
            "user": {
                "timestamp": U
            },
            "provider": {
                "challenge": c["signature"]["provider"]["challenge"]
            }
        },
        "user": account["address"],
        "dapp": sitekey,
        "nonce": b,
        "verifiedTimeout": 120000
    })
    if r.json().get("verified") != True:
        return "Failed"
    return ya({
        "providerUrl": f"https://pronode{node}.prosopo.io",
        "user": account["address"],
        "dapp": sitekey,
        "challenge": c["challenge"],
        "nonce": b,
        "timestamp": c["timestamp"],
        "signature": {
            "provider": {
                "challenge": c["signature"]["provider"]["challenge"]
            },
            "user": {
                "timestamp": U
            }
        }
    })
