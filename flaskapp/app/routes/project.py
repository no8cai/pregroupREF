from flask import Blueprint, redirect, Flask, request
from ..models import db,Project
import json


bp = Blueprint('project', __name__, url_prefix='/api/projects')

# Get all project data
@bp.route('')
def all_projects():
    return [project.to_dict() for project in Project.query.all()]

# Get project data by Id
@bp.route('/<int:id>')
def single_project(id):
    oneProject = Project.query.get(id).to_dict()
    return oneProject

# Create a project
@bp.route('', methods=['POST'])
def add_project():
    data=json.loads(request.data)
    newproject=Project(**data)
    db.session.add(newproject)
    db.session.commit()
    return newproject.to_dict()

# Edit a project
@bp.route('/<int:id>', methods=['PUT'])
def edit_project(id):
    
    data=json.loads(request.data)
    Project.query.filter(Project.id==id).update(data)
    db.session.commit()
    return Project.query.get(id).to_dict()

# Delete a project
@bp.route('/<int:id>', methods=['DELETE'])
def delete_project(id):
    oneProject = Project.query.get(id)
    db.session.delete(oneProject)
    db.session.commit()
    return "delete succeful"



#post /
# @bp.route('', methods=['POST'])
# def main_page_add_pokemon():
    # form = PokemonForm()
    # form['csrf_token'].data = request.cookies['csrf_token']
    # if form.validate_on_submit():
    #     data = Pokemon()
    #     form.populate_obj(data)
    #     db.session.add(data)
    #     db.session.commit()
    
    # json post
    # data=json.loads(request.data)
    # temp=data["name"]
    
    # form post
    
    # try:
    #    form = SimpleForm(name=request.form.get("name"))
    #    result="good"
    # except:
    #    result="bad"
    # return result
