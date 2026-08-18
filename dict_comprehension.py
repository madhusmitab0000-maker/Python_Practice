items=[("Alice"), ("Bob"), ("Charlie")]
prices=[10, 20, 30]

dict_prices={items[i]:prices[i] for i in range(len(items))}
print(dict_prices)