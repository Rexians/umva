from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from api.routes import guardian_info

app = FastAPI()
app.include_router(guardian_info.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    errors = exc.errors()
    error_content = "The following arguments are missing/invalid: "
    for error in errors:
        if error["type"] == "value_error.missing":
            field = f"{error['loc'][1]}, "
            error_content += field
        elif error["type"] == "type_error.integer":
            field = f"{error['loc'][1]}, "
            error_content += field
    error_content = error_content.removesuffix(", ")

    return JSONResponse({"detail": error_content}, status_code=422)


@app.get("/")
def home():
    """
    Home Page to get Information, and version
    """
    version = "1.0.0"
    home_dict = {
        "information": "Unofficial Disney Mirrorverse API, Abbreviated as UMVA, Is a API developed for DMV Players. More information soon.",
        "documentation": "Coming Soon",
        "version": version,
    }
    return home_dict
