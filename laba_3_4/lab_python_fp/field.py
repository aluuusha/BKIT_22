def field(arrset, *args):
    assert len(args) > 0
    result = []
    for seti in arrset:
        args_in_seti = [arg for arg in args if arg in seti]
        result.append({arg: seti[arg] for arg in args_in_seti} if len(args) > 1 else seti[args_in_seti[0]] if len(args_in_seti) > 0 else None)
    while None in result:
        result.remove(None)
    while {} in result:
        result.remove({})
    return result
    
if __name__ == "__main__":
    workers = [
        {'name': 'Иван', 'surname': 'Иванов', 'age': 25, 'position': 'водитель'},
        {'name': 'Петр', 'surname': 'Петров', 'age': 35, 'position': 'инженер'},
        {'name': 'Алексей', 'surname': 'Алексеев', 'age': 18, 'position': 'стажер'},
    ]
    print(field(workers, 'age'))
    print(field(workers, 'name'))
    print(field(workers, 'name', 'position'))
    print(field(workers, 0, 2))
    print(field(workers, 0))    