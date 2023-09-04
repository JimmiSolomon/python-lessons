def normalize_url(site):
	if site[:8] == 'https://':
		return site
	elif site[:7] == 'http://':
		return 'https://' + site[7:]
	else:
		return 'https://' + site
