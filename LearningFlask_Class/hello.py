from flask import Flask
from primeNumbers import prime

app = Flask(__name__)


@app.route('/')
def hundred_primes():
    primN = prime()
    return str(primN.get_primes(100))
    return "hello"
if __name__ == "__main__":
    app.run(debug=True)
