import logging as logger
import random
import string


def generate_random_company(domain=None, email_prefix=None):
    logger.debug("Generating random email and password.")

    if not domain:
        domain = "example.odoo"
    if not email_prefix:
        email_prefix = "autotestuser"

    random_email_string_length = 10
    random_string = "".join(random.choices(string.ascii_lowercase, k=random_email_string_length))

    email = f"{email_prefix}_{random_string}@{domain}"


