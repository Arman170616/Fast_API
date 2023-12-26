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


class Contact(BaseModel):
    name: str
    email: str
    message: str

contacts = []

@app.get("/contacts/", response_model=List[Contact])
def get_contacts():
    return contacts

@app.post("/contacts/", status_code=201)
def create_contact(contact: Contact):
    contacts.append(contact)
    return {"message": "Contact created successfully"}


@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: Contact):
    if contact_id < 0 or contact_id >= len(contacts):
        raise HTTPException(status_code=404, detail="Contact not found")
    contacts[contact_id] = contact
    return {"message": "Contact updated successfully"}

@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    if contact_id < 0 or contact_id >= len(contacts):
        raise HTTPException(status_code=404, detail="Contact not found")
    del contacts[contact_id]
    return {"message": "Contact deleted successfully"}


class Projects(BaseModel):
    name: str
    description: str
    image: str
    link: str
    is_active: bool = True

projects = []

@app.get("/projects/", response_model=List[Projects])
def get_projects():
    return projects

@app.post("/projects/", status_code=201)
def create_project(project: Projects):
    projects.append(project)
    return {"message": "Project created successfully"}

@app.put("/projects/{project_id}")
def update_project(project_id: int, project: Projects):
    if project_id < 0 or project_id >= len(projects):
        raise HTTPException(status_code=404, detail="Project not found")
    projects[project_id] = project
    return {"message": "Project updated successfully"}

@app.delete("/projects/{project_id}")
def delete_project(project_id: int):
    if project_id < 0 or project_id >= len(projects):
        raise HTTPException(status_code=404, detail="Project not found")
    del projects[project_id]
    return {"message": "Project deleted successfully"}

