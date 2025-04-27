from playwright.sync_api import expect, TimeoutError
from playwright.sync_api import Page, expect

class QuotePage:
    def __init__(self, page: Page):
        self.page = page
        self.name_input = page.locator("#q_name")
        self.email_input = page.locator("#q_email")
        self.service_select = page.locator("#q_service")
        self.message_textarea = page.locator("#q_message")
        self.submit_button = page.locator("div[class='col-12']>button[type='submit']")
        self.status_message = page.locator("#quoteStatus")

    def fill_form(self, name=None, email=None, service=None, message=None):
        if name:
            self.name_input.fill(name)
        if email:
            self.email_input.fill(email)
        if service:
            self.service_select.select_option(service)
        if message:
            self.message_textarea.fill(message)

    def submit(self):
        self.submit_button.click()

    def is_success(self):
        element=self.status_message
        #expect(element).to_be_visible(timeout=20000)
        return not "d-none" in element.get_attribute("class")

    def has_error(self, field_name):
        element = getattr(self, f"{field_name}_input", None) or \
                 getattr(self, f"{field_name}_textarea", None)
        return "is-invalid" in element.get_attribute("class")