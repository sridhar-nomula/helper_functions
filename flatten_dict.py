
def flatten_dict(d, parent_key='', sep='_'):
    """
    Recursively flattens a nested dictionary.
    """
    items = []
    for k, v in d.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                nested_key = f'{new_key}{sep}{i}'
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, nested_key, sep=sep).items())
                else:
                    items.append((nested_key, item))
        else:
            items.append((new_key, v))
    return dict(items)

flattend_file = [flatten_dict(d) for d in pr_list]
df = pd.DataFrame(flattend_file)
