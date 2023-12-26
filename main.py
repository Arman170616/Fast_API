from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

company_info = {
    "name": "Sicunet INC",
    "address": "Panthopath, Dahaka, Bangladesh",
    "founder": "IKE HuH",
    "founded_year": 2006,
    "employees": 1000,
    "website": "https://yourcompany.com",

}

@app.get("/about")
def get_company_info():
    return company_info


class Service(BaseModel):
    name: str
    description: str
    price: float
    is_active: bool = True


services = []

@app.get("/services/", response_model=List[Service])
def get_services():
    return services

@app.get("/services/{service_id}", response_model=Service)
def get_service(service_id: int):
    if service_id < 0 or service_id >= len(services):
        raise HTTPException(status_code=404, detail="Service not found")
    return services[service_id]

@app.post("/services/", status_code=201)
def create_service(service: Service):
    services.append(service)
    return {"message": "Service created successfully"}

@app.put("/services/{service_id}")
def update_service(service_id: int, service: Service):
    if service_id < 0 or service_id >= len(services):
        raise HTTPException(status_code=404, detail="Service not found")
    services[service_id] = service
    return {"message": "Service updated successfully"}

@app.delete("/services/{service_id}")
def delete_service(service_id: int):
    if service_id < 0 or service_id >= len(services):
        raise HTTPException(status_code=404, detail="Service not found")
    del services[service_id]
    return {"message": "Service deleted successfully"}