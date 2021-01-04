import os

print('hello')




from github import Github

g = Github('f8b71cde1741c6c22b82710f887281c0b2472eb1')


# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)

    