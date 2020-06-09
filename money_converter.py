ty_gia_paypal = 22.72322
ty_gia_bank = 23.44550
fix_salary = 582


def count_diff(salary):
    diff_vnd = ty_gia_bank - ty_gia_paypal
    diff_usd = diff_vnd / ty_gia_bank
    return salary * diff_usd


def calculate_salary_from_diff(diff):
    diff_vnd = ty_gia_bank - ty_gia_paypal
    diff_usd = diff_vnd / ty_gia_bank
    return diff/diff_usd


print(count_diff(fix_salary))
print("total usd salary: ", fix_salary+count_diff(fix_salary))
print(calculate_salary_from_diff(22))
