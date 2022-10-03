from model.project import Project
import random


def test_delete_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.add_project(Project(name="project_new"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)