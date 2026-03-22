from app.services.ai_service import get_crop_recommendation

def recommend_crop(soil_type, location, season, language):
    return get_crop_recommendation(soil_type, location, season, language)