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

class Team(BaseModel):
    name: str
    designation: str
    image: str
    is_active: bool = True

teams = []


@app.get("/teams/", response_model=List[Team])
def get_teams():
    return teams

@app.post("/teams/", status_code=201)
def create_team(team: Team):
    teams.append(team)
    return {"message": "Team created successfully"}


@app.put("/teams/{team_id}")
def update_team(team_id: int, team: Team):
    if team_id < 0 or team_id >= len(teams):
        raise HTTPException(status_code=404, detail="Team not found")
    teams[team_id] = team
    return {"message": "Team updated successfully"}

@app.delete("/teams/{team_id}")
def delete_team(team_id: int):
    if team_id < 0 or team_id >= len(teams):
        raise HTTPException(status_code=404, detail="Team not found")
    del teams[team_id]
    return {"message": "Team deleted successfully"}

class Testimonial(BaseModel):
    name: str
    designation: str
    image: str
    comment: str
    is_active: bool = True

testimonials = []


@app.get("/testimonials/", response_model=List[Testimonial])
def get_testimonials():
    return testimonials


@app.post("/testimonials/", status_code=201)
def create_testimonial(testimonial: Testimonial):
    testimonials.append(testimonial)
    return {"message": "Testimonial created successfully"}

@app.put("/testimonials/{testimonial_id}")
def update_testimonial(testimonial_id: int, testimonial: Testimonial):
    if testimonial_id < 0 or testimonial_id >= len(testimonials):
        raise HTTPException(status_code=404, detail="Testimonial not found")
    testimonials[testimonial_id] = testimonial
    return {"message": "Testimonial updated successfully"}

@app.delete("/testimonials/{testimonial_id}")
def delete_testimonial(testimonial_id: int):
    if testimonial_id < 0 or testimonial_id >= len(testimonials):
        raise HTTPException(status_code=404, detail="Testimonial not found")
    del testimonials[testimonial_id]
    return {"message": "Testimonial deleted successfully"}


class Blog(BaseModel):
    title: str
    description: str
    image: str
    link: str
    is_active: bool = True

blogs = []

@app.get("/blogs/", response_model=List[Blog])
def get_blogs():
    return blogs


@app.post("/blogs/", status_code=201)
def create_blog(blog: Blog):
    blogs.append(blog)
    return {"message": "Blog created successfully"}

@app.put("/blogs/{blog_id}")
def update_blog(blog_id: int, blog: Blog):
    if blog_id < 0 or blog_id >= len(blogs):
        raise HTTPException(status_code=404, detail="Blog not found")
    blogs[blog_id] = blog
    return {"message": "Blog updated successfully"}


@app.delete("/blogs/{blog_id}")
def delete_blog(blog_id: int):
    if blog_id < 0 or blog_id >= len(blogs):
        raise HTTPException(status_code=404, detail="Blog not found")
    del blogs[blog_id]
    return {"message": "Blog deleted successfully"}


class Client(BaseModel):
    name: str
    image: str
    is_active: bool = True

clients = []


@app.get("/clients/", response_model=List[Client])
def get_clients():
    return clients

@app.post("/clients/", status_code=201)
def create_client(client: Client):
    clients.append(client)
    return {"message": "Client created successfully"}

@app.put("/clients/{client_id}")
def update_client(client_id: int, client: Client):
    if client_id < 0 or client_id >= len(clients):
        raise HTTPException(status_code=404, detail="Client not found")
    clients[client_id] = client
    return {"message": "Client updated successfully"}

@app.delete("/clients/{client_id}")
def delete_client(client_id: int):
    if client_id < 0 or client_id >= len(clients):
        raise HTTPException(status_code=404, detail="Client not found")
    del clients[client_id]
    return {"message": "Client deleted successfully"}



