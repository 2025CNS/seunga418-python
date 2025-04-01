h, b, c, s = map(int, input().split())
total_bits = h * b * c * s
total_bytes = total_bits / 8
total_kb = total_bytes / 1024
total_mb = total_kb / 1024
print(f"{total_mb:.1f} MB")