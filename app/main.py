from fastapi import FastAPI

app =FastAPI(title="Urbanlife Apı")
@app.get("/")
def root():
    return {"message":"urbalife Api is running"}
