def tim_so_fibonacci(n):
    if n <= 1:
        return n
    return tim_so_fibonacci(n-1) + tim_so_fibonacci(n-2)

# Test
n = int(input("Nhập n: "))
print("Fibonacci thứ", n, "là:", tim_so_fibonacci(n))
