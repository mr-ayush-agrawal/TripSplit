import secrets
from server.models.group import NewGroup, AddMembersRequest, GroupData
from fastapi import HTTPException

from server.utils.logger import logging
from server.utils.validate_usernames import validate_usernames
from server.utils.simplify_debts import simplify_debts

from server.databases.config import database
group_collection = database.get_group_collection()

def create_group(group: NewGroup, creator: str): 
    try:
        logging.info('Creating new group')
        group_id = create_unique_group_id()
        group_data = group.model_dump()
        group_data['group_id'] = group_id
        group_data['owner_username'] = creator['user_name']
        group_data['members'] = [creator['user_name']]  # Add creator as the first member

        group_collection.insert_one(group_data)
        logging.info(f'Group created successfully: {group_data}')
        return {
            'status_code': 201,
            'message': 'Group created successfully',
            'group_id': group_id
        }
    
    except HTTPException as he:
        logging.error(f'Error {str(he)}')
        raise he
    except Exception as e:
        logging.error(f'Failed to make group, {e}')
        raise HTTPException(status_code=500, detail=str(e))

def add_member(group_id: str, member_list: AddMembersRequest, current_user: str):
    try:
        group = group_collection.find_one({"group_id": group_id})
        if not group:
            raise HTTPException(status_code=404, detail="Group not found")
        if group['owner_username'] != current_user['user_name']:
            raise HTTPException(status_code=403, detail="Only the group owner can add members")
        

        logging.info(f'Adding members to the group {group_id}')

        member_list = validate_usernames(member_list.usernames)
        if not member_list:
            raise HTTPException(status_code=400, detail="No valid usernames provided")

        existing_members = group.get('members', [])
        new_members = list(set(existing_members + member_list))

        group_collection.update_one(
            {"group_id": group_id},
            {"$set": {"members": new_members}}
        )

        # TO add the group to the users list of groups
        # for username in valid_usernames:
        #     user_collection.update_one(
        #         {"user_name": username},
        #         {"$addToSet": {"groups": data.group_id}}  # prevents duplicates
        #     )

        logging.info(f'Members added to group {group_id}: {member_list}')
        return {
            "status_code": 200,
            "message": f"Successfully added {len(member_list)} members to the group",
            "members_added": member_list
        }

    except HTTPException as he:
        logging.error(f'Error {str(he)}')
        raise he
    except Exception as e:
        logging.error(f'Failed to add members to group {group_id}, {e}')
        raise HTTPException(status_code=500, detail=str(e))
   
def remove_member(group_id: str, username: str, current_user: str):
    try : 
        logging.info(f'Removing member {username} from group {group_id}')
        group = group_collection.find_one({"group_id": group_id})
        if not group:
            raise HTTPException(status_code=404, detail="Group not found")
        if group['owner_username'] != current_user['user_name']:
            raise HTTPException(status_code=403, detail="Only the group owner can remove members")
        if username not in group.get("members", []):
            raise HTTPException(status_code=404, detail="User is not a member of the group")
        if username == group['owner_username']:
            other_members = [m for m in group['members'] if m != username]
            if other_members:
                raise HTTPException(
                    status_code=400,
                    detail="Cannot remove the group owner until all other members are removed."
                )
        
        balances = group.get("member_balances", {})
        user_balance = balances.get(username, 0.0)

        if round(user_balance, 2) != 0.0: 
            raise HTTPException(status_code=400, detail=f"Cannot remove {username}. Balance is not zero (currently {user_balance}).")

        group_collection.update_one(
            {"group_id": group_id},
            {
                "$pull": {"members": username},
                "$unset": {f"member_balances.{username}": ""}  # Remove the balance entry
            }
        )
        logging.info(f"User {username} removed from group {group_id}")
        return {
            "status_code": 200,
            "data" : {
                "group_id": group_id,
                "username": username
            },
            "message": f"{username} successfully removed from the group"
        }

    except HTTPException as he:
        logging.error(f'Error {str(he)}')
        raise he
    except Exception as e:
        logging.error(f'Failed to remove member {username} from group {group_id}, {e}')
        raise HTTPException(status_code=500, detail=str(e))

def get_all_groups(current_user: str):
    try : 
        username = current_user['user_name']
        groups_list = group_collection.find({"members": username})

        user_groups = []
        for group in groups_list:
            group_id = group.get("group_id")
            group_name = group.get("group_name", "Unnamed Group")
            balances = group.get("member_balances", {})
            user_balance = round(balances.get(username, 0.0), 2) 

            user_groups.append({
                "group_id": group_id,
                "name": group_name,
                "balance": user_balance
            })
        return{
            "status_code" : 200,
            "user_groups" : user_groups
        }
    
    except HTTPException as he:
        logging.error(f'Error {str(he)}')
        raise he
    except Exception as e:
        logging.error(f'Failed to get the groups of  {username}, {e}')
        raise HTTPException(status_code=500, detail=str(e))

def group_by_id(group_id: str, current_user: str):
    try : 
        username = current_user['user_name']
        group = group_collection.find_one({"group_id": group_id})
        logging.info(f'Fetching the group info of {group_id}')

        if not group:
            raise HTTPException(status_code=404, detail="Group not found")

        if username not in group.get("members", []) and username != group.get("owner_username"):
            raise HTTPException(status_code=403, detail="You are not a member of this group")

        group.pop('_id', None)

        logging.info(f'{group_id} group info fetched')
        return {
            'status_code' : 200,
            'data' : GroupData(**group)
        }
    
    except HTTPException as he:
        logging.error(f'Error {str(he)}')
        raise he
    except Exception as e: 
        logging.error(f'Failed to get the group info of {group_id}, {e}')
        raise HTTPException(status_code = 500, detail = str(e))

def simplify(group_id:str, current_user: dict):
    try :
        username = current_user['user_name']
        group = group_collection.find_one({"group_id": group_id})
        logging.info(f'Simplifying Debts for group : {group_id}')

        if not group:
            raise HTTPException(status_code=404, detail="Group not found")

        if username not in group.get("members", []) and username != group.get("owner_username"):
            raise HTTPException(status_code=403, detail="You are not a member of this group")
        
        member_balances = group.get("member_balances", {})
        payments : dict[str, list[tuple[str, float]]] =  simplify_debts(member_balances)

        return {
            'status_code' : 200,
            'description' : 'user1 : [user2 : amt] \n User1 pays amt to user2',
            'base_currency': group.get("base_currency", "INR"),
            'data' : payments
        }
    
    except HTTPException as he:
        logging.error(f'Error {str(he)}')
        raise he
    except Exception as e: 
        logging.error(f'Failed to get the group info of {group_id}, {e}')
        raise HTTPException(status_code = 500, detail = str(e))


def create_unique_group_id():
    i = 0
    while i<100:
        group_id = secrets.token_hex(3)
        exists = group_collection.find_one({"group_id": group_id})
        if not exists:
            return group_id
        i+=1
    logging.error('Failed to generate unique group ID after 100 attempts')
    raise HTTPException(
        status_code=500,
        detail='Failed to generate unique group ID'
    )
    