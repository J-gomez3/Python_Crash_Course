current_users=['jaden', 'yonatan', 'jose', 'raul', 'kio']
new_users=['KIO', 'marcos', 'jose','jonathan', 'estefanio']
new_userss=[x.lower() for x in new_users]
for new_user in new_userss:
	if new_user in current_users:
		print(f"{new_user} already been taken")
	else:
		print(f"welcome {new_user}")

