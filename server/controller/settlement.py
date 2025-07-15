import secrets
from fastapi import HTTPException

from shared.models.settlement import NewSettlement
from server.databases.config import database
from server.utils.logger import logging

settlement_collection = database.get_settlement_collection()
group_collection = database.get_group_collection()

def make_settlement(group_id: str, info : NewSettlement, current_user):
    try:
        logging.info('Making Settlement')
        if info.group_id != group_id:
            raise HTTPException(status_code=401, detail='Wrong Data')
        
        group = group_collection.find_one({"group_id": group_id})
        if not group:
            raise HTTPException(status_code=404, detail="Group not found")
        if current_user['user_name'] not in group.get('members', []):
            raise HTTPException(status_code=403, detail="Not the member of group")
        if current_user['user_name'] != info.paid_by or current_user['user_name']!=info.paid_to:
            raise HTTPException(status_code=403, detail='You are not the part of this transaction')

        info.settlement_id = create_unique_settlement_id()

        balances = group.get('member_balances', [])
        balances[info.paid_by] += info.amount
        balances[info.paid_to] -= info.amount

        res = settlement_collection.insert_one(info.model_dump())

        group_collection.update_one(
            {"group_id": group_id},
            {"$set": {"member_balances": balances}}
        )

        logging.info(f'Settlement done')
        return {
            "status_code": 200,
            "message": f"Successfully settled amount {info.amount}",
        }

    except HTTPException as he:
        logging.error(f'Error {str(he)}')
        raise he
    except Exception as e:
        print(e)
        logging.error(f'Failed to make group, {e}')
        raise HTTPException(status_code=500, detail=str(e))




def create_unique_settlement_id():
    i = 0
    while i<100:
        id = secrets.token_hex(4)
        exists = settlement_collection.find_one({"settlement_id": id})
        if not exists:
            return id
        i+=1
    logging.error('Failed to generate unique group ID after 100 attempts')
    raise HTTPException(
        status_code=500,
        detail='Failed to generate unique group ID'
    )
