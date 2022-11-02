from fastapi import FastAPI, HTTPException, APIRouter
from ..models.dmv_db import DataBase

router = APIRouter()


@router.get("/guardian/")
def get_guardian_data(guardian_id: str, tier: int, astral: int = 0):

    guardian_info = DataBase()
    try:
        guardian_info.get_data(guardian_id, tier, astral)
        data = {
            "name": guardian_info.name,
            "id": guardian_info.code_name,
            "catchline": guardian_info.catchline,
            "type": guardian_info.type,
            "rarity": tier,
            "astral_rating": guardian_info.astral,
            "img_url": guardian_info.img_url,
            "health": guardian_info.health,
            "attack": guardian_info.attack,
            "defense": guardian_info.defense,
            "focus": guardian_info.focus,
            "abilities": guardian_info.abilities,
            "talents": guardian_info.talents,
        }
        data.update({"status": 200, "detail": "Successful"})
        return data
    except:
        raise HTTPException(status_code=404, detail=guardian_info.error)
