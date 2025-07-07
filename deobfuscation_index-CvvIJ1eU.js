async function mx(...n) {
  n["length"] = 1;
  n.goQwR8Y = -12;
  // n["olIpuh"] = atob(e(262) + e(263) + e["apply"]("undefined", [264]) + "=")["replace"]("-----BEGIN PUBLIC KEY-----", "")["replace"]("-----END PUBLIC KEY-----", "")["replace"](/[\n\r]/g, "");
  n["olIpuh"] = atob("-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtJjBk4884quOzXZYCnD/\ndXKAqPUkwtb76WtbG0rM5s2p2htyFT9Zo3PR/BT87OExVDfAy0iN1e2HGEQWsLAM\n8QZ7xWnG1zYolsARNhHAwv/IXsH1zUZmkujTaBpb8S4IHDHAjZLm7i4Qhr7lk/0n\nSJ+Oh2NtCkbKfjlsyoxMoN4IdE4u6T8cSn+AXwZ3F7Bk+NlkmzGMQHYeobD5Mstv\ncDsbwPCJstdnESnTxCiUSrS9SYCgxaxMB8TbmcVx5NImz0HbPZmj/nnpHJOIUR+T\nekMdw3FfZqAyAC4ARXlyWxZbOm0rF4B98HtXwVqfzcQmN9AzJBLW+p3/PXjvZECx\nZwIDAQAB\n-----END PUBLIC KEY-----\n")["replace"]("-----BEGIN PUBLIC KEY-----", "")["replace"]("-----END PUBLIC KEY-----", "")["replace"](/[\n\r]/g, "");
  n["uu00tb"] = n[3];
  n[2] = atob(n["olIpuh"]);
  n.uu00tb = new Uint8Array(n[2].length);
  n[52] = n.olIpuh;
  for (let a = 0; a < n[2]["length"] && w.WJiG_S(); a++) {
    n["uu00tb"][a] = n[2]["charCodeAt"](a);
  }
  n.z9sVTo = await window.Crypto["subtle"]["importKey"](e(n.goQwR8Y + 286), n.uu00tb, {
    name: "RSA-OAEP",
    hash: "SHA-256"
  }, F(1, B(-(n["goQwR8Y"] - (n["goQwR8Y"] - 29)))), [e(279)]);
  n["rLrD4v"] = new TextEncoder().encode(n[0]);
  n.TI7kHGD = await window.crypto.subtle.encrypt({
    name: "RSA-OAEP"
  }, n.z9sVTo, n["rLrD4v"]);
  return n["goQwR8Y"] > 94 ? n[n.goQwR8Y + 247] : ($ = [n.TI7kHGD], P(e(280)));
}
const xe = n => {
  const a = Date["now"]();
  const s = F((Number(("" + a).slice(F(3, 13))) + n) / 999 * Math.PI, Math.PI / 2, 61);
  const t = F(Math.sin(s), 1e3, D = -42);
  return [a, t];
};
const ne = async (...n) => {
  n.length = 0;
  n.XlcnSj = n.GzYp5t;
  const a = await X0();
  const s = F(Math.random(), 0.3, -42);
  const t = Math.min(F(a.reduce((l, d) => l + d, 0), s, D = -21), 1);
  n[62] = -134;
  n["XlcnSj"] = undefined;
  n.Qu66nyo = -80;
  try {
    n.XlcnSj = await mx(c(-998).stringify(xe(t)));
  } catch {
    n.XlcnSj = "";
  }
  return n[62] > -72 ? n[-195] : {
    token: n["XlcnSj"]
  };
};
