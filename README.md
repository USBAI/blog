# Simple Blog Application with API

A minimalist blog application built with Django that provides both a web interface and REST API endpoints for managing blog posts.

## Assignment Information
- **Assigned to:** Elias Luzwehimana
- **Assigned by:** Asker Midov (asker@toborrow.com)

## Features
- Clean, modern web interface at root URL ("/")
- RESTful API endpoints under "/api/"
- Django admin interface for content management
- CRUD operations for blog posts
- Responsive design with a light, minimal aesthetic

## Prerequisites
- Python 3 or higher
- pip (Python package manager)
- Git

## Installation

1. Clone the repository:
```bash
git clone git@github.com:USBAI/blog.git
cd blog
```

Note: If Git asks for authentication, you can use the password: `kluret` (though the repository is public)

2. Create and activate a virtual environment (recommended):
```bash
# On Windows
python -m venv env
env\Scripts\activate

# On macOS/Linux
python3 -m venv env
source env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser for admin access:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up your admin account.

6. Start the development server:
```bash
python manage.py runserver
```

The application will be available at:
- Web Interface: http://localhost:8000/
- Admin Panel: http://localhost:8000/admin/
- API Endpoints: http://localhost:8000/api/

## API Endpoints

### List all posts
- **URL:** `/api/posts/`
- **Method:** GET
- **Response:** List of all blog posts

### Create a new post
- **URL:** `/api/posts/`
- **Method:** POST
- **Body:**
```json
{
    "title": "Your Post Title",
    "content": "Your post content"
}
```

### Get a single post
- **URL:** `/api/posts/{id}/`
- **Method:** GET
- **Response:** Single post details

### Update a post
- **URL:** `/api/posts/{id}/`
- **Method:** PUT
- **Body:**
```json
{
    "title": "Updated Title",
    "content": "Updated content"
}
```

### Delete a post
- **URL:** `/api/posts/{id}/`
- **Method:** DELETE

## Web Interface

The web interface provides a clean, modern design with the following features:
- View all posts at the root URL ("/")
- Create new posts through the "Create Post" button
- Edit and delete posts directly from the post cards
- Responsive design that works on all devices
- Clean typography and minimal UI elements

## Design Decisions

1. **Separation of Concerns:**
   - Web interface at root URL for better user experience
   - API endpoints under "/api/" for clear separation
   - Django admin for content management

2. **User Interface:**
   - Minimalist design with light color scheme
   - Fully rounded buttons for modern aesthetics
   - Responsive layout with clean typography
   - Card-based post display with hover effects

3. **Architecture:**
   - Django's built-in admin for robust content management
   - RESTful API design principles
   - Simple and straightforward data model

## Future Improvements

- User authentication and authorization
- Categories and tags for posts
- Rich text editor for post content
- Comment system
- Search functionality
- Docker containerization
- Unit tests
- CI/CD pipeline

## Contributing

This is a test project, but contributions are welcome. Please feel free to submit issues and pull requests.

## License

This project is open-source and available under the MIT License. 