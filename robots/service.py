from datetime import datetime, timedelta
from django.http import HttpResponse
from django.utils.timezone import get_current_timezone
from django.db.models import Count
import xlsxwriter

from robots.models import Robot


def get_week_ago():
    now = datetime.now()
    last_week_now = now - timedelta(days=7)
    last_week_now = last_week_now.astimezone(get_current_timezone())
    return last_week_now


def write_report_in_excel(arr: list):
    workbook = xlsxwriter.Workbook('media/files/robots.xlsx')
    bold = workbook.add_format({'bold': True})
    for data in arr:
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Модель', bold)
        worksheet.write('B1', 'Версия', bold)
        worksheet.write('C1', 'Количество за неделю', bold)
        
        row, col = 1, 0
        for model, version, amount  in data:
            worksheet.write_string(row, col, model)
            worksheet.write_string(row, col+1, version)
            worksheet.write(row, col+2, amount)
            row += 1
        worksheet.set_column('C:C', 25)
    workbook.close()


def get_excel_response(week_ago):
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