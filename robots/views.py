import json
from datetime import datetime

from robots.models import Robot
from robots.service import get_week_ago, write_report_in_excel

from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import get_current_timezone
from django.db.models import Count


@csrf_exempt
@require_POST
def add_robot(request: HttpRequest):
    robot_json = json.loads(request.body)
    to_time = datetime.strptime(robot_json["created"], "%Y-%m-%d %H:%M:%S")
    robot_json["created"] = to_time.astimezone(get_current_timezone())
    robot_json['serial'] = f'{robot_json["model"]}-{robot_json["version"]}'
    robot = Robot.objects.create(**robot_json)
    return JsonResponse(
        {"Robot is created": {"model": robot.model, "version": robot.version}}
    )


def get_robots_by_week(request: HttpRequest):
    week_ago = get_week_ago()
    if request.user.is_staff:
        robot_ids = set(Robot.objects.values_list("model", flat=True))
        models = [model for model in robot_ids]
        to_excel = []
        for model in models:
            data = (
                Robot.objects.values_list("model", "version")
                .annotate(count=Count("version"))
                .filter(model=model, created__gt=week_ago)
            )
            to_excel.append(list(data))
        write_report_in_excel(to_excel)
        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        content_disposition = (
            f"filename=robots_{week_ago.day}-{week_ago.month}-{week_ago.year}"
        )
        response["Content-Disposition"] = content_disposition
        with open("media/files/robots.xlsx", "rb") as f:
            response.content = f.read()
        return response
    else:
        return redirect("robots:get_all_robots")


def get_all_robots(request: HttpRequest):
    robots = Robot.objects.all()
    return render(request, "robots/catalog.html", {"robots": robots})
