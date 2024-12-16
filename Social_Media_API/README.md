# Social Media API
A RESTful API for managing a social media platform, enabling features like user management, posts, likes, and comments, notifications.


## Features
- User authentication and authorization  

- CRUD operations for posts and comments  and profile managment

- Follow/unfollow functionality  

- Like system for posts  

- notifications system for new likes, comments, followers

## API Endpoints
| **Endpoint**                                 | **Method** | **Description**                                                        |
|----------------------------------------------|------------|------------------------------------------------------------------------|
| **Authentication**                           |            |                                                                        |
| `/account/register/`                         | POST       | Registers a new user with username, email, password.                   |
| `/account/login/`                            | POST       | Authenticates user and returns a token.                                |
| `/account/logout/`                           | POST       | Logs the user out by destroying the token.                             |
| **User Profile**                             |            |                                                                        |
| `/account/profile/<username>`                | GET        | Retrieves user profile details.                                        |
| `/api/profile/<username>`                    | PUT        | Updates user profile data.                                             |
| `/account/profile/<username>`                | PATCH      | Partially updates profile fields.                                      |
| `/account/profile/<username>`                | DELETE     | Deletes the user profile.                                              |
| **Follow System**                            |            |                                                                        |
| `/account/profile/<username>/follow/`        | POST       | Follow a user.                                                         |
| `/account/profile/<username>/unfollow/`      | DELETE     | Unfollow a user.                                                       |
| **Posts**                                    |            |                                                                        |
| `/api/posts/`                                | POST       | Creates a new post.                                                    |
| `/api/posts/<title>/`                        | GET        | Retrieves a post by title.                                             |
| `/api/posts/`                                | GET        | Retrieves all posts by the logged-in user.                             |
| `/api/posts/<title>/`                        | PUT        | Updates an existing post.                                              |
| `/api/posts/<title>/`                        | DELETE     | Deletes a specific post.                                               |
| **Feed**                                     |            |                                                                        |
| `/api/posts/feed/`                           | GET        | Retrieves the user’s feed of posts.                                    |
| **Likes**                                    |            |                                                                        |
| `/api/posts/<title>/like/`                   | POST       | Like a specific post.                                                  |
| `/api/posts/<title>/unlike/`                 | DELETE     | Remove like from a specific post.                                      |
| **Comments**                                 |            |                                                                        |
| `/api/comments/`                             | POST       | Create a new comment on a post.                                        |
| `/api/comments/`                             | GET        | Retrieves a list of all comments.                                      |
| `/api/comments/<id>/`                        | GET        | Retrieves a specific comment by ID.                                    |
| `/api/comments/<id>/`                        | PUT        | Updates an existing comment.                                           |
| `/api/comments/<id>/`                        | DELETE     | Deletes a comment by ID.                                               |
| **Notifications**                            |            |                                                                        |
| `/notification/`                             | GET        | Retrieves notifications for the user.                                  |




## Technologies will Used
- Django REST Framework, and Django
- MySql
- Built in token from DRF for authentication

## In development (we still working on the peoject)







