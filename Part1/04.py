str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str_arr = str.split(" ")

print [{i: str_arr[i-1][0] if i in {1, 5, 6, 7, 8, 9, 15, 16, 19} else str_arr[i-1][:2]} for i in range(1,len(str_arr)+1)]
