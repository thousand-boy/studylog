"""URL設定。

TODO（設計書「9. URL設計」の表）：9つのURLを登録する。
- ""（record_list）、"records/new/"（record_create）、"records/<int:pk>/"（record_detail）
- "records/<int:pk>/edit/"（record_update）、"records/<int:pk>/delete/"（record_delete）
- "categories/"（category_list）、"categories/new/"（category_create）
- "categories/<int:pk>/edit/"（category_update）、"categories/<int:pk>/delete/"（category_delete）
"""

app_name = "records"
urlpatterns = []
