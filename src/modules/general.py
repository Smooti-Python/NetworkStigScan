from colorama import Fore

def display_stig(title: str, vulnId, severity: str, description: str, dashCount: int=120):
	# * Output vuln currently being checked
	# Items to check
	# Title
	# Vuln ID
	# Severity
	# Description

	dash = "-" * dashCount
	titleString = f"{Fore.CYAN}Title:{Fore.BLUE} {title}"
	vulnIdString = f"{Fore.CYAN}Vuln ID:{Fore.MAGENTA} {vulnId}"
	severityString = f"{Fore.CYAN}Severity: {severity}"
	descriptionString = f"{Fore.CYAN}Description:{Fore.WHITE} {description}"
	fullString = f"{dash}\n{titleString}\n{vulnIdString}\n{severityString}\n{descriptionString}\n{dash}\n"

	return fullString

def classify_color(severity: str):
	# Assign color to severity level

	if severity == "high":
		severity = Fore.RED + severity
	elif severity == "medium":
		severity = Fore.YELLOW + severity
	else:
		severity = Fore.GREEN + severity

	return severity