"""ビュー（すべて Django の汎用ビュー）。

TODO（設計書「9. URL・View・Template」）
- OwnerQuerysetMixin：get_queryset() を user=self.request.user で絞る（他人のIDは404）
- StudyRecordListView（ListView）
  - select_related("category")、RecordSearchForm で検索・絞り込み・並び替え
  - 不正な検索条件は無視して初期表示にする
  - get_context_data で集計（総記録数・今月・学習した日数・今週の曜日別件数）
- StudyRecordDetailView / CreateView / UpdateView / DeleteView
  - 作成時は form_valid で form.instance.user = self.request.user
  - get_form_kwargs でフォームに user を渡す
  - カテゴリーがないときは登録画面に案内を出す（F-11）
- CategoryListView（annotate(record_count=Count("records"))）/ CreateView / UpdateView
- CategoryDeleteView
  - 確認画面に使用件数を出す
  - form_valid で RestrictedError を受け、エラーメッセージを出して一覧へ戻す
- 完了メッセージは SuccessMessageMixin
"""
