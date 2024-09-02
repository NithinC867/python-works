email_id="john@gmail.com"

index=email_id.index("@")

username=email_id[:index]
domain=email_id[index:]

print(f"username:{username},domain:{domain}")