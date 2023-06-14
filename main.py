import os


def main():
    print("starting")
    global project_name
    project_name = input("project name: ")

    global working_directory_path
    working_directory_path = os.getcwd()
    global project_folder_path
    project_folder_path = os.path.join(working_directory_path, project_name)
    os.mkdir(project_folder_path)

    
    os.mkdir(os.path.join(get_project_folder_path(), "resources"))

    running = True
    pages=[]
    while running:
        page_name = input("page name, q to quit:")
        if(page_name=="q"): break
        pages.append(page_name)
        make_page(page_name)
    
    generate_file_with_text("index.html", 
        get_resource_text("index.html.txt").format(name=project_name, 
            links = "\n\t".join(["<a href='./resources/{0}/{0}.html'>{0}</a>"
                .format(name) for name in pages])
        )
    )
    print("done")


def make_page(name):
    page_path = os.path.join(get_project_folder_path(), "resources", name)
    os.mkdir(page_path)
    generate_file_in_folder_with_text(page_path, name+".html",
            get_resource_text("page.html.txt").format(title=project_name,name=name))
    generate_file_in_folder(page_path, name+".css")
    generate_file_in_folder(page_path, name+".js")




def generate_file(name):
    open(get_project_folder_path(name), "w").close()


def generate_file_with_path(path):
    open(path, "w").close()


def generate_file_in_folder(path, name):
    open(os.path.join(path, name), "w").close()


def generate_file_with_text(name, text):
    with open(get_project_folder_path(name), "w") as file:
        file.write(text)


def generate_file_with_text_and_path(path, text):
    with open(path, "w") as file:
        file.write(text)

def generate_file_in_folder_with_text(path, name, text):
    with open(os.path.join(path, name), "w") as file:
        file.write(text)


def get_project_folder_path(name=""):
    return os.path.join(project_folder_path, name)


def get_working_folder_path(name=""):
    return os.path.join(working_directory_path, name)


def get_resource_text(name):
    return open(get_relative_file_path(name), "r").read()


def get_relative_file_path(name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), name)


if __name__=="__main__": main()
