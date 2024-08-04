def input_uni(uni_num):
    print(f"---------Enter data for University {uni_num+1}-------------:")
    num_can = int(input("Enter the number of candidates:"))
    # Collect candidate names
    cand_names = [input(f"Enter the name of candidate {i+1}: ") for i in range(num_can)]
    # Collect performance indices
    old_range = list(map(float, input("Enter the list for current performance Index (space-separated): ").split()))
    new_range = list(map(float, input("Enter the list for new performance Index (space-separated): ").split()))
    # Collect results
    results = [float(input(f"Enter result for {cand_names[i]}: ")) for i in range(num_can)]
    return old_range, new_range, results, cand_names

def normalize(old_range, new_range, result):
    min_old_range = min(old_range)
    max_old_range = max(old_range)
    min_new_range = min(new_range)
    max_new_range = max(new_range)
    
    # Correct normalization formula
    if max_old_range == min_old_range:
        return min_new_range  # Avoid division by zero
    normalized_value = ((result - min_old_range) / (max_old_range - min_old_range)) * (max_new_range - min_new_range) + min_new_range
    return normalized_value

def output(uni_num):
    old_range, new_range, results, cand_names = input_uni(uni_num)
    output_normalize = []
    for i in range(len(results)):
        v = normalize(old_range, new_range, results[i])
        print(f"{cand_names[i]} --> {v}")
        output_normalize.append(v)

uni_num = int(input("Enter the number of Universities: "))
for i in range(uni_num):
    output(i)
