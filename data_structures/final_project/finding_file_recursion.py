import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    path_ls = list()
    sub_dirs = os.listdir(path=path)
    for sub_dir in sub_dirs:
        sub_path = os.path.join(path, sub_dir)
        if os.path.isfile(sub_path) and sub_dir.endswith(suffix):
            path_ls.append(sub_path)
        if os.path.isdir(sub_path):
            output = find_files(suffix, sub_path)
            path_ls += output

    return path_ls


# test the method find_files
test_path = "./testdir"
test_suffix = ".c"
print(find_files(test_suffix, test_path))
