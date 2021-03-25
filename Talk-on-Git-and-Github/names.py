def count_unique_values_name_with_set(names_list):
    return len(set(names_list))

def count_unique_values(arr):
    return len(set(arr))

if __name__ == "__main__":
    all_names = ["Anish", "Raja", "Magnus", "Magnus"]
    print(count_unique_values(all_names))

