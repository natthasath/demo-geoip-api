from fastapi import APIRouter, Depends, Form
from fastapi.responses import JSONResponse
from app.models.model_geoip import GeoipSchema
from app.services.service_geoip import GeoipService

router = APIRouter(
    prefix="/geoip",
    tags=["GEOIP"],
    responses={404: {"message": "Not found"}}
)

@router.get("/get_ip")
async def get_ip():
    return GeoipService().get_ip()

@router.post("/get_location")
async def get_location(data: GeoipSchema = Depends(GeoipSchema)):
    return GeoipService().get_location(data.ip_address)