"""A collection of messages used in simple_deploy.py."""

# Module is called deploy_messages to avoid collisions with any messages.py 
#   files.
#
# Storing messages here makes for a much shorter simple_deploy.py file, and
#   makes it easier to see how the messages actually look on screen. The 
#   disadvantage is that it's harder to track what messages are being
#   displayed when working on simple_deploy.
# When you add a message here, make sure the stdout.write() call has a comment
#   that clearly summarizes what the message says.
#
# CommandError messages
# - Any message used when raising a CommandError should have a blank line after
#   the line with the opening triple quote, to separate the main error message
#   from the generic "Command Error".
#
# Line length conventions
# - Try to keep lines at the 79-char PEP 8 limit, but the project is not
#   overly strict about it at this point.
#
# - DynamicMessages
#   - It can be helpful to make a second vertical line at 86 characters
#     (78 characters + two indentation levels) to judge the line lengths
#     for dynamic messages.


from textwrap import dedent

from django.conf import settings


cancel_automate_all = """
Okay, canceling this run. If you want to configure your project
for deployment, run simple_deploy again without the --automate-all flag.
"""

requires_platform_flag = """
The --platform flag is required; you must specify which platform you want to 
deploy your project to.
- Current options are `heroku` and `platform_sh`.
- Example usage:
  $ python manage.py simple_deploy --platform heroku
  $ python manage.py simple_deploy --platform platform_sh

For more detailed information, see https://github.com/ehmatthes/django-simple-deploy/blob/main/docs/cli_args.md

Please re-run the command with a --platform option specified.
"""

unclean_git_status = """
The output of `git status` indicates that you have uncommitted changes.

We highly recommend you commit all changes before running simple_deploy, so
you can easily undo configuration changes if deployment doesn't work, or if you
wish to deploy to a different platform.

Please commit all changes and then run simple_deploy again. If you really wish
to continue without committing current changes, you can use
the --ignore-unclean-git flag.
"""


# --- Dynamic strings ---
# These need to be generated in functions, to display information that's 
#   determined as the script runs.

# No platform-agnostic dynamic strings are needed at this time.
#   However, some messages that are currently in platform-specific files
#   can probably be moved here.