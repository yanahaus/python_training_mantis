from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def add_project(self, project):
        wd = self.app.wd
        self.go_to_projects_page()
        self.init_project_creation()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        if project.description is not None:
            wd.find_element_by_name("description").click()
            wd.find_element_by_name("description").clear()
            wd.find_element_by_name("description").send_keys(project.description)
        self.submit_project_creation()
        self.project_cache = None

    def delete_project(self, project):
        wd = self.app.wd
        self.go_to_projects_page()
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_css_selector("form > input.button").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_css_selector("input.button").click()
        self.project_cache = None

    def go_to_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def init_project_creation(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("td.form-title > form > input.button-small").click()

    def submit_project_creation(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input.button").click()

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.go_to_projects_page()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector("table.width100 tr[class^='row']")[1:]:
                name = element.find_element_by_css_selector('a').text
                description = element.find_elements_by_css_selector('td')[4].text
                id = element.find_element_by_css_selector('a').get_attribute("href").split('=')[-1]
                self.project_cache.append(Project(name=name, description=description))
        return list(self.project_cache)

