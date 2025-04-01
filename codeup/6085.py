w, h, b = map(int, input().split())
storage_size_mb = (w * h * b) / 8 / 1024 / 1024
print(f"{storage_size_mb:.2f} MB")