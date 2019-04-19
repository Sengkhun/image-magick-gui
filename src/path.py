def regex_path(path):
    new_path = path.replace(' ', '\ ')
    new_path = new_path.replace('(', '\(')
    new_path = new_path.replace(')', '\)')
    return new_path