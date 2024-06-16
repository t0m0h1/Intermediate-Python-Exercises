import time

start_time = time.time()

for i in range(1, 2_000_000_001):
    if i % 100_000_000 == 0:  # Print progress every 100 million counts
        elapsed_time = time.time() - start_time
        print(f"Reached {i} in {elapsed_time:.2f} seconds")

end_time = time.time()
total_time = end_time - start_time
print(f"Total time to count to 2 billion: {total_time:.2f} seconds")
