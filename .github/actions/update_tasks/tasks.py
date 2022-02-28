import os
import re
import git
import pandoc
from pandoc import types


def get_git_root(path:str) -> str:
    git_repo = git.Repo(path, search_parent_directories=True)
    return git_repo.git.rev_parse('--show-toplevel')


def get_all_task_docs_paths(root:str='.', name:str='README.md') -> list[str]:
    task_docs = []
    for path, _, files in os.walk(root):
        for file in files:
            if file.endswith(name) and path != root:
                task_docs.append(os.path.join(path, file))
    return task_docs


def get_task_docs_data(file:str) -> map:
    data = {}
    with open(file) as f:
        content = pandoc.read(f.read())
    for elt in pandoc.iter(content):
        if isinstance(elt, types.Header):
            if not 'name' in data:
                data['name'] = pandoc.write(elt).lstrip('#').strip().split('\n')[0]
        elif isinstance(elt, types.Para):
            if not 'description' in data:
                data['description'] = pandoc.write(elt).strip()
        if 'name' in data and 'description' in data:
            break
    return data


def path_to_link(path:str, repository:str='github.com/happyRip/judge', branch:str='master') -> str:
    return 'https://{}/tree/{}/{}'.format(
        repository,
        branch,
        os.path.dirname(os.path.relpath(path, get_git_root(os.getcwd())))
    )


def task_data_to_markdown(task_data:map) -> str:
    tasks_md = ''
    for path, values in task_data.items():
        tasks_md += '- [ ] [{}]({}) - {}\n\n'.format(
            values['name'],
            path_to_link(path),
            values['description'])
    return tasks_md[:-1]


def fill_base_file(task_data:str, file:str='README.md', base:str='base.md'):
    with open(file, mode='w') as f:
        with open(base, mode='r') as b:
            pattern = re.compile('^#+\sTasks')
            for line in b:
                f.write(line)
                if pattern.search(line):
                    f.write('\n' + task_data)            
        

def main():
    task_docs = get_all_task_docs_paths(root=os.getcwd())

    tasks = {}
    for file in task_docs:
        tasks[file] = get_task_docs_data(file)

    fill_base_file(task_data_to_markdown(tasks))


if __name__ == '__main__':
    main()
