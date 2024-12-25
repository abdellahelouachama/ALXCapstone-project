# Social Media API

This Social Media API is a robust and scalable backend solution designed to power social media platforms. It offers essential features such as user authentication (registration, login, and logout), post management, and profile management. Users can interact dynamically by following and unfollowing others, commenting on posts, and liking content. Additionally, the API supports a notification system to keep users informed about important interactions. Built with modern web technologies, this API is tailored to deliver a seamless and efficient user experience while providing a solid foundation for further enhancements.


## Features

- User authentication (registration, login, and logout)
- Post management
- Profile management
- Following and unfollowing users
- Commenting and liking posts
- Notifications

## Technologies Used

- **Backend Framework**:
  ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
- **Database**:
  ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
  

## API Endpoints

## Authentication Endpoints

| Endpoint                          | Description |
|-----------------------------------|-------------|
| `POST /account/register/`         | Registers a new user with required fields (username, password, email) and optional fields (first_name, last_name, profile_picture, bio). Responds with 201 Created and a success message. |
| `POST /account/login/`            | Validates user credentials (username, password) and returns a token if successful. Responds with 200 OK and token, or 401 unauthorized for invalid credentials. |
| `POST /account/logout/`           | Logs out a user by invalidating the token. Responds with 200 OK and a success message, or  if the token is invalid 401 unauthorized. |

## User Management Endpoints

| Endpoint                            | Description |
|-------------------------------------|-------------|
| `GET /account/profile/<username>`   | Retrieves profile information for the specified user. Responds with 200 OK or 404 Not Found if the user doesn’t exist. |
| `PUT /api/profile/<username>`       | Updates user information with required fields (username, password, email). Responds with 200 OK on success, or 400 Bad Request if validation fails. |
| `PATCH /account/profile/<username>` | Updates partial user information. Responds with 200 OK on success, or 400 Bad Request if validation fails. |
| `DELETE /account/profile/<username>`| Deletes a user profile. Responds with 204 No Content on success or 404 Not Found if the user is not found. |

## Follow System Endpoints

| Endpoint                             | Description |
|--------------------------------------|-------------|
| `POST /account/follow/<username>`    | Allows the logged-in user to follow another user. Responds with a confirmation message on success, or an error if the action cannot be completed. |
| `DELETE /account/unfollow/<username>`| Allows the logged-in user to unfollow another user. Responds with 200 OK or 404 Not Found if the user was not followed |

## Post Management Endpoints

| Endpoint                            | Description |
|-------------------------------------|-------------|
| `POST /api/posts/`                  | Creates a new post with content, title, and required fields. Responds with 201 Created on success. |
| `GET /api/posts/<title>/`           | Retrieves a post by title. Responds with 200 OK on success, or 404 Not Found if the post doesn’t exist. |
| `PUT /api/posts/<title>/`           | Updates an existing post by title. Responds with 200 OK on success, or 404 Not Found if the post is not found. |
| `DELETE /api/posts/<title>/`        | Deletes a post by title. Responds with 204 No Content on success, or 404 Not Found if the post is not found. |

## Feed of Posts Endpoints

| Endpoint                     | Description |
|------------------------------|-------------|
| `GET /api/feed/`              | Retrieves a personalized feed of posts for the logged-in user. Responds with 200 OK and a list of posts, or 401 Unauthorized if the user is not logged in. |

## Liking System Endpoints

| Endpoint                              | Description |
|---------------------------------------|-------------|
| `POST /api/posts/<title>/like/`       | Likes a post. Responds with 201 created if successful, or 404 Not Found if the post does not exist. |
| `DELETE /api/posts/<title>/unlike/`   | Removes like from a post. Responds with 200 OK if successful, or 404 Not Found if the post was not liked. |

## Comment Endpoints

| Endpoint                              | Description |
|---------------------------------------|-------------|
| `POST /api/comments/`                 | Creates a comment on a post. Responds with 201 Created on success, or 400 Bad Request if the data is invalid. |
| `GET /api/comments/`                  | Lists all comments. Responds with 200 OK and a paginated list of comments. |
| `GET /api/comments/<id>/`             | Retrieves a specific comment by ID. Responds with 200 OK if found, or 404 Not Found if the comment does not exist. |
| `PUT /api/comments/<id>/`             | Updates a comment. Responds with 200 OK on success, or 403 Forbidden if the user is not authorized to edit the comment. |
| `DELETE /api/comments/<id>/`          | Deletes a comment. Responds with 200 OK on success, or 404 Not Found if the comment does not exist. |

## Notifications Endpoints

| Endpoint                             | Description |
|--------------------------------------|-------------|
| `GET /notification/notifications/`   | Retrieves a list of notifications for the logged-in user. Responds with 200 OK and a paginated list of notifications. |



## Setup and Installation

1. Clone the repository:
   ```bash
  git clone https://github.com/your-username/social-media-api.git

2. Navigate to the Project Directory : 
  ```bash
  cd /path/to/project

3. Install the dependencies :
  ```bash
  pip install -r requirements.txt


