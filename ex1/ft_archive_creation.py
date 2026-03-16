if __name__ == "__main__":
	file_name = "new_discovery.txt"
	print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
	with open(file_name, "w") as f:
		print(f"Initializing new storage unit: {file_name}")
		print("Storage unit created successfully...\n")
		print("Inscribing preservation data...")
		f.write("[ENTRY 001] New quantum algorithm discovered\n")
		f.write("[ENTRY 002] Efficiency increased by 347%\n")
		f.write("[ENTRY 003] Archived by Data Archivist trainee\n")
	with open(file_name, "r") as r:
		print(r.read())
		print("Data inscription complete. Storage unit sealed.")
		print("Archive 'new_discovery.txt' ready for long-term preservation.")
