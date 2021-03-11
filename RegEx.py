
import re
n = 2
r =[]
for i in range(n):
    card = input()
    if len(card) == 19:
        if re.findall('^[456]...-....-....-....',card):
            if re.findall('[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$',card):
                card = card + ' Valid'
                r.append(card)
            else:
                card = card + ' Invalid'
                r.append(card)
        else:
            card = card + ' Invalid'
            r.append(card)
    else:
        card = card + ' Invalid'
        r.append(card)

r[0:2]