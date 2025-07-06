# Prosopo-Procaptcha
Prosopo Procaptcha Solver / Almost Fully Reverse Engineered (For pow challenge)
# usage
You can get solve Procaptcha (only PoW captcha), or Generate some parameters with this.
```py
import prosopo

# "0x00016c68747470733a2f2f70726f6e6f6465372e70726f736f706f2e69...", "Failed" or "Unsupported CAPTCHA type"
prosopo.solve("5HNC3s77ASNSAL9gFQSMoyYHxP6KHJ54qXjutaSqLmQ81EYL", "https://hamutan86.pythonanywhere.com/captchademo/prosopo", f"http://your.proxy:1000")

# "DQ/eO5qI2zigH6pgY2IiQYVOVO9MEXv3x3x7CvJP..."
prosopo.ns()["token"]
# "5CnpDkV5wyqpsLazTKGabDwfb1fTHJoLmjF65s3qUdTBHFWz"
prosopo.createAccount()["address"]
```
