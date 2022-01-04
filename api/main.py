from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
#from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .app.models import PredictionResponse, PredictionRequest
from .app.views import get_prediction

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post('/v1/prediction')
def make_model_prediction(request: PredictionRequest):
    brand_name = request.form['Brand_name']
    if(brand_name == "Bajaj"):
        PredictionRequest.BrandName.Bajaj = 1    
    elif(brand_name == "Royal Enfield"):
        PredictionRequest.BrandName.Royal_Enfield = 1    
    elif(brand_name == "Hyosung"):
        PredictionRequest.BrandName.Hyosung = 1
    elif(brand_name == "Jawa"):
        PredictionRequest.BrandName.Jawa = 1
    elif(brand_name == "KTM"):
        PredictionRequest.BrandName.KTM = 1        
    elif(brand_name == "TVS"):
        PredictionRequest.BrandName.TVS = 1
    elif(brand_name == "Yamaha"):
        PredictionRequest.BrandName.Yamaha = 1
    elif(brand_name == "Honda"):
        PredictionRequest.BrandName.Honda = 1
    elif(brand_name == "Hero"):
        PredictionRequest.BrandName.Hero = 1
    elif(brand_name == "Suzuki"):
        PredictionRequest.BrandName.Suzuki = 1
    elif(brand_name == "Husqvarna"):
        PredictionRequest.BrandName.Husqvarna = 1
    elif(brand_name == "Mahindra"):
        PredictionRequest.BrandName.Mahindra = 1 
    elif(brand_name == "Kawasaki"):
        PredictionRequest.BrandName.Kawasaki = 1
    elif(brand_name == "Benelli"):
        PredictionRequest.BrandName.Benelli = 1
    elif(brand_name == "Harley Davidson"):
        PredictionRequest.BrandName.Harley_Davidson = 1
    elif(brand_name == "Triumph"):
        PredictionRequest.BrandName.Triumph = 1
    elif(brand_name == "Ducati"):
        PredictionRequest.BrandName.Ducati = 1
    elif(brand_name == "BMW"):
        PredictionRequest.BrandName.BMW = 1

    model_name = request.form['Model_name']
    if(model_name == "Pulsar"):
        PredictionRequest.Pulsar= 1
    elif(model_name == "Classic"):
        PredictionRequest.Classic= 1
    elif(model_name == "Thunderbird"):
        PredictionRequest.Thunderbird= 1
    elif(model_name == "Apache"):
        PredictionRequest.Apache= 1
    elif(model_name == "Avenger"):
        PredictionRequest.Avenger= 1
    elif(model_name == "CB"):
        PredictionRequest.CB= 1
    elif(model_name == "Bullet"):
        PredictionRequest.Bullet= 1
    elif(model_name == "YZF-R15"):
        PredictionRequest.YZF_R15= 1
    elif(model_name == "Duke"):
        PredictionRequest.Duke= 1
    elif(model_name == "RC"):
        PredictionRequest.RC= 1
    elif(model_name == "Discover"):
        PredictionRequest.Discover= 1
    elif(model_name == "Passion"):
        PredictionRequest.Passion= 1
    elif(model_name == "Gixxer"):
        PredictionRequest.Gixxer= 1
    elif(model_name == "Splendor"):
        PredictionRequest.Splendor= 1
    elif(model_name == "Dominar"):
        PredictionRequest.Dominar= 1
    elif(model_name == "V15"):
        PredictionRequest.V15= 1
    elif(model_name == "Street"):
        PredictionRequest.Street= 1
    elif(model_name == "FZ"):
        PredictionRequest.FZ= 1
    elif(model_name == "CBR"):
        PredictionRequest.CBR= 1
    elif(model_name == "FZs"):
        PredictionRequest.FZs= 1
    elif(model_name == "Standard"):
        PredictionRequest.Standard= 1
    elif(model_name == "Platina"):
        PredictionRequest.Platina= 1
    elif(model_name == "Himalayan"):
        PredictionRequest.Himalayan= 1
    elif(model_name == "Karizma"):
        PredictionRequest.Karizma= 1
    elif(model_name == "Xtreme"):
        PredictionRequest.Xtreme= 1
    elif(model_name == "Fazer"):
        PredictionRequest.Fazer= 1
    elif(model_name == "Intruder"):
        PredictionRequest.Intruder= 1
    elif(model_name == "HF"):
        PredictionRequest.HF= 1
    elif(model_name == "Glamour"):
        PredictionRequest.Glamour= 1
    elif(model_name == "FZ25"):
        PredictionRequest.FZ25= 1
    elif(model_name == "CT"):
        PredictionRequest.CT= 1
    elif(model_name == "CBZ"):
        PredictionRequest.CBZ= 1
    elif(model_name == "TNT"):
        PredictionRequest.TNT= 1
    elif(model_name == "FZ16"):
        PredictionRequest.FZ16= 1
    elif(model_name == "Super"):
        PredictionRequest.Super= 1
    elif(model_name == "Electra"):
        PredictionRequest.Electra= 1
    elif(model_name == "Ninja"):
        PredictionRequest.Ninja= 1
    elif(model_name == "CD"):
        PredictionRequest.CD= 1
    elif(model_name == "CBF"):
        PredictionRequest.CBF= 1
    elif(model_name == "Continental"):
        PredictionRequest.Continental= 1
    elif(model_name == "Dream"):
        PredictionRequest.Dream= 1
    elif(model_name == "Hunk"):
        PredictionRequest.Hunk= 1
    elif(model_name == "Forty"):
        PredictionRequest.Forty= 1
    elif(model_name == "FZS"):
        PredictionRequest.FZS= 1
    elif(model_name == "Star"):
        PredictionRequest.Star= 1
    elif(model_name == "Interceptor"):
        PredictionRequest.Interceptor= 1
    elif(model_name == "GT250R"):
        PredictionRequest.GT250R= 1
    elif(model_name == "Ignitor"):
        PredictionRequest.Ignitor= 1
    elif(model_name == "V12"):
        PredictionRequest.V12= 1
    elif(model_name == "Centuro"):
        PredictionRequest.Centuro= 1
    elif(model_name == "Livo"):
        PredictionRequest.Livo= 1
    elif(model_name == "Sport"):
        PredictionRequest.Sport= 1
    elif(model_name == "FZS-FI"):
        PredictionRequest.FZS_FI= 1
    elif(model_name == "Aquila"):
        PredictionRequest.Aquila= 1
    elif(model_name == "MT-15"):
        PredictionRequest.MT_15= 1
    elif(model_name == "Xpulse"):
        PredictionRequest.Xpulse= 1
    elif(model_name == "Iron"):
        PredictionRequest.Iron= 1
    elif(model_name == "Z650"):
        PredictionRequest.Z650= 1
    elif(model_name == "YZF-R3"):
        PredictionRequest.YZF_R3= 1
    elif(model_name == "Victor"):
        PredictionRequest.Victor= 1
    elif(model_name == "Radeon"):
        PredictionRequest.Radeon= 1
    elif(model_name == "SZR"):
        PredictionRequest.SZR= 1
    elif(model_name == "Perak"):
        PredictionRequest.Perak= 1
    elif(model_name == "GT650R"):
        PredictionRequest.GT650R= 1
    elif(model_name == "302R"):
        PredictionRequest.tres302R= 1
    elif(model_name == "Monster"):
        PredictionRequest.Monster= 1
    elif(model_name == "Mojo"):
        PredictionRequest.Mojo= 1
    elif(model_name == "X-Blade"):
        PredictionRequest.X_Blade= 1
    elif(model_name == "Bonneville"):
        PredictionRequest.Bonneville= 1
    elif(model_name == "G"):
        PredictionRequest.G= 1
    elif(model_name == "Achiever"):
        PredictionRequest.Achiever= 1
    elif(model_name == "SP125"):
        PredictionRequest.SP125= 1
    elif(model_name == "Machismo"):
        PredictionRequest.Machismo= 1
    elif(model_name == "Honda"):
        PredictionRequest.Honda= 1
    elif(model_name == "Meteor"):
        PredictionRequest.Meteor= 1
    elif(model_name == "FZ-FI"):
        PredictionRequest.FZ_FI= 1
    elif(model_name == "Slingshot"):
        PredictionRequest.Slingshot= 1
    elif(model_name == "SZ-RR"):
        PredictionRequest.SZ_RR= 1
    elif(model_name == "Svartpilen"):
        PredictionRequest.Svartpilen= 1
    elif(model_name == "XCD"):
        PredictionRequest.XCD= 1
    elif(model_name == "Hness"):
        PredictionRequest.Hness= 1
    elif(model_name == "ER-6n"):
        PredictionRequest.ER_6n= 1
    elif(model_name == "Imperiale"):
        PredictionRequest.Imperiale= 1
    elif(model_name == "Saluto"):
        PredictionRequest.Saluto= 1
    elif(model_name == "SZ"):
        PredictionRequest.SZ= 1
    elif(model_name == "Vitpilen"):
        PredictionRequest.Vitpilen= 1
    elif(model_name == "390"):
        PredictionRequest.tres390= 1
    elif(model_name == "RX135"):
        PredictionRequest.RX135= 1
    elif(model_name == "Z800"):
        PredictionRequest.Z800= 1
    elif(model_name == "Gladiator"):
        PredictionRequest.Gladiator= 1
    elif(model_name == "Z1000"):
        PredictionRequest.Z1000= 1
    elif(model_name == "Tiger"):
        PredictionRequest.Tiger= 1
    elif(model_name == "Hayate"):
        PredictionRequest.Hayate= 1
    elif(model_name == "RX"):
        PredictionRequest.RX= 1
    elif(model_name == "1200"):
        PredictionRequest.mil1200= 1
    elif(model_name == "Panigale"):
        PredictionRequest.Panigale= 1
    elif(model_name == "GSX-R"):
        PredictionRequest.GSX_R= 1
    elif(model_name == "Discover150"):
        PredictionRequest.Discover150= 1
    elif(model_name == "Flame"):
        PredictionRequest.Flame= 1
    elif(model_name == "Leoncino"):
        PredictionRequest.Leoncino= 1
    elif(model_name == "Fazer25"):
        PredictionRequest.Fazer25= 1
    elif(model_name == "CB300R"):
        PredictionRequest.CB300R= 1
    elif(model_name == "Crux"):
        PredictionRequest.Crux= 1
    elif(model_name == "New"):
        PredictionRequest.New= 1
    elif(model_name == "CBR1000RR"):
        PredictionRequest.CBR1000RR= 1
    elif(model_name == "Boxer"):
        PredictionRequest.Boxer= 1
    elif(model_name == "SS"):
        PredictionRequest.SS= 1
    elif(model_name == "4S"):
        PredictionRequest.cuatro4S= 1
    elif(model_name == "CT110"):
        PredictionRequest.CT110= 1
    elif(model_name == "Z900"):
        PredictionRequest.Z900= 1
    elif(model_name == "SZX"):
        PredictionRequest.SZX= 1
    elif(model_name == "YZFR15"):
        PredictionRequest.YZFR15= 1
    elif(model_name == "S"):
        PredictionRequest.S= 1
    elif(model_name == "CD110"):
        PredictionRequest.CD110= 1
    elif(model_name == "MAX"):
        PredictionRequest.MAX= 1
    elif(model_name == "Speed"):
        PredictionRequest.Speed= 1
    elif(model_name == "Thruxton"):
        PredictionRequest.Thruxton= 1
    elif(model_name == "Multistrada"):
        PredictionRequest.Multistrada= 1
    elif(model_name == "FZS25"):
        PredictionRequest.FZS25= 1
    elif(model_name == "Z250"):
        PredictionRequest.Z250= 1
    elif(model_name == "Phoenix"):
        PredictionRequest.Phoenix= 1
    elif(model_name == "XDiavel"):
        PredictionRequest.XDiavel= 1
    elif(model_name == "Impulse"):
        PredictionRequest.Impulse= 1
    elif(model_name == "Inazuma"):
        PredictionRequest.Inazuma= 1
    elif(model_name == "Discover150S"):
        PredictionRequest.Discover150S= 1
    elif(model_name == "Sportster"):
        PredictionRequest.Sportster= 1
    elif(model_name == "CBR650F"):
        PredictionRequest.CBR650F= 1
    elif(model_name == "Fiero"):
        PredictionRequest.Fiero= 1
    elif(model_name == "GT"):
        PredictionRequest.GT= 1
    elif(model_name == "Scrambler"):
        PredictionRequest.Scrambler= 1
    elif(model_name == "Vulcan"):
        PredictionRequest.Vulcan= 1
    elif(model_name == "VT1300CX"):
        PredictionRequest.VT1300CX= 1
    elif(model_name == "YZF-R1M"):
        PredictionRequest.YZF_R1M= 1
    elif(model_name == "XG750"):
        PredictionRequest.XG750= 1
    elif(model_name == "YBR"):
        PredictionRequest.YBR= 1
    elif(model_name == "GS"):
        PredictionRequest.GS= 1
    elif(model_name == "TRK"):
        PredictionRequest.TRK= 1
    elif(model_name == 'GSX-S750'):
        PredictionRequest.GSX_S750=1



    return PredictionResponse(price=get_prediction(request))

