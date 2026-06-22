# Update balance after withdrawal
# Before: balance = 12000
# Withdrawal: 3000
# After: ?

balance=12000
withdrawal=3000
print(f'Before:balance={balance}')
print(f'Withdrawal:withdrawal={withdrawal}')
balance -= withdrawal
print(f'After Withdrawal:balance={balance}')