import sys

has_true_flag = "true" in sys.argv

if has_true_flag:
	print("has true")
else:
	print("does not have true")