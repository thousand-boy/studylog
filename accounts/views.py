from django.contrib.auth.decorators import login_not_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView


# LoginRequiredMiddleware の対象から外し、未ログインでも開けるようにする
@method_decorator(login_not_required, name="dispatch")
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("accounts:login")
    success_message = "ユーザー登録が完了しました。ログインしてください。"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Django標準のフォームをそのまま使い、見た目のクラスだけ付ける
        for field in form.fields.values():
            field.widget.attrs["class"] = "form-control"
        return form
