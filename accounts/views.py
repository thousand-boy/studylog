"""ユーザー登録のビュー。

TODO
- SignUpView（CreateView）
  - form_class = UserCreationForm、template_name = "registration/signup.html"
  - 登録後はログイン画面（accounts:login）へ移動する
  - @method_decorator(login_not_required, name="dispatch") で未ログインでも開けるようにする
"""
