from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Insights Platform"
        }

@app.get("/about")
def about():
    return {
           "project": "Employee Insights Platform",
            "version": "1.0"
    }  

@app.get("/health")
def health():
    return {
        "status": "OK",
        "application": "Employee Insights Platform"
    }      