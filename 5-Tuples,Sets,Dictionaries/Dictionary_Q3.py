test_list = ["DataScience", 3, "is", 8]
key_list = ["name", "id"]
result = [dict(zip(key_list, test_list[i:i+len(key_list)])) for i in range(0, len(test_list), len(key_list))]
print(result)
