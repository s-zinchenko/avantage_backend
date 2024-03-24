from typing import Dict, Any, List

from utils.email import send_template_mail


def send_email(
    subject: str, template: str, data: Dict[Any, Any], recipients: List[str]
) -> None:
    try:
        send_template_mail(subject, template, data, recipients)
    except Exception as e:
        print(e)
