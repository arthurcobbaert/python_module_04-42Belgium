def lost_archive() -> None:
	file = "lost_archive.txt"
	print(f"CRISIS ALERT: Attempting access to '{file}'...")
	try:
		with open(file, 'r') as f:
			data = f.read()
			print(f"SUCCESS: Archive recovered - ''{data}''")
		print("STATUS: Normal operations resumed\n")
	except PermissionError:
		print("RESPONSE: Security protocols deny access")
		print("STATUS: Crisis handled, security maintained\n")
	except FileNotFoundError:
		print("RESPONSE: Archive not found in storage matrix")
		print("STATUS: Crisis handled, system stable\n")

def permission_archive() -> None:
	file = "classified_vault.txt"
	print(f"CRISIS ALERT: Attempting access to '{file}'...")
	try:
		with open(file, 'r') as f:
			data = f.read()
			print(f"SUCCESS: Archive recovered - ''{data}''")
		print("STATUS: Normal operations resumed\n")
	except PermissionError:
		print("RESPONSE: Security protocols deny access")
		print("STATUS: Crisis handled, security maintained\n")
	except FileNotFoundError:
		print("REPONSE: Archive not found in storage matrix")
		print("STATUS: Crisis handled, system stable\n")


def standard_archive() -> None:
	file = "standard_archive.txt"
	print(f"ROUTINE ACCESS: Attempting access to '{file}'...")
	try:
		with open(file, 'r') as f:
			data = f.read()
			print(f"SUCCESS: Archive recovered - ''{data}''")
		print("STATUS: Normal operations resumed\n")
	except PermissionError:
		print("RESPONSE: Security protocols deny access")	
		print("STATUS: Crisis handled, security maintained\n")
	except FileNotFoundError:
		print("RESPONSE: Archive not found in storage matrix")
		print("STATUS: Crisis handled, system stable\n")
if __name__ == "__main__":
	print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
	lost_archive()
	permission_archive()
	standard_archive()
	print("All crisis scenarios handled successfully. Archives secure.")
