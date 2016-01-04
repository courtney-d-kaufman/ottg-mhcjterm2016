# history > history.txt


# automatically run a web browser
from selenium import webdriver

# Edith has head about a cool new online to-do app.
# Xe goes to check out its homepage
browser = webdriver.Firefox()
# port 8000, where it is going to be, start a server on port 8000
browser.get('http://localhost:8000')

# write the assertion (test) before writing the program
# we can't find Django because there isn't anything there in the first place
# http://127.0.0.1:8000/

# built in construct in python, does that string (Django)
# show up anywhere in that variable (browser, reference to something that managaes firefox browser window)
# .title (the label on the tab in web browser)
# assert -- does this resolve to true, if so assert goes on its merry way, otherwise throws a new execption

# Xe notices the page title and header mention to-do lists.
# Feel free to use non-cisgender pronouns, the book uses she
#assert 'Django' in browser.title

assert 'To-Do' in browser.title
# Xe is invited to enter a to-do item straight away

# Xe types "Buy peacock feathers" into a text box
# (Edith's hobby is tying fly-fishing lures)

# When xe hits enter, the page updates, and now the page lists
# "1. Buy peacock feathers" as an item in a to-do lists

# There is still a text book inviting xyr to add another item.
# Xe enters 'Use peacock feathers to make fly'
# (Edith is very methodical)

# The homepage updates again, and now shows both items on xyr lists

# Edith wonders whether the site with remember xyr list. Then xe sees
# THat the sit has generated a unique url for xyr -- there is some
# explanatory text to that effect.

# Xe visites that url


browser.quit()





# Nothing in software has ever been intuitive



# Test for false
if ! 'Django' in browser.title:
    throw new AssertionError

# git allows us to keep revision history, source control is that on steroids
# git is source control program
# git -V or git -- version


# git status -- what's going on with project that git cares about
# initial commit -- haven't made any changes yet
# git add -- tell git we care about these files git add .
# git commit -- save changes
# .pyc is a compiled python file, binary, don't want in source control, they're generated
# echo '*.pyc' >> .gitignore -- git creates a file to ignore .pyc files every time
