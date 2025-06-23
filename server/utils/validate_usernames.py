from fastapi import HTTPException
from server.databases.config import database

user_collection = database.get_user_collection()

def validate_usernames(usernames: list[str]) -> list[str]:
    """
    Given a list of usernames, validate which ones exist.
    Return only the valid ones. Raise error if none are valid.
    """
    if not usernames:
        raise HTTPException(status_code=400, detail="Usernames list cannot be empty.")

    valid_usernames = []
    for username in usernames:
        print(f"Here : {username}")
        user = user_collection.find_one({"user_name": username})
        if user:
            valid_usernames.append(username)

    if not valid_usernames:
        raise HTTPException(status_code=404, detail="None of the usernames are valid.")

    return valid_usernames
