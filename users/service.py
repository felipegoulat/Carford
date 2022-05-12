from users.models import UserModel


class UserService():
    def  find_by_username(self, username: str):
        return UserModel.objects.filter(username=username).first()

    
    def update_user(self, user: UserModel, new_password: str):
        user.set_password(new_password)
        user.save()
        return user
        