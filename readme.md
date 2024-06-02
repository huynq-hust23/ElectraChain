# How to use
## Create new wallet

There are 2 way to create new wallet

First you need to visit solana playground: ![beta.solpg.io](https://beta.solpg.io/)

Then select connect to devnet on bottom left of website
![](tutorial/01.png)

Then you can create an account direct on top right menu
![](tutorial/02.png)

Another way is better but not recommend for noob, you need to download Phantom extension and sign up an account. Then you can create many wallet as you want, but to use this wallet in devnet solana, you need to first connect in solana playground
![](tutorial/03.png)

## How to start server API

First of all you need python > 3.10 and pip

### Windows
```
./install.bat
./run.bat
```

### Linux
```
cd blockchain\client

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python main.py
```

## Account are using for fee payer

you can change fee payer in `blockchain\client\config.py`