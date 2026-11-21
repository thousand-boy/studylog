"""ログイン・ログアウト・ユーザー登録のURL。

TODO
- "login/"：django.contrib.auth.views.LoginView（name="login"）
- "logout/"：django.contrib.auth.views.LogoutView（name="logout"、POSTのみ）
- "signup/"：SignUpView（name="signup"）
include("django.contrib.auth.urls") は使わない（パスワード再設定のURLまで公開されるため）。
"""

app_name = "accounts"
urlpatterns = []
