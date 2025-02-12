# run.py
from app import create_app
from app.models import db
from app.operations import populate_treatments

app = create_app('development')

if __name__ == '__main__':
    with app.app_context():
        try:
            # Create all tables in the database if they don't already exist
            db.create_all()

            # Populate default treatments data if needed
            populate_treatments()

        except Exception as e:
            print(f"Error during database setup or treatment population: {e}")
            exit(1)  # Exit gracefully on error

    try:
        # Start the Flask application in debug mode
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the Flask app: {e}")
        exit(1)  # Graceful exit on app startup failure
