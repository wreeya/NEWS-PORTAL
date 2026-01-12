import csv

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.generic import View

User = get_user_model()

COLUMNS = [
    "first_name",
    "last_name",
    "username",
    "email",
    "is_staff",
    "is_active",
    "is_superuser",
    "last_login",
    "date_joined",
]


class UserReportView(View):
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="users.csv"'

        writer = csv.writer(response)
        writer.writerow(COLUMNS)

        for user in User.objects.all():
            writer.writerow([
                user.first_name,
                user.last_name,
                user.username,
                user.email,
                user.is_staff,
                user.is_active,
                user.is_superuser,
                user.last_login,
                user.date_joined,
            ])

        return response

