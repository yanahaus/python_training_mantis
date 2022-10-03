from model.project import Project


def test_add_project(app):
    project = Project("name6", "description6")
    old_projects = app.project.get_project_list()
    if project in old_projects:
        app.project.delete_project(project)
        old_projects.remove(project)
    app.project.add_project(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)