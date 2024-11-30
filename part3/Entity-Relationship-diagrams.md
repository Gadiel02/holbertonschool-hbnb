# Entity-Relationship Diagram

## Overview
This Entity-Relationship (ER) diagram represents the entities and relationships in the system. The following entities are included:
- `User`
- `Place`
- `Review`
- `Place_Amenity`

### Diagram
![Entity-Relationship Diagram](path_to_image/Entity-Relationship-diagram.png)

## Entities and Attributes
- **User**:
  - id (CHAR(36))
  - first_name (VARCHAR)
  - last_name (VARCHAR)
  - email (VARCHAR)
  - password (VARCHAR)
  - is_admin (BOOLEAN)
  - created_at (DATETIME)
  - updated_at (DATETIME)

- **Place**:
  - id (CHAR(36))
  - title (TEXT)
  - description (TEXT)
  - price (DECIMAL)
  - latitude (FLOAT)
  - longitude (FLOAT)
  - owner_id (CHAR(36))
  - created_at (DATETIME)
  - updated_at (DATETIME)

- **Review**:
  - id (CHAR(36))
  - text (TEXT)
  - rating (INT)
  - user_id (CHAR(36))
  - place_id (CHAR(36))
  - created_at (DATETIME)
  - updated_at (DATETIME)

- **Place_Amenity**:
  - place_id (CHAR(36))
  - amenity_id (CHAR(36))
  - created_at (DATETIME)
  - updated_at (DATETIME)

## Relationships
- `User` has a one-to-many relationship with `Review`.
- `Place` has a one-to-many relationship with `Review`.
- `Place` and `Amenity` have a many-to-many relationship through `Place_Amenity`.
