from datetime import date
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .app.models import PredictionResponse, PredictionRequest
from .app.views import get_prediction


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static", check_dir=False), name="static")

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/prediction')
async def make_model_prediction(request:Request):
    form = await request.form()
    brand_name = form.get("brand_name")
    model_name = form.get("model_name")
    motor_size = float(form.get("motor_size"))
    years = date.today().year - int(form.get("model_year"))
    kms_driven = float(form.get("kms_driven"))
    mileage = float(form.get("mileage"))
    owner = int(form.get("owner"))
    power = float(form.get("power"))

    features = {
        "brand_name": brand_name,
        "model_name": model_name,
        "motor_size": motor_size,
        "years": years,
        "kms_driven": kms_driven,
        "mileage": mileage,
        "owner": owner,
        "power": power
    }
    

    output = PredictionResponse(price=get_prediction(features))
    return templates.TemplateResponse("index.html", {"request": request, "prediction_text": output})
    
