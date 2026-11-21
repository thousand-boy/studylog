"""学習記録アプリのモデル。

TODO（設計書「7. データベース設計」）
- Category
  - user：ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name="categories")
  - name：CharField("カテゴリー名", max_length=50)
  - Meta：ordering = ["name"]、
    UniqueConstraint(fields=["user", "name"], name="unique_category_name_per_user")
  - __str__：カテゴリー名を返す
- StudyRecord
  - user：ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name="study_records")
  - category：ForeignKey(Category, on_delete=RESTRICT, related_name="records")
    （PROTECT ではなく RESTRICT。理由は設計書7章）
  - title：CharField("タイトル", max_length=100)
  - study_date：DateField("学習日", default=timezone.localdate)
  - content：TextField("学習内容")
  - reflection：TextField("振り返り・メモ", blank=True)
  - created_at：DateTimeField(auto_now_add=True)、updated_at：DateTimeField(auto_now=True)
  - Meta：ordering = ["-study_date", "-created_at"]
  - get_absolute_url：詳細画面（records:record_detail）のURLを返す

書き終えたら、次を実行してテーブルを作る。
    python manage.py makemigrations records
    python manage.py migrate
"""
