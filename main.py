import os


def main():
    print("starting")
    project_name = input("project name: ")

    global working_directory_path
    working_directory_path = os.getcwd()
    global project_folder_path
    project_folder_path = os.path.join(working_directory_path, project_name)
    os.mkdir(project_folder_path)

    generate_file_with_text("index.html", get_text_from_file("index.html.txt").format(name=project_name))
    os.mkdir(os.path.join(get_project_folder_path(), "resources"))

    running = True
    while running:
        page_name = input("page name, q to quit:")
        if(page_name=="q"): break
    
    print("done")


def make_page(name):
    page_path = os.path.join(get_project_folder_path(), name)




def generate_file(name):
    open(get_project_folder_path(name), "w").close()


def generate_file_with_path(path):
    open(path, "w").close()


def generate_file_with_path_and_name(path, name):
    open(os.path.join(path, name), "w").close()


def generate_file_with_text(name, text):
    with open(get_project_folder_path(name), "w") as file:
        file.write(text)


def generate_file_with_text_and_path(path, text):
    with open(path, "w") as file:
        file.write(text)

def generate_file_with_text_and_path_and_name(path, name, text):
    with open(os.path.join(path, name), "w") as file:
        file.write(text)


def get_project_folder_path(name=""):
    return os.path.join(project_folder_path, name)


def get_working_folder_path(name=""):
    return os.path.join(working_directory_path, name)


def get_text_from_file(name):
    return open(get_working_folder_path(name), "r").read()


if __name__=="__main__": main()
