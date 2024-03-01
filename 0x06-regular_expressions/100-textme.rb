import re

def parse_transaction(transaction_text):
    
    pattern = re.compile(r'(?P<sender>[\w\s\+\(\)]+),(?P<receiver>[\w\s\+\(\)]+),(?P<flags>[\w,]+)')

    
    match = pattern.match(transaction_text)

    if match:
        
        sender = match.group('sender')
        receiver = match.group('receiver')
        flags = match.group('flags')

        
        print(f"{sender},{receiver},{flags}")
    else:
        print("Invalid transaction format")

transaction_text = "Raissa MUGENI,+250798979591,Ny"
parse_transaction(transaction_text)

