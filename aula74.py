def hello(msg, nome):
    
    def send_hello():
        return f'{msg}, {nome}'
    
    return send_hello

msg = hello('hello', 'gay')

print(msg())