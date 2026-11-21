"""フォーム。

TODO（設計書「9. View設計の要点」「10. セキュリティ設計」）
- StudyRecordForm（ModelForm）
  - fields は明示する：["title", "category", "study_date", "content", "reflection"]
  - __init__(self, *args, user, **kwargs) でカテゴリーの選択肢を自分のものに限定する
  - 学習日は DateInput(attrs={"type": "date"})
  - clean_study_date：未来の日付ならエラー（今日は timezone.localdate()）
- CategoryForm（ModelForm）
  - fields = ["name"]
  - clean_name：同じユーザーの中で名前が重複したらエラー（編集中の自分自身は除く）
    ※ user がフォームにないため、一意制約は自動では検証されない（Django ticket #36668）
- RecordSearchForm（Form）
  - q（キーワード）、category（自分のカテゴリー、任意）、sort（"new" / "old"、任意）
"""
