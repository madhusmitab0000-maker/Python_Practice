names=["Ali","Sara","John"]
cleaned_data=[new_name.strip().lower()for new_name in names if new_name]
print(cleaned_data)