Here is a comprehensive list of all the commonly used `manage.py` commands in Django, along with descriptions of what each command does:

### Core Django Commands

1. **`python manage.py runserver`**
   - Starts the development server on the default port `8000`.
   - You can specify the port and IP, for example: `python manage.py runserver 8080`.

2. **`python manage.py migrate`**
   - Applies migrations to the database, creating or updating tables based on the models defined in the project.

3. **`python manage.py makemigrations`**
   - Creates new migrations based on the changes detected in your models.

4. **`python manage.py createsuperuser`**
   - Creates a new superuser account with admin privileges.

5. **`python manage.py startapp <appname>`**
   - Creates a new Django app with the provided name within the project.

6. **`python manage.py startproject <projectname>`**
   - Starts a new Django project with the provided project name.

7. **`python manage.py shell`**
   - Opens the interactive Python shell, with your Django environment pre-loaded.

8. **`python manage.py sqlmigrate <app_label> <migration_number>`**
   - Displays the raw SQL for a specific migration for a given app and migration number.

9. **`python manage.py showmigrations`**
   - Shows all migrations and their applied/unapplied status.

10. **`python manage.py dbshell`**
    - Opens the database shell for running SQL queries directly on the database.

11. **`python manage.py collectstatic`**
    - Gathers all static files from your apps into a single directory (usually for deployment).

12. **`python manage.py check`**
    - Checks the project for potential problems or errors without making any database changes.

13. **`python manage.py test`**
    - Runs the test suite for the project to ensure code quality and correctness.

14. **`python manage.py flush`**
    - Deletes all data in the database and returns it to the initial migration state.

15. **`python manage.py changepassword <username>`**
    - Changes the password for the specified user.

16. **`python manage.py diffsettings`**
    - Shows the difference between the current settings file and Django’s default settings.

17. **`python manage.py loaddata <fixture_file>`**
    - Loads data from a fixture file into the database.

18. **`python manage.py dumpdata <app_label.ModelName>`**
    - Outputs the contents of a model as a JSON fixture file.

19. **`python manage.py clearsessions`**
    - Clears expired sessions from the database.

20. **`python manage.py sqlflush`**
    - Returns the SQL commands needed to flush the database (used with `flush`).

21. **`python manage.py inspectdb`**
    - Generates models from an existing database.

22. **`python manage.py compilemessages`**
    - Compiles `.po` files to `.mo` files for translation.

23. **`python manage.py makemessages -l <language_code>`**
    - Extracts all translatable strings into a `.po` file for a given language.

24. **`python manage.py createsuperuser`**
    - Allows you to create an admin user interactively via the terminal.

25. **`python manage.py collectstatic`**
    - Collects static files into the location defined in `STATIC_ROOT` for production use.

26. **`python manage.py migrate --fake <app_label> <migration_name>`**
    - Marks the migration as applied without actually running it, useful in certain advanced migration cases.

27. **`python manage.py showmigrations <app_label>`**
    - Lists the migration status for a specific app.

28. **`python manage.py sqlsequencereset <app_label>`**
    - Resets the database sequence for an app’s models (useful when working with PostgreSQL or other databases that use sequences).

### For Django Extensions (optional commands if you install `django-extensions`):

1. **`python manage.py graph_models`**
   - Generates a visual graph of your models using Graphviz.

2. **`python manage.py runscript <script_name>`**
   - Runs a custom script placed in a special directory.

3. **`python manage.py show_urls`**
   - Displays all of the URLs configured in your project.

These are the essential `manage.py` commands you’ll use when working with a Django project, covering development, testing, migration management, and administration tasks.