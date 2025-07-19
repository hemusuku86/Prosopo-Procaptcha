# Procaptcha
Prosopo Procaptcha Solver / Almost Fully Reverse Engineered (For pow challenge)
# 📘 Usage
You can solve Procaptcha (only PoW captcha), or Generate some parameters with this.
```py
import prosopo

# "0x00016c68747470733a2f2f70726f6e6f6465372e70726f736f706f2e69...", "Failed" or "Unsupported CAPTCHA type"
prosopo.solve("5HNC3s77ASNSAL9gFQSMoyYHxP6KHJ54qXjutaSqLmQ81EYL", "https://hamutan86.pythonanywhere.com/captchademo/prosopo", f"http://your.proxy:1000")

# "DQ/eO5qI2zigH6pgY2IiQYVOVO9MEXv3x3x7CvJP..."
prosopo.ns()["token"]
# "5CnpDkV5wyqpsLazTKGabDwfb1fTHJoLmjF65s3qUdTBHFWz"
prosopo.createAccount()["address"]
```
# 🖼️ Showcase
![Screenshot](https://github.com/hemusuku86/prosopo-procaptcha/blob/main/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202025-07-06%20190919.png?raw=true)
