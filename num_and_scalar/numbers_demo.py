
from decimal import Decimal

# Gives error because float is a binary representation
print(float(0.8) - float(0.7))

# Decimal supports floating point repr. Also has the same issue
print(Decimal(0.8) - Decimal(0.7))

# When called with string literal constructors, Decimal gives correct results
print(Decimal('0.8') - Decimal('0.7'))
