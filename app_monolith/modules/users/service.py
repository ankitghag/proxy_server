from app.modules.users.repository import UserRepository


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def get_user(self, user_id: int):
        user = self.repository.get_by_id(user_id)

        if user is None:
            raise ValueError("User not found")

        return user
