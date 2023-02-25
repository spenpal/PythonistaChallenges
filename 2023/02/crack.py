next_to = {
    '0': ['8'],
    '1': ['2', '4'],
    '2': ['1', '3', '5'],
    '3': ['2', '6'],
    '4': ['1', '5', '7'],
    '5': ['2', '4', '6', '8'], 
    '6': ['3', '5', '9'],
    '7': ['4', '8'],
    '8': ['0', '5', '7', '9'],
    '9': ['6', '8']
}

def crack(pin: str) -> list[str]:
    if not pin:
        return ['']
    
    all_pins = []
    partial_pins = crack(pin[1:])
    for d in sorted(next_to[pin[0]] + [pin[0]]):
        all_pins += [''.join([d, partial_pin]) for partial_pin in partial_pins]
    return all_pins
    
    
# Tests
print(crack("0"))
print(crack("2"))
print(crack("007"))
print(crack("46"))