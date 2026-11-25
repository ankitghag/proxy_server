class UserRepository:

    def get_by_id(self, user_id: int):
        return {
            "id": user_id,
            "name": "John",
            "email": "john@example.com",
        }
