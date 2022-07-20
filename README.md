**Summary**
| Field | Detail |
|-------|--------|
| Project Name | K-DramaFever of Finch Collecter|
| Description |Central location for your K-Drama guilty pleasures |
| Developer | Chedeline Viljean|
| Live Website | https://cv-sei-222-finchcollector.herokuapp.com/ |
| Repo | https://github.com/vchedeline/finchcollector |
| Technologies | Python, Django, HTML,CSS, JavaScript, Heroku, Imgur, Github |

## Problem Being Solved and Target Market

Delve into that feverish dream where all your beloved Korean shows come alive!
Add your all time favorites, and your future favorites and keep track of them all in one place!

## User Stories

- As a user, I want login in to my account
- As a user, I want to be add K-Drama shows and Awards to my list
- As a user, I want to click on a K-Drama or award and see the details
- As a user, I want to be able to edit, update, and delete a K-Drama or an awards
- As a user, I want to be able to keep track of the days I watched specific k-dramas
- As a user, I want to be able to add pictures of the actors for the specific k-drama
- As a user, I want to be able to assign and unassign awards to the different k-dramas

## Route Tables

| Endpoint  | Response                       | Other                                                                                                      |
| --------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| /about/   | About section for the weebsite |                                                                                                            |
| /kdramas/ | Displays all of K-Dramas       | id/, id/update, id/delete, id/add_watching, id/add_photo, id/assoc_award/id, id/disassoc_award/id, create/ |
| /awards   | Displays all Awards            | id/, id/update, id/delete, create/                                                                         |
| /accounts | Link to login, logout, signup  |                                                                                                            |
| /admin    | Admin access for superuser     |                                                                                                            |

## Live Site

![Home Page](https://i.imgur.com/H2M4WxL.png)
![Home Page 2](https://i.imgur.com/z64fNfx.png)
![About Page](https://i.imgur.com/umESLD0.png)
![Awards Page](https://i.imgur.com/LaZOe2v.png)
![K-Dramas Page](https://i.imgur.com/yfRgF9k.png)
![K-Drama 1 Page](https://i.imgur.com/sAXY9MN.png)
![K-Drama 1 Page 2](https://i.imgur.com/kEL2CX7.png)
![K-Drama 2 Page](https://i.imgur.com/DY3Qa7E.png)
