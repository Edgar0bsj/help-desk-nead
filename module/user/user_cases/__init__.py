from module.user.user_cases.user_alteration import UserAlteration
from module.user.user_cases.user_authentication import UserAuthentication
from module.user.user_cases.user_init import UserInit
from module.user.user_cases.user_read import UserRead


class UserLoad(UserAuthentication, UserInit, UserAlteration, UserRead):
    def __init__(self):
        UserInit.__init__(self)
        UserAlteration.__init__(self)
        UserRead.__init__(self)
        UserAuthentication.__init__(self)
