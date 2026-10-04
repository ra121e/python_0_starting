def count_in_list(lst, item):
    return lst.count(item)

# step of the package flow
# 1. make directory tree as
# project root(ex09)
# ├── ft_package
# │   ├── count_in_list.py
# │   └── __init___.py
# ├── pyproject.toml
# │
# └── test.py
#
# 2. make function and module as count_in_list.py
# 3. make __init__.py for package
# 4. make pyproject.toml for distribution
# 5. pip install . set package into active venv
# 6. python3 -m build make dist files
