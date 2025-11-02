import string
import secrets

def generate_uid(used_uids):
    for _ in range(100):
        new_uid = ""
        for _ in range(8):
            new_uid += secrets.choice(string.digits)
        
        if new_uid not in used_uids:
            used_uids.append(new_uid)
            return new_uid