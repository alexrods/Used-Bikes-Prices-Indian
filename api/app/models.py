from pydantic import BaseModel

class BrandName(BaseModel):
        Bajaj: int = 0
        Royal_Enfield: int = 0
        Hyosung: int = 0
        Jawa: int = 0
        KTM: int = 0
        TVS: int = 0
        Yamaha: int = 0
        Honda: int = 0
        Hero: int = 0
        Suzuki: int = 0
        Husqvarna: int = 0
        Mahindra: int = 0
        Kawasaki:int = 0
        Benelli: int  = 0
        Harley_Davidson: int = 0
        Triumph: int = 0
        Ducati: int = 0
        BMW: int = 0


class ModelName(BaseModel):    
    Pulsar: int = 0
    Classic: int = 0
    Thunderbird: int = 0
    Apache: int = 0
    Avenger: int = 0
    CB: int = 0
    Bullet: int = 0
    YZF_R15: int = 0
    Duke: int = 0
    RC: int = 0
    Discover: int = 0
    Passion: int = 0
    Gixxer: int = 0
    Splendor: int = 0
    Dominar: int = 0
    V15: int = 0
    Street: int = 0
    FZ: int = 0
    CBR: int = 0
    FZS: int = 0
    Standard: int = 0
    Platina: int = 0
    Himalayan: int = 0
    Karizma: int = 0
    Xtreme: int = 0
    Fazer: int = 0
    Intruder: int = 0
    HF: int = 0
    Glamour: int = 0
    FZ25: int = 0
    CT: int = 0
    CBZ: int = 0
    TNT: int = 0
    FZ16: int = 0
    Super: int = 0
    Electra: int = 0
    Ninja: int = 0
    CD: int = 0
    CBF: int = 0
    Continental: int = 0
    Dream: int = 0
    Hunk: int = 0
    Forty: int = 0
    FZS: int = 0
    Star: int = 0
    Interceptor: int = 0
    GT250R: int = 0
    Ignitor: int = 0
    V12: int = 0
    Centuro: int = 0
    Livo: int = 0
    Sport: int = 0
    FZS_FI: int = 0
    Aquila: int = 0
    MT_15: int = 0
    Xpulse: int = 0
    Iron: int = 0
    Z650: int = 0
    YZF_R3: int = 0
    Victor: int = 0
    Radeon: int = 0
    SZR: int = 0
    Perak: int = 0
    GT650R: int = 0
    tres302R: int = 0
    Monster: int = 0
    Mojo: int = 0
    X_Blade: int = 0
    Bonneville: int = 0
    G: int = 0
    Achiever: int = 0
    SP125: int = 0
    Machismo: int = 0
    Honda: int = 0
    Meteor: int = 0
    FZ_FI: int = 0
    Slingshot: int = 0
    SZ_RR: int = 0
    Svartpilen: int = 0
    XCD: int = 0
    Hness: int = 0
    ER_6n: int = 0
    Imperiale: int = 0
    Saluto: int = 0
    SZ: int = 0
    Vitpilen: int = 0
    tres390: int = 0
    RX135: int = 0
    Z800: int = 0
    Gladiator: int = 0
    Z1000: int = 0
    Tiger: int = 0
    Hayate: int = 0
    RX: int = 0
    mil1200: int = 0
    Panigale: int = 0
    GSX_R: int = 0
    Discover150: int = 0
    Flame: int = 0
    Leoncino: int = 0
    Fazer25: int = 0
    CB300R: int = 0
    Crux: int = 0
    New: int = 0
    CBR1000RR: int = 0
    Boxer: int = 0
    SS: int = 0
    cuatro4S: int = 0
    CT110: int = 0
    Z900: int = 0
    SZX: int = 0
    YZFR15: int = 0
    S: int = 0
    CD110: int = 0
    MAX: int = 0
    Speed: int = 0
    Thruxton: int = 0
    Multistrada: int = 0
    FZS25: int = 0
    Z250: int = 0
    Phoenix: int = 0
    XDiavel: int = 0
    Impulse: int = 0
    Inazuma: int = 0
    Discover150S: int = 0
    Sportster: int = 0
    CBR650F: int = 0
    Fiero: int = 0
    GT: int = 0
    Scrambler: int = 0
    Vulcan: int = 0
    VT1300CX: int = 0
    YZF_R1M: int = 0
    XG750: int = 0
    YBR: int = 0
    GS: int = 0
    TRK: int = 0
    GSX_S750: int = 0


class PredictionRequest(BrandName, ModelName):
    model_name: str
    motor_size: float
    years: int
    kms_driven: float
    mileage: float
    owner: int
    power: float

class PredictionResponse(BaseModel):
    price: float

    