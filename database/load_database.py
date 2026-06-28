import subprocess

print("=" * 50)
print("Initializing Database...")
print("=" * 50)

subprocess.run(["python", "database/init_db.py"])

print("\nLoading Master Data...")

subprocess.run(["python", "database/seed_data.py"])

print("\nGenerating Sales Records...")

subprocess.run(["python", "database/seed_sales.py"])

print("\n")
print("=" * 50)
print("DATABASE READY SUCCESSFULLY")
print("=" * 50)