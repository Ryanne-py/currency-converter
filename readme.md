# Descriptsin
Module for parsing of the site currency converter https://minfin.com.ua
# Start instructions
Installing module

    git clone https://github.com/Ryanne-py/currency-converter.git
  
Creating a venv

    python -m venv venv

Activate in a venv:

windows

    venv/Scripts/activate
another os

    source venv/bin/activate
Install packages

    pip install -r requirements.txt
In folder ./currency-converter/

    python many_convert.py
# Docs
    from many_convert.py import conversione
    
Docs in funk conversione

    """
    input:(str(start_currency), int(quantity), str(end_currency))
    output:final quantity
    """
    
Simple example

    result = conversion('USD', 900, 'UAH') # result: 35 685
