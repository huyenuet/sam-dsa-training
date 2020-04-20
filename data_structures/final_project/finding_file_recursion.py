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
    if path is None or len(path) == 0:
        return
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
# test case 1
print("test case 1")
test_path = "./testdir"
test_suffix = ".c"
print(find_files(test_suffix, test_path))
print(
    "Expected output: ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', "
    "'./testdir/subdir1/a.c']"
)

# test case 2
print("\ntest case 2")
test_path = "."
print(find_files(test_suffix, test_path))
print(
    "Expected output: ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', "
    "'./testdir/subdir1/a.c']"
)

# test case 3
print("\ntest case 3")
test_path = ""
test_suffix = ""
print(find_files(test_suffix, test_path))
print("Expected output: None")
