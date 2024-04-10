from typing import Any, Dict, List

from django.conf import settings
from django.core.files import File
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def render_template_mail(template: str, context: Dict[Any, Any]) -> str:
    message = render_to_string(template, context)
    return message


def send_mail(
    subject: str,
    message: str,
    recipient_list: List[str],
    fail_silently: bool = False,
    attachment: File = None,
) -> Any:
    # from_email = settings.EMAIL_FROM_USER
    from_email = settings.EMAIL_HOST_USER

    headers: Dict[Any, Any] = {}

    msg = EmailMultiAlternatives(
        subject=subject,
        # body="",
        body=message,
        from_email=from_email,
        to=recipient_list,
        headers=headers,
    )
    msg.attach_alternative(message, "text/html")
    if attachment:
        msg.attach(content=attachment.file.read(), mimetype="application/pdf")

    return msg.send(fail_silently)


def send_template_mail(
    subject: str,
    template: str,
    context: Dict[Any, Any],
    recipient_list: List[str],
    fail_silently: bool = False,
) -> Any:
    context_dict = {"subject": subject, "data": context}
    message = render_template_mail(template, context_dict)
    return send_mail(
        subject,
        message,
        recipient_list,
        fail_silently,
        # attachment=context.get("Документ"),
    )
