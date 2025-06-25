# python-bypass-https

A Python utility/library to bypass HTTPS SSL certificate verification for HTTP requests. This can be useful for development, testing, or scraping scenarios where you need to interact with HTTPS endpoints that have invalid, self-signed, or expired certificates.

## ⚠️ Disclaimer

**Use at your own risk! Disabling SSL verification can expose you to man-in-the-middle (MITM) attacks. Never use this in production or with sensitive data. Only use for development or testing in a controlled environment.**

## Features

- Easily disable SSL certificate verification for Python HTTP requests.
- Support for popular HTTP libraries: `requests`, `http.client`, `urllib3`, etc.
- Can be used as a script or imported as a module.

## Installation

Clone the repository:

```bash
git clone https://github.com/REVEAL1001/python-bypass-https.git
cd python-bypass-https
```

## Usage

```bash
python3 app.py #Starts a vulnerable server
python3 downgrade.py #Starts a http proxy
```
