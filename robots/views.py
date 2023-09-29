from robots.models import Robot
from robots.serializers import RobotSerializer
from robots.service import get_excel_response, get_week_ago, write_report_in_excel

from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.response import Response
    

class CreateRobotView(APIView):
    def post(self, request):
        serializer = RobotSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Success': 'Robot is succesfully created'})


def get_excel_file(request: HttpRequest):
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
        return get_excel_response(week_ago)
    else:
        return redirect("robots:get_all_robots")


def get_all_robots(request: HttpRequest):
    robots = Robot.objects.values("model", "version", "serial").annotate(
        count=Count("version")
    )
    selled_robots = (
        Robot.objects.filter(is_ordered=True)
        .values("model", "version", "serial")
        .annotate(count=Count("version"))
    )
    for a_robot in robots:
        for s_robot in selled_robots:
            if a_robot["serial"] == s_robot["serial"]:
                a_robot["count"] -= s_robot["count"]
    return render(request, "robots/catalog.html", {"robots": robots})
