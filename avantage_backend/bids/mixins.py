from avantage_backend.core.email import send_email


class SendEmailMixin:
    email_subject: str = ""
    template = "emails/bid.html"
    email_recipient = ""

    @property
    def to_dict(self):  # type: ignore
        raise NotImplementedError()

    def send_email(self) -> None:
        if not self.email_recipient:
            return None
        send_email(
            self.email_subject,
            self.template,
            self.to_dict,
            [self.email_recipient],
        )
